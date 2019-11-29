from __future__ import print_function

try:
    import urllib.parse as urlparse
except ImportError:
    import urlparse as urlparse

import re

# html_helper.py contains the logic for parsing HTML and getting useful URLs
# from it

def clean_up_href(href):
    '''Browsers do all kinds of crazy things to make their hrefs valid even when
    they're sketchy. For example, spaces get autoescaped on Chrome.'''
    return href.replace(" ", "%20")


def absolutize_path(path, base_path):
    if path and path[0] != "/" or path.startswith("/."):
        sections = re.sub("/([^/]*)$", "", base_path).split("/") + \
            path.split("/")
        out = []
        for section in sections:
            if section == "." or section == "":
                pass
            elif section == "..":
                out.pop()
            else:
                out.append(section)

        return "/" + "/".join(out)
    else:
        return path

def get_neighbors(body_str, url):
    paths_to_follow = get_url_strings_from_doc(body_str)

    return get_urls_from_page(paths_to_follow, url)

def get_urls_from_page(paths_to_follow, url):
    # here's how that tuple is formatted:
    #  scheme://netloc/path;parameters?query#fragment
    parent_url_tuple = urlparse.urlparse(url)

    out = []
    errors = []

    for href in paths_to_follow:
        href = clean_up_href(href)

        # turning it into a list for mutability
        child_url_list = list(urlparse.urlparse(href))

        # This is a regular expression which checks that a section of a URL only
        # has valid characters in it. If we don't do this, the requests library
        # will throw an exception because we're giving it invalid inputs.
        valid_section_regex = "\\A[a-zA-Z0-9._~!$&'()*+,;=:@/\-]*$"

        if any(not re.search(valid_section_regex, part) for part in child_url_list):
            errors.append("The page {0} has an href of {1}, which is not a valid URI"
                .format(url, href))
            continue

        if href.startswith("mailto"):
            continue

        # empty the fragment
        child_url_list[5] = ""

        # default scheme is http
        if not child_url_list[0]:
            child_url_list[0] = "http"

        # If the network location was unspecified, copy the network location of
        #  the parent url.
        if not child_url_list[1]:
            child_url_list[2] = absolutize_path(
                child_url_list[2], parent_url_tuple[2])
            child_url_list[1] = parent_url_tuple[1]
            child_url_list[0] = parent_url_tuple[0]

        out.append(urlparse.urlunparse(child_url_list))

    return (out, errors)

def get_hrefs_from_a_tags(body_str):
    return re.findall(r'<a [^>]*href="([^"]*)"', body_str)

def get_hrefs_from_link_tags(body_str):
    return re.findall(r'<link [^>]*href="([^"]*)"', body_str)

def get_srcs_from_script_tags(body_str):
    return re.findall(r'<script [^>]*src="([^"]*)"', body_str)

def get_url_strings_from_doc(body_str):
    return (get_srcs_from_script_tags(body_str) +
            get_hrefs_from_link_tags(body_str) +
            get_hrefs_from_a_tags(body_str))
