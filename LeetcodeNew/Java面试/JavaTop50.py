"""
https://github.com/faif/python-patterns
https://github.com/PacktPublishing/Mastering-Python-Design-Patterns-Second-Edition/tree/master/chapter07

https://github.com/rajan2275/Python-Design-Patterns/tree/master/Creational
https://github.com/ivkalita/python-design-patterns



1、面向对象的特征有哪些方面?
1)抽象
2)继承
3)封装
4)多态性

2、访问修饰符public,private,protected,以及不写（默认）时的区别？

答：区别如下：

作用域        当前类     同包   子类    其他

public        √        √       √      √

protected     √        √       √      ×

default       √        √       ×      ×

private       √        ×       ×      ×

受保护（protected）对子类相当于公开，对不是同一包中的没有父子关系的类相当于私有


3、String 是最基本的数据类型吗?

不是。Java中的基本数据类型只有8个：byte、short、int、long、float、double、char、boolean；
除了基本类型（primitive type）和枚举类型（enumeration type），

剩下的都是引用类型（reference type）

4、float f=3.4;是否正确?
答:不正确。3.4是双精度数，将双精度型（double）赋值给浮点型（float）属于下转型（down-casting，也称为窄化）
会造成精度损失，因此需要强制类型转换float f =(float)3.4; 或者写成float f =3.4F;

5、short s1 = 1; s1 = s1 + 1;有错吗?short s1 = 1; s1 += 1;有错吗?
答：对于short s1 = 1; s1 = s1 + 1;由于1是int类型，因此s1+1运算结果也是int 型，需要强制转换类型才能赋值给short型。
而short s1 = 1; s1 += 1;可以正确编译，因为s1+= 1;相当于s1 = (short)(s1 + 1);其中有隐含的强制类型转换


6、Java 有没有goto?
答：goto 是Java中的保留字，在目前版本的Java中没有使用

7、int 和Integer 有什么区别?
答：Java是一个近乎纯洁的面向对象编程语言，但是为了编程的方便还是引入不是对象的基本数据类型，
但是为了能够将这些基本数据类型当成对象操作，Java为每一个基本数据类型都引入了对应的包装类型（wrapper class），
int的包装类就是Integer，从JDK 1.5开始引入了自动装箱/拆箱机制，使得二者可以相互转换。

Java 为每个原始类型提供了包装类型：
原始类型: boolean，char，byte，short，int，long，float，double
包装类型：Boolean，Character，Byte，Short，Integer，Long，Float，Double


package com.lovo;

public class AutoUnboxingTest {

	public static void main(String[] args) {
		Integer a = new Integer(3);
		Integer b = 3;				// 将3自动装箱成Integer类型
		int c = 3;
		System.out.println(a == b);	// false 两个引用没有引用同一对象
		System.out.println(a == c);	// true a自动拆箱成int类型再和c比较
	}

补充：最近还遇到一个面试题，也是和自动装箱和拆箱相关的，代码如下所示：

public class Test03 {

	public static void main(String[] args) {
		Integer f1 = 100, f2 = 100, f3 = 150, f4 = 150;

		System.out.println(f1 == f2);
		System.out.println(f3 == f4);
	}

如果不明就里很容易认为两个输出要么都是true要么都是false。
首先需要注意的是f1、f2、f3、f4四个变量都是Integer对象，所以下面的==运算比较的不是值而是引用。
装箱的本质是什么呢？当我们给一个Integer对象赋一个int值的时候，会调用Integer类的静态方法valueOf，
如果看看valueOf的源代码就知道发生了什么。

public static Integer valueOf(int i) {
        if (i >= IntegerCache.low && i <= IntegerCache.high)
            return IntegerCache.cache[i + (-IntegerCache.low)];
        return new Integer(i);

8、&和&&的区别？
答：&运算符有两种用法：(1)按位与；(2)逻辑与
&& and ||, once we check the left as false, we will skip the right side, that's why we call it 短路与

9、解释内存中的栈（stack）、堆(heap)和静态存储区的用法。
答：通常我们定义一个基本数据类型的变量，一个对象的引用，还有就是函数调用的现场保存都使用内存中的栈空间
而通过new关键字和构造器创建的对象放在堆空间

程序中的字面量（literal）如直接书写的100、“hello”和常量都是放在静态存储区中
栈空间操作最快但是也很小，通常大量的对象都是放在堆空间，整个内存包括硬盘上的虚拟内存都可以被当成堆空间来使用

String str = new String(“hello”);
上面的语句中str放在栈上，用new创建出来的字符串对象放在堆上，而“hello”这个字面量放在静态存储区


10、Math.round(11.5) 等于多少? Math.round(-11.5)等于多少?
答：Math.round(11.5)的返回值是12，Math.round(-11.5)的返回值是-11。四舍五入的原理是在参数上加0.5然后进行下取整。

11、swtich 是否能作用在byte 上，是否能作用在long 上，是否能作用在String上?
答：早期的JDK中，switch（expr）中，expr可以是byte、short、char、int
从1.5版开始，Java中引入了枚举类型（enum），expr也可以是枚举，从JDK 1.7版开始，
还可以是字符串（String）。长整型（long）是不可以的。

12、用最有效率的方法计算2乘以8?
答： 2 << 3（左移3位相当于乘以2的3次方，右移3位相当于除以2的3次方）。

补充：我们为编写的类重写hashCode方法时，可能会看到如下所示的代码，
其实我们不太理解为什么要使用这样的乘法运算来产生哈希码（散列码），而且为什么这个数是个素数，
为什么通常选择31这个数？前两个问题的答案你可以自己百度一下，选择31是因为可以用移位和减法运算来代替乘法，
从而得到更好的性能。说到这里你可能已经想到了：31 * num <==> (num << 5) - num，
左移5位相当于乘以2的5次方（32）再减去自身就相当于乘以31。现在的VM都能自动完成这个优化

13、数组有没有length()方法?String 有没有length()方法？
答：数组没有length()方法，有length 的属性。
String 有length()方法。
JavaScript中，获得字符串的长度是通过length属性得到的，这一点容易和Java混淆。

14、在Java 中，如何跳出当前的多重嵌套循环？
break和continue

15、构造器（constructor）是否可被重写（override）?
答：构造器不能被继承，因此不能被重写，但可以被重载。

16、两个对象值相同(x.equals(y) == true)，但却可有不同的hash code，这句话对不对？

答：不对，如果两个对象x和y满足x.equals(y) == true，它们的哈希码（hash code）应当相同。
Java对于eqauls方法和hashCode方法是这样规定的：(1)如果两个对象相同（equals方法返回true，
那么它们的hashCode值一定要相同；(2)如果两个对象的hashCode相同，它们并不一定相同

17、是否可以继承String 类?
答：String 类是final类，不可以被继承。
补充：继承String本身就是一个错误的行为，对String类型最好的重用方式是关联（HAS-A）而不是继承（IS-A）。

18、当一个对象被当作参数传递到一个方法后，此方法可改变这个对象的属性，并可返回变化后的结果，
那么这里到底是值传递还是引用传递?

答：是值传递。Java 编程语言只有值传递参数。当一个对象实例作为一个参数被传递到方法中时，
参数的值就是对该对象的引用。对象的属性可以在被调用过程中被改变，但对象的引用是永远不会改变的。
C++和C#中可以通过传引用或传输出参数来改变传入的参数的值

补充：Java中没有传引用实在是非常的不方便，这一点在Java 8中仍然没有得到改进，
正是如此在Java编写的代码中才会出现大量的Wrapper类（将需要通过方法调用修改的引用置于一个Wrapper类中，
再将Wrapper对象传入方法），这样的做法只会让代码变得臃肿，尤其是让从C和C++转型为Java程序员的开发者无法容忍。

19、String 和StringBuilder、StringBuffer 的区别?

答：Java 平台提供了两种类型的字符串：String和StringBuffer / StringBuilder，
它们可以储存和操作字符串。其中String是只读字符串，也就意味着String引用的字符串内容是不能被改变的。
而StringBuffer和StringBuilder类表示的字符串对象可以直接进行修改
StringBuilder是JDK 1.5中引入的，它和StringBuffer的方法完全相同，区别在于它是在单线程环境下使用的
因为它的所有方面都没有被synchronized修饰，因此它的效率也比StringBuffer略高。

20、重载（Overload）和重写（Override）的区别。重载的方法能否根据返回类型进行区分?
答：方法的重载和重写都是实现多态的方式，区别在于前者实现的是编译时的多态性，而后者实现的是运行时的多态性
重载发生在一个类中，同名的方法如果有不同的参数列表（参数类型不同、参数个数不同或者二者都不同）则视为重载
重写发生在子类与父类之间，重写要求子类被重写方法与父类被重写方法有相同的返回类型，比父类被重写方法更好访问
不能比父类被重写方法声明更多的异常（里氏代换原则）。重载对返回类型没有特殊的要求。

21、描述一下JVM 加载class文件的原理机制?
答：JVM 中类的装载是由类加载器（ClassLoader） 和它的子类来实现的，
Java中的类加载器是一个重要的Java 运行时系统组件，它负责在运行时查找和装入类文件中的类。

补充：

1.由于Java的跨平台性，经过编译的Java源程序并不是一个可执行程序，而是一个或多个类文件。
当Java程序需要使用某个类时，JVM会确保这个类已经被加载、连接(验证、准备和解析)和初始化。
类的加载是指把类的.class文件中的数据读入到内存中，通常是创建一个字节数组读入.class文件，
然后产生与所加载类对应的Class对象。加载完成后，Class对象还不完整，所以此时的类还不可用。
当类被加载后就进入连接阶段，这一阶段包括验证、准备(为静态变量分配内存并设置默认的初始值)
和解析(将符号引用替换为直接引用)三个步骤。最后JVM对类进行初始化，
包括：1如果类存在直接的父类并且这个类还没有被初始化，那么就先初始化父类；2如果类中存在初始化语句，
就依次执行这些初始化语句。

2.类的加载是由类加载器完成的，类加载器包括：根加载器（BootStrap）、扩展加载器（Extension）、
系统加载器（System）和用户自定义类加载器（java.lang.ClassLoader的子类）。
从JDK 1.2开始，类加载过程采取了父亲委托机制(PDM)。PDM更好的保证了Java平台的安全性，
在该机制中，JVM自带的Bootstrap是根加载器，其他的加载器都有且仅有一个父类加载器。类的加载首先请求父类加载器加载，
父类加载器无能为力时才由其子类加载器自行加载。JVM不会向Java程序提供对Bootstrap的引用。下面是关于几个类加载器的说明：

a)Bootstrap：一般用本地代码实现，负责加载JVM基础核心类库（rt.jar）；

b)Extension：从java.ext.dirs系统属性所指定的目录中加载类库，它的父加载器是Bootstrap；

c)System：又叫应用类加载器，其父类是Extension。它是应用最广泛的类加载器。它从环境变量classpath或者系统属性java.class.path所指定的目录中记载类，
是用户自定义加载器的默认父加载器。


22、char 型变量中能不能存贮一个中文汉字?为什么?
答：char类型可以存储一个中文汉字，因为Java中使用的编码是Unicode（不选择任何特定的编码，直接使用字符在字符集中的编号，这是统一的唯一方法），一个char类型占2个字节（16bit），所以放一个中文是没问题的。

23、抽象类（abstract class）和接口（interface）有什么异同?
答：抽象类和接口都不能够实例化，但可以定义抽象类和接口类型的引用
一个类如果继承了某个抽象类或者实现了某个接口都需要对其中的抽象方法全部进行实现，否则该类仍然需要被声明为抽象类

接口(interface)比抽象类更加抽象，因为抽象类中可以定义构造器，可以有抽象方法和具体方法
而接口中不能定义构造器而且其中的方法全部都是抽象方法

抽象类中的成员可以是private、默认、protected、public的
而接口中的成员全都是public的

抽象类中可以定义成员变量
而接口中定义的成员变量实际上都是常量

有抽象方法的类必须被声明为抽象类，而抽象类未必要有抽象方法

24、静态嵌套类(Static Nested Class)和内部类（Inner Class）的不同？
Static Nested Class是被声明为静态（static）的内部类，它可以不依赖于外部类实例被实例化
而通常的内部类需要在外部类实例化后才能实例化，其语法看起来挺诡异的

25、Java 中会存在内存泄漏吗，请简单描述。
答：理论上Java因为有垃圾回收机制（GC）不会存在内存泄露问题（这也是Java被广泛使用于服务器端编程的一个重要原因）；
然而在实际开发中，可能会存在无用但可达的对象，这些对象不能被GC回收也会发生内存泄露。一个例子就是Hibernate的Session
（一级缓存）中的对象属于持久态，垃圾回收器是不会回收这些对象的，然而这些对象中可能存在无用的垃圾对象。
下面的例子也展示了Java中发生内存泄露的情况：

上面的代码实现了一个栈（先进后出（FILO））结构，乍看之下似乎没有什么明显的问题，
它甚至可以通过你编写的各种单元测试。然而其中的pop方法却存在内存泄露的问题，当我们用pop方法弹出栈中的对象时，
该对象不会被当作垃圾回收，即使使用栈的程序不再引用这些对象，因为栈内部维护着对这些对象的过期引用
（obsolete reference）。在支持垃圾回收的语言中，内存泄露是很隐蔽的，这种内存泄露其实就是无意识的对象保持。
如果一个对象引用被无意识的保留起来了，那么垃圾回收器不会处理这个对象，也不会处理该对象引用的其他对象，
即使这样的对象只有少数几个，也可能会导致很多的对象被排除在垃圾回收之外，从而对性能造成重大影响，
极端情况下会引发Disk Paging（物理内存与硬盘的虚拟内存交换数据），甚至造成OutOfMemoryError。

26、抽象的（abstract）方法是否可同时是静态的（static）,是否可同时是本地方法（native），
是否可同时被synchronized修饰?

答：都不能。抽象方法需要子类重写，而静态的方法是无法被重写的，因此二者是矛盾的
本地方法是由本地代码（如C代码）实现的方法，而抽象方法是没有实现的，也是矛盾的
synchronized和方法的实现细节有关，抽象方法不涉及实现细节，因此也是相互矛盾的。

27、静态变量和实例变量的区别？
答：静态变量是被static修饰符修饰的变量，也称为类变量，它属于类，不属于类的任何一个对象
一个类不管创建多少个对象，静态变量在内存中有且仅有一个拷贝；实例变量必须依存于某一实例，需要先创建对象然后通过对象才能访问到它
静态变量可以实现让多个对象共享内存。在Java开发中，上下文类和工具类中通常会有大量的静态成员

28、是否可以从一个静态（static）方法内部发出对非静态（non-static）方法的调用？
答：不可以，静态方法只能访问静态成员，因为非静态方法的调用要先创建对象，因此在调用静态方法时可能对象并没有被初始化。

29、如何实现对象克隆？
答：有两种方式：

1.实现Cloneable接口并重写Object类中的clone()方法；
2.实现Serializable接口，通过对象的序列化和反序列化实现克隆，可以实现真正的深度克隆，代码如下。

30、GC 是什么？为什么要有GC？

答：GC是垃圾收集的意思，内存处理是编程人员容易出现问题的地方，忘记或者错误的内存回收会导致程序或系统的不稳定甚至崩溃
Java提供的GC功能可以自动监测对象是否超过作用域从而达到自动回收内存的目的，
Java语言没有提供释放已分配内存的显示操作方法。Java程序员不用担心内存管理，因为垃圾收集器会自动进行管理
要请求垃圾收集，可以调用下面的方法之一：System.gc() 或Runtime.getRuntime().gc() ，但JVM可以屏蔽掉显示的垃圾回收调用。

垃圾回收可以有效的防止内存泄露，有效的使用可以使用的内存。垃圾回收器通常是作为一个单独的低优先级的线程运行，
不可预知的情况下对内存堆中已经死亡的或者长时间没有使用的对象进行清除和回收，
程序员不能实时的调用垃圾回收器对某个对象或所有对象进行垃圾回收。在Java诞生初期，垃圾回收是Java最大的亮点之一，
因为服务器端的编程需要有效的防止内存泄露问题，然而时过境迁，如今Java的垃圾回收机制已经成为被诟病的东西。
移动智能终端用户通常觉得iOS的系统比Android系统有更好的用户体验，其中一个深层次的原因就在于Android系统中垃圾回收的不可预知性。

补充：垃圾回收机制有很多种，包括：分代复制垃圾回收、标记垃圾回收、增量垃圾回收等方式。
标准的Java进程既有栈又有堆。栈保存了原始型局部变量，堆保存了要创建的对象。Java平台对堆内存回收和再利用的基本算法被称为标记和清除，
但是Java对其进行了改进，采用“分代式垃圾收集”。这种方法会跟Java对象的生命周期将堆内存划分为不同的区域，
在垃圾收集过程中，可能会将对象移动到不同区域：

伊甸园（Eden）：这是对象最初诞生的区域，并且对大多数对象来说，这里是它们唯一存在过的区域。
幸存者乐园（Survivor）：从伊甸园幸存下来的对象会被挪到这里。
终身颐养园（Tenured）：这是足够老的幸存对象的归宿。年轻代收集（Minor-GC）过程是不会触及这个地方的。
当年轻代收集不能把对象放进终身颐养园时，就会触发一次完全收集（Major-GC），这里可能还会牵扯到压缩，以便为大对象腾出足够的空间。

与垃圾回收相关的JVM参数:
-Xms / -Xmx --- 堆的初始大小 / 堆的最大大小
-Xmn --- 堆中年轻代的大小
-XX:-DisableExplicitGC --- 让System.gc()不产生任何作用
-XX:+PrintGCDetail --- 打印GC的细节
-XX:+PrintGCDateStamps --- 打印GC操作的时间戳

31、String s=new String(“xyz”);创建了几个字符串对象？

答：两个对象，一个是静态存储区的"xyz",一个是用new创建在堆上的对象。


32、接口是否可继承（extends）接口? 抽象类是否可实现（implements）接口? 抽象类是否可继承具体类（concrete class）?

答：接口可以继承接口。抽象类可以实现(implements)接口，抽象类可继承具体类，但前提是具体类必须有明确的构造函数。


33、一个“.java”源文件中是否可以包含多个类（不是内部类）？有什么限制？

答：可以，但一个源文件中最多只能有一个公开类（public class）而且文件名必须和公开类的类名完全保持一致。

34、Anonymous Inner Class(匿名内部类)是否可以继承其它类？是否可以实现接口？

答：可以继承其他类或实现其他接口，在Swing编程中常用此方式来实现事件监听和回调。

35、内部类可以引用它的包含类（外部类）的成员吗？有没有什么限制？

答：一个内部类对象可以访问创建它的外部类对象的成员，包括私有成员。

36、Java 中的final关键字有哪些用法？

答：(1)修饰类：表示该类不能被继承；(2)修饰方法：表示方法不能被重写；(3)修饰变量：表示变量只能一次赋值以后值不能被修改（常量）

37、指出下面程序的运行结果:
答：执行结果：1a2b2b。创建对象时构造器的调用顺序是：先初始化静态成员，然后调用父类构造器，再初始化非静态成员，最后调用自身构造器。

38、数据类型之间的转换:

1)如何将字符串转换为基本数据类型？

2)如何将基本数据类型转换为字符串？

答：

1)调用基本数据类型对应的包装类中的方法parseXXX(String)或valueOf(String)即可返回相应基本类型；

2)一种方法是将基本数据类型与空字符串（””）连接（+）即可获得其所对应的字符串；另一种方法是调用String 类中的valueOf(…)方法返回相应字符串

39、如何实现字符串的反转及替换？

答：方法很多，可以自己写实现也可以使用String或StringBuffer / StringBuilder中的方法。
有一道很常见的面试题是用递归实现字符串反转，代码如下所示：

public static String reverse(String originStr) {
		if(originStr == null || originStr.length() <= 1)
			return originStr;
		return reverse(originStr.substring(1)) + originStr.charAt(0);


40、怎样将GB2312编码的字符串转换为ISO-8859-1编码的字符串？

答：代码如下所示:

String s1 = "你好";

String s2 = newString(s1.getBytes("GB2312"), "ISO-8859-1");


41、日期和时间：

1)如何取得年月日、小时分钟秒？

2)如何取得从1970年1月1日0时0分0秒到现在的毫秒数？

3)如何取得某月的最后一天？

4)如何格式化日期？

答：操作方法如下所示：

1)创建java.util.Calendar 实例，调用其get()方法传入不同的参数即可获得参数所对应的值

2)以下方法均可获得该毫秒数:

43、比较一下Java 和JavaSciprt。

答：JavaScript 与Java是两个公司开发的不同的两个产品。Java 是原Sun 公司推出的面向对象的程序设计语言，
特别适合于互联网应用程序开发；而JavaScript是Netscape公司的产品，
为了扩展Netscape浏览器的功能而开发的一种可以嵌入Web页面中运行的基于对象和事件驱动的解释性语言，
它的前身是LiveScript；而Java 的前身是Oak语言。

下面对两种语言间的异同作如下比较：

1）基于对象和面向对象：Java是一种真正的面向对象的语言，即使是开发简单的程序，必须设计对象；
JavaScript是种脚本语言，它可以用来制作与网络无关的，与用户交互作用的复杂软件。
它是一种基于对象（Object-Based）和事件驱动（Event-Driven）的编程语言。
因而它本身提供了非常丰富的内部对象供设计人员使用；

2）解释和编译：Java 的源代码在执行之前，必须经过编译；JavaScript 是一种解释性编程语言，
其源代码不需经过编译，由浏览器解释执行；

3）强类型变量和类型弱变量：Java采用强类型变量检查，即所有变量在编译之前必须作声明；
JavaScript中变量声明，采用其弱类型。即变量在使用前不需作声明，而是解释器在运行时检查其数据类型；

4）代码格式不一样。

补充：上面列出的四点是原来所谓的标准答案中给出的。其实Java和JavaScript最重要的区别是一个是静态语言，
一个是动态语言。目前的编程语言的发展趋势是函数式语言和动态语言。在Java中类（class）是一等公民，
而JavaScript中函数（function）是一等公民。对于这种问题，在面试时还是用自己的语言回答会更加靠谱

45、Error 和Exception 有什么区别?

答：Error 表示系统级的错误和程序不必处理的异常，是恢复不是不可能但很困难的情况下的一种严重问题；比如内存溢出，不可能指望程序能处理这样的情况
Exception 表示需要捕捉或者需要程序进行处理的异常，是一种设计或实现问题；也就是说，它表示如果程序运行正常，从不会发生的情况

46、try{}里有一个return语句，那么紧跟在这个try后的finally{}里的code会不会被执行，什么时候被执行，在return前还是后?

答：会执行，在方法返回调用者前执行。Java允许在finally中改变返回值的做法是不好的，因为如果存在finally代码块
try中的return语句不会立马返回调用者，而是记录下返回值待finally代码块执行完毕之后再向调用者返回其值
然后如果在finally中修改了返回值，这会对程序造成很大的困扰，C#中就从语法上规定不能做这样的事。

47、Java 语言如何进行异常处理，关键字：throws、throw、try、catch、finally分别如何使用？

在Java 中，每个异常都是一个对象，它是Throwable 类或其子类的实例。当一个方法出现异常后便抛出一个异常对象，该对象中包含有异常信息，调用这个对象的方法可以捕获到这个异常并进行处理
Java 的异常处理是通过5 个关键词来实现的：try、catch、throw、throws和finally
一般情况下是用try来执行一段程序，如果出现异常，系统会抛出（throw）一个异常，这时候你可以通过它的类型来捕捉（catch）它，或最后（finally）由缺省处理器来处理
try用来指定一块预防所有“异常”的程序；catch 子句紧跟在try块后面，用来指定你想要捕捉的“异常”的类型
throw 语句用来明确地抛出一个“异常”；throws用来标明一个成员函数可能抛出的各种“异常”
finally 为确保一段代码不管发生什么“异常”都被执行一段代码, 可以在一个成员函数调用的外面写一个try语句，在这个成员函数内部写另一个try语句保护其他代码
每当遇到一个try 语句，“异常”的框架就放到栈上面，直到所有的try语句都完成。如果下一级的try语句没有对某种“异常”进行处理，栈就会展开，直到遇到有处理这种“异常”的try 语


49、列出一些你常见的运行时异常？

答：

ArithmeticException（算术异常）

ClassCastException （类转换异常）

IllegalArgumentException （非法参数异常）

IndexOutOfBoundsException （下表越界异常）

NullPointerException （空指针异常）

SecurityException （安全异常）

50、final, finally, finalize 的区别?

答：final：修饰符（关键字）有三种用法：如果一个类被声明为final，意味着它不能再派生出新的子类，即不能被继承，因此它和abstract是反义词
将变量声明为final，可以保证它们在使用中不被改变，被声明为final 的变量必须在声明时给定初值，而在以后的引用中只能读取不可修改。被声明为final 的方法也同样只能使用，不能在子类中被重写
finally：通常放在try…catch的后面构造总是执行代码块，这就意味着程序无论正常执行还是发生异常，这里的代码只要JVM不关闭都能执行，可以将释放外部资源的代码写在finally块中
finalize：Object类中定义的方法，Java中允许使用finalize() 方法在垃圾收集器将对象从内存中清除出去之前做必要的清理工作
这个方法是由垃圾收集器在销毁对象时调用的，通过重写finalize() 方法可以整理系统资源或者执行其他清理工作

----------------------------------------------------------------------------------------------------------------
23、String s = new String(“xyz”);创建了几个字符串对象？

答：两个对象，一个是静态区的”xyz”，一个是用new创建在堆上的对象

24、接口是否可继承（extends）接口？抽象类是否可实现（implements）接口？抽象类是否可继承具体类（concrete class）？

答：接口可以继承接口，而且支持多重继承。抽象类可以实现(implements)接口，抽象类可继承具体类也可以继承抽象类。

25、Java 中的final关键字有哪些用法？
答：(1)修饰类：表示该类不能被继承；(2)修饰方法：表示方法不能被重写；(3)修饰变量：表示变量只能一次赋值以后值不能被修改（常量）。

26、指出下面程序的运行结果。


class A {

    static {
        System.out.print("1");
    }

    public A() {
        System.out.print("2");
    }
}

class B extends A{

    static {
        System.out.print("a");
    }

    public B() {
        System.out.print("b");
    }
}

public class Hello {

    public static void main(String[] args) {
        A ab = new B();
        ab = new B();
    }

}
答：执行结果：1a2b2b。创建对象时构造器的调用顺序是：先初始化静态成员，然后调用父类构造器，再初始化非静态成员，最后调用自身构造器。
try {
    throw new Annoyance();
} catch (Sneeze s) {
    System.out.println("Caught Sneeze");
    return;
} finally {
    System.out.println("Hello World!");
}

try {
    throw new Annoyance();
} catch (Sneeze s) {
    System.out.println("Caught Sneeze");
    return;
} catch (Exception e) {
    System.out.println("Caught Exception");
    return;
} finally {
    System.out.println("Hello World!");
}

35、List、Set、Map是否继承自Collection接口？
答：List、Set 是，Map 不是。Map是键值对映射容器，与List和Set有明显的区别
而Set存储的零散的元素且不允许有重复元素（数学中的集合也是如此），List是线性结构的容器，适用于按数值索引访问元素的情形

36、Collection和Collections的区别？
答：Collection是一个接口，它是Set、List等容器的父接口
Collections是个一个工具类，提供了一系列的静态方法来辅助容器操作，这些方法包括对容器的搜索、排序、线程安全化等等

37、List、Map、Set三个接口存取元素时，各有什么特点？
答：List以特定索引来存取元素，可以有重复元素。Set不能存放重复元素（用对象的equals()方法来区分元素是否重复）。Map保存键值对（key-value pair）映射，映射关系可以是一对一或多对一

38、Thread类的sleep()方法和对象的wait()方法都可以让线程暂停执行，它们有什么区别?
答：sleep()方法（休眠）是线程类（Thread）的静态方法，调用此方法会让当前线程暂停执行指定的时间，将执行机会（CPU）让给其他线程，但是对象的锁依然保持，因此休眠时间结束后会自动恢复
wait()是Object类的方法，调用对象的wait()方法导致当前线程放弃对象的锁（线程暂停执行），进入对象的等待池（wait pool），
只有调用对象的notify()方法（或notifyAll()方法）时才能唤醒等待池中的线程进入等锁池（lock pool），如果线程重新获得对象的锁就可以进入就绪状态。

39、线程的sleep()方法和yield()方法有什么区别？
① sleep()方法给其他线程运行机会时不考虑线程的优先级，因此会给低优先级的线程以运行的机会；
   yield()方法只会给相同优先级或更高优先级的线程以运行的机会；

② 线程执行sleep()方法后转入阻塞（blocked）状态，而执行yield()方法后转入就绪（ready）状态；

③ sleep()方法声明抛出InterruptedException，而yield()方法没有声明任何异常；

④ sleep()方法比yield()方法（跟操作系统CPU调度相关）具有更好的可移植性。

40、当一个线程进入一个对象的synchronized方法A之后，其它线程是否可进入此对象的synchronized方法B？
答：不能。其它线程只能访问该对象的非同步方法，同步方法则不能进入
因为非静态方法上的synchronized修饰符要求执行方法时要获得对象的锁，如果已经进入A方法说明对象锁已经被取走
那么试图进入B方法的线程就只能在等锁池（注意不是等待池哦）中等待对象的锁。

41、请说出与线程同步以及线程调度相关的方法。
- wait()：使一个线程处于等待（阻塞）状态，并且释放所持有的对象的锁；
- sleep()：使一个正在运行的线程处于睡眠状态，是一个静态方法，调用此方法要处理InterruptedException异常；
- notify()：唤醒一个处于等待状态的线程，当然在调用此方法的时候，并不能确切的唤醒某一个等待状态的线程，而是由JVM确定唤醒哪个线程，而且与优先级无关；
- notityAll()：唤醒所有处于等待状态的线程，该方法并不是将对象的锁给所有线程，而是让它们竞争，只有获得锁的线程才能进入就绪状态；

42、编写多线程程序有几种实现方式？
答：一种是继承Thread类；另一种是实现Runnable接口。两种方式都要通过重写run()方法来定义线程的行为，推荐使用后者
因为Java中的继承是单继承，一个类有一个父类，如果继承了Thread类就无法再继承其他类了，显然使用Runnable接口更为灵活

43、synchronized关键字的用法？
答：synchronized关键字可以将对象或者方法标记为同步，以实现对对象和方法的互斥访问，可以用synchronized(对象)
 { … }定义同步代码块，或者在声明方法时将synchronized作为方法的修饰符。

44、举例说明同步和异步。
答：如果系统中存在临界资源（资源数量少于竞争资源的线程数量的资源），例如正在写的数据以后可能被另一个线程读到，
或者正在读的数据可能已经被另一个线程写过了，那么这些数据就必须进行同步存取（数据库操作中的排他锁就是最好的例子）
当应用程序在对象上调用了一个需要花费很长时间来执行的方法，并且不希望让程序等待方法的返回时，就应该使用异步编程，
在很多情况下采用异步途径往往更有效率。事实上，所谓的同步就是指阻塞式操作，而异步就是非阻塞式操作。

45、简述synchronized 和java.util.concurrent.locks.Lock的异同？
答：Lock是Java 5以后引入的新的API，和关键字synchronized相比主要相同点：Lock 能完成synchronized所实现的所有功能；
主要不同点：Lock有比synchronized更精确的线程语义和更好的性能，而且不强制性的要求一定要获得锁
synchronized会自动释放锁，而Lock一定要求程序员手工释放，并且最好在finally 块中释放（这是释放外部资源的最好的地方）

46、事务的ACID是指什么？
答：
- 原子性(Atomic)：事务中各项操作，要么全做要么全不做，任何一项操作的失败都会导致整个事务的失败；
- 一致性(Consistent)：事务结束后系统状态是一致的；
- 隔离性(Isolated)：并发执行的事务彼此无法看到对方的中间状态；
- 持久性(Durable)：事务完成后所做的改动都会被持久化，即使发生灾难性的失败。通过日志和同步备份可以在故障发生后重建数据。

47、获得一个类的类对象有哪些方式？
答：
- 方法1：类型.class，例如：String.class
- 方法2：对象.getClass()，例如：”hello”.getClass()
- 方法3：Class.forName()，例如：Class.forName(“java.lang.String”)

48、简述一下面向对象的”六原则一法则”。


48、简述一下面向对象的”六原则一法则”。
答：

- 单一职责原则：一个类只做它该做的事情。（单一职责原则想表达的就是”高内聚”，写代码最终极的原则只有六个字”高内聚、低耦合”，就如同葵花宝典或辟邪剑谱的中心思想就八个字”欲练此功必先自宫”，所谓的高内聚就是一个代码模块只完成一项功能，
在面向对象中，如果只让一个类完成它该做的事，而不涉及与它无关的领域就是践行了高内聚的原则，这个类就只有单一职责。我们都知道一句话叫”因为专注，所以专业”，
一个对象如果承担太多的职责，那么注定它什么都做不好。这个世界上任何好的东西都有两个特征，一个是功能单一，
好的相机绝对不是电视购物里面卖的那种一个机器有一百多种功能的，它基本上只能照相；
另一个是模块化，好的自行车是组装车，从减震叉、刹车到变速器，所有的部件都是可以拆卸和重新组装的，
好的乒乓球拍也不是成品拍，一定是底板和胶皮可以拆分和自行组装的，一个好的软件系统，
它里面的每个功能模块也应该是可以轻易的拿到其他系统中使用的，这样才能实现软件复用的目标。）

- 开闭原则：软件实体应当对扩展开放，对修改关闭。（在理想的状态下，当我们需要为一个软件系统增加新功能时，
只需要从原来的系统派生出一些新类就可以，不需要修改原来的任何一行代码。要做到开闭有两个要点：
①抽象是关键，一个系统中如果没有抽象类或接口系统就没有扩展点；
②封装可变性，将系统中的各种可变因素封装到一个继承结构中，如果多个可变因素混杂在一起，系统将变得复杂

- 依赖倒转原则：面向接口编程。

- 里氏替换原则：任何时候都可以用子类型替换掉父类型。（关于里氏替换原则的描述，Barbara Liskov女士的描述比这个要复杂得多，
但简单的说就是能用父类型的地方就一定能使用子类型。里氏替换原则可以检查继承关系是否合理，如果一个继承关系违背了里氏替换原则，
那么这个继承关系一定是错误的，需要对代码进行重构。例如让猫继承狗，或者狗继承猫，又或者让正方形继承长方形都是错误的继承关系，
因为你很容易找到违反里氏替换原则的场景。需要注意的是：子类一定是增加父类的能力而不是减少父类的能力，因为子类比父类的能力更多，
把能力多的对象当成能力少的对象来用当然没有任何问题。）

- 接口隔离原则：接口要小而专，绝不能大而全。（臃肿的接口是对接口的污染，既然接口表示能力，那么一个接口只应该描述一种能力，
接口也应该是高度内聚的。例如，琴棋书画就应该分别设计为四个接口，而不应设计成一个接口中的四个方法，
因为如果设计成一个接口中的四个方法，那么这个接口很难用，毕竟琴棋书画四样都精通的人还是少数，而如果设计成四个接口，
会几项就实现几个接口，这样的话每个接口被复用的可能性是很高的。Java中的接口代表能力、代表约定、代表角色，
能否正确的使用接口一定是编程水平高低的重要标识。）

- 合成聚合复用原则：优先使用聚合或合成关系复用代码。

- 迪米特法则：迪米特法则又叫最少知识原则，一个对象应当对其他对象有尽可能少的了解。（迪米特法则简单的说就是如何做到”低耦合”，
门面模式和调停者模式就是对迪米特法则的践行。对于门面模式可以举一个简单的例子，你去一家公司洽谈业务，你不需要了解这个公司内部是如何运作的，
你甚至可以对这个公司一无所知，去的时候只需要找到公司入口处的前台美女，告诉她们你要做什么，她们会找到合适的人跟你接洽，
前台的美女就是公司这个系统的门面。再复杂的系统都可以为用户提供一个简单的门面，Java Web开发中作为前端控制器的Servlet或Filter不就是一个门面吗，
浏览器对服务器的运作方式一无所知，但是通过前端控制器就能够根据你的请求得到相应的服务。调停者模式也可以举一个简单的例子来说明，
例如一台计算机，CPU、内存、硬盘、显卡、声卡各种设备需要相互配合才能很好的工作，但是如果这些东西都直接连接到一起，
计算机的布线将异常复杂，在这种情况下，主板作为一个调停者的身份出现，它将各个设备连接在一起而不需要每个设备之间直接交换数据，
这样就减小了系统的耦合度和复杂度，如下图所示。迪米特法则用通俗的话来将就是不要和陌生人打交道，
如果真的需要，找一个自己的朋友，让他替你和陌生人打交道。）

52、Servlet的运行过程？
Web容器加载Servlet并将其实例化后，Servlet生命周期开始，容器运行其init()方法进行Servlet的初始化；
请求到达时调用Servlet的service()方法，service()方法会根据需要调用与请求对应的doGet或doPost等方法；
当服务器关闭或项目被卸载时服务器会将Servlet实例销毁，此时会调用Servlet的destroy()方法。

53、转发（forward）和重定向（redirect）的区别？
答：forward是容器中控制权的转向，是服务器请求资源，服务器直接访问目标地址的URL，把那个URL 的响应内容读取过来，
然后把这些内容再发给浏览器，浏览器根本不知道服务器发送的内容是从哪儿来的，所以它的地址栏中还是原来的地址。

redirect就是服务器端根据逻辑，发送一个状态码，告诉浏览器重新去请求那个地址，因此从浏览器的地址栏中可以看到跳转后的链接地址，
很明显redirect无法访问到服务器保护起来资源，但是可以从一个网站redirect到其他网站。

forward更加高效，所以在满足需要时尽量使用forward（通过调用RequestDispatcher对象的forward()方法，该对象可以通过ServletRequest对象的getRequestDispatcher()方法获得），
并且这样也有助于隐藏实际的链接；在有些情况下，比如需要访问一个其它服务器上的资源，则必须使用重定向（通过HttpServletResponse对象调用其sendRedirect()方法实现）。

54、JSP有哪些内置对象？作用分别是什么？
答：JSP有9个内置对象：
- request：封装客户端的请求，其中包含来自GET或POST请求的参数；
- response：封装服务器对客户端的响应；
- pageContext：通过该对象可以获取其他对象；
- session：封装用户会话的对象；
- application：封装服务器运行环境的对象；
- out：输出服务器响应的输出流对象；
- config：Web应用的配置对象；
- page：JSP页面本身（相当于Java程序中的this）；
- exception：封装页面抛出异常的对象。

55、讲解JSP中的四种作用域。
答：JSP中的四种作用域包括page、request、session和application，具体来说：
- page代表与一个页面相关的对象和属性。
- request代表与Web客户机发出的一个请求相关的对象和属性。一个请求可能跨越多个页面，涉及多个Web组件；需要在页面显示的临时数据可以置于此作用域。
- session代表与某个用户与服务器建立的一次会话相关的对象和属性。跟某个用户相关的数据应该放在用户自己的session中。

- application代表与整个Web应用程序相关的对象和属性，它实质上是跨越整个Web应用程序，包括多个页面、请求和会话的一个全局作用域。

https://blog.csdn.net/chao_ji_cai/article/details/98937250

Java框架
1. Spring的核心特性是什么？Spring优点？
2. spring框架中需要引用哪些jar包，以及这些jar包的用途
3. 理解AOP、IoC的基本原理；
4. AOP的一些场景应用；
5. spring注入的几种方式
6. Spring容器的加载顺序？
7. spring如何实现事务管理的
8. Spring中Bean的作用域有哪些
9. 请介绍一下bean的生命周期
10. Spring中自动装配的方式有哪些
11. @Resource 和 @Autowired 区别？分别用在什么场景？
12. 静态代理和动态代理的区别？
13. Hibernate和mybatis的区别？
14. mybatis是如何工作的？
15. Hibernate对象有几个状态值？
16. 对ajax的理解
17. session和cookie的区别和联系，session的生命周期，多个服务部署时session管理
18. 简述Springmvc的流程；
19. spring中beanFactory和ApplicationContext的联系和区别
20. Springmvc和Springboot有什么区别？
21. Springboot为什么配置简单？（即它自动做了什么操作才能简化程序员的操作）
22. 持久层设计要考虑的问题有哪些？请谈一下你用过的持久层框架都有哪些？

专业理论知识
计算机网络
TCP三次握手过程、参数；
TCP四次挥手过程、参数；
TCP和UDP的区别？应用场景有何不同？
TCP阻塞控制；
OSI七层模型、各层所用到的协议；
一些常见协议的原理：ARP、ICMP、FTP等（TCP UDP更不用说啦，一定要了解）

数据库
数据库有哪些索引？原理是什么？
索引有什么作用？有什么特点（索引的优缺点，什么字段上建立索引）
索引为什么用B+树？
B+树和B-树有什么区别？
mysql中MyISAM和InnoDB的区别？
事务的四大特性（常考）
数据库隔离级别及各自能解决的问题
数据库优化的一些策略；
增删改查要熟悉，随时可能提一个需求让你写一个SQL语句；
数据库索引：聚集索引和非聚集索引的区别？
数据库的视图和索引都有什么特点，有什么区别？
高并发处理的理解
数据库连接池作用

Linux
https://www.cnblogs.com/passzhang/p/8552757.html
问题一：

绝对路径用什么符号表示？当前目录、上层目录用什么表示？主目录用什么表示? 切换目录用什么命令？

答案：
绝对路径： 如/etc/init.d
当前目录和上层目录： ./  ../
主目录： ~/
切换目录： cd




Java基础（题目太多了，Java程序员面试宝典基础部分总结的蛮好的）
面向对象的特性？（封装继承多态）如何体现出来？
重载和重写有什么区别？
集合类有哪些？（常考）
Set和List、Map的区别；
ArrayList、Linkedlist、Vector区别？（常考，建议看下底层实现代码）
ArrayList如何扩容？（常考）
Map下Hashmap、TreeMap的区别？
TreeMap底层是什么？红黑树还是二叉树？
Map、List下哪些类是线程安全的？（常考）
Hashmap的扩容机制；
Hashmap如何解决哈希冲突？与HashTable有何不同？
正则表达式；（服务端岗位常考）
接口跟抽象类的区别？
Java可以多继承吗？
JVM垃圾回收机制；（常考）
Java中是值传递还是引用传递？
Java中锁机制；
Lock的底层怎么实现的？源码怎么写的？
sychronized的底层实现？
sychronized修饰静态方法和修饰普通方法有什么区别？
异常类有哪些实现类、子类？
多线程中如何保证线程安全？
多线程有哪些常见的线程安全的类？
如何开启一个线程？
get请求和post请求有什么区别？
反射的原理？
ClassLoader和Class.forName()这两个有什么区别？（反射源码的考察）
NIO这一块有什么了解？
谈谈堆和栈的区别
谈谈你所了解的设计模式，并简单描述其特点和用法，或简单写一个某某设计模式！
HTTP基本的状态码
监听器、过滤器、拦截器、servlet的区别
web.xml 的加载顺序是：context- param -> listener -> filter -> servlet
监听器（listener）：
在request、session、application三个对象创建消亡或者往其中增/删/改属性时自动执行指定代码的功能组件。
生命周期：随web应用的启动而启动，只初始化一次，随web应用的停止而销毁。
作用：做一些初始化的内容添加工作、设置一些基本的内容、比如一些参数或者是一些固定的对象等等。
过滤器（filter）：
拦截请求，filter能够在一个请求到达控制层之前预处理用户请求，也可以在离开控制层时处理http 响应,进行一些设置以及逻辑判断,然后再传入servlet或者struts的 action进行业务逻辑，基于函数回调。
生命周期：它是随你的web应用启动而启动的，只初始化一次，以后就可以拦截相关请求，只有当你的web应用停止或重新部署的时候才销毁。
作用：a.对请求或响应(Request、Response)统一设置统一编码，简化操作；b.进行逻辑判断，如用户是否已经登陆、有没有权限访问该页面等等工作。c.过滤掉非法url
拦截器（interceptor）：
拦截器是在面向切面编程中应用的，基于JAVA的反射机制，在一个业务逻辑（某个方法) 前、后调用另一个方法。
servlet：
servlet是一种运行服务器端的java应用程序，具有独立于平台和协议的特性，并且可以动态的生成web页面，它工作在客户端请求与服务器响应的中间层。
当在浏览器输入一个网址，所要经过的全部在过程，请详细描述
类加载的过程？类加载器有哪些？为什么使用双亲委派模式
接口和抽象类的区别是什么？
什么是值传递和引用传递？
Java的内存模型以及GC算法
Java堆的结构是什么样子的？什么是堆中的永久代(Perm Gen space)?
串行(serial)收集器和吞吐量(throughput)收集器的区别是什么？
在Java中，对象什么时候可以被垃圾回收？
JVM的永久代中会发生垃圾回收么？
Serial 与 Parallel GC之间的不同之处？
Java 中 WeakReference 与 SoftReference的区别？
动态代理的两种方式，以及区别
.Java内存泄露的问题调查定位
什么是迭代器(Iterator)？Iterator和ListIterator的区别是什么？
快速失败(fail-fast)和安全失败(fail-safe)的区别是什么？

https://blog.csdn.net/chao_ji_cai/article/details/98960419
Java框架
1. Spring的核心特性是什么？Spring优点？
Spring的核心是控制反转（IoC）和面向切面（AOP）
Spring优点：
（1）方便解耦，简化开发 （高内聚低耦合）
Spring就是一个大工厂（容器），可以将所有对象创建和依赖关系维护，交给Spring管理
spring工厂是用于生成bean

（2）AOP编程的支持
Spring提供面向切面编程，可以方便的实现对程序进行权限拦截、运行监控等功能

（3） 声明式事务的支持
只需要通过配置就可以完成对事务的管理，而无需手动编程

（4） 方便程序的测试
Spring对Junit4支持，可以通过注解方便的测试Spring程序

（5）方便集成各种优秀框架
Spring不排斥各种优秀的开源框架，其内部提供了对各种优秀框架（如：Struts、Hibernate、MyBatis、Quartz等）的直接支持

（6） 降低JavaEE API的使用难度
Spring 对JavaEE开发中非常难用的一些API（JDBC、JavaMail、远程调用等），都提供了封装，使这些API应用难度大大降低

2. spring框架中需要引用哪些jar包，以及这些jar包的用途
4 + 1 ： 4个核心（beans、core、context、expression） + 1个依赖（commons-loggins…jar）

3. 理解AOP、IoC的基本原理；
IOC：控制反转（IoC）与依赖注入（DI）是同一个概念，
控制反转的思想：
传统的 java 开发模式中，当需要一个对象时，我们会自己使用 new 或者 getInstance 等直接或者间接调用构造方法创建一个对象。
而在 spring 开发模式中，spring 容器使用了工厂模式为我们创建了所需要的对象，不需要我们自己创建了，
直接调用 spring 提供的对象就可以了

引入IOC的目的：
（1）脱开、降低类之间的耦合；（2）倡导面向接口编程、实施依赖倒换原则；
（3）提高系统可插入、可测试、可修改等特性

AOP：面向切面编程（AOP）
面向切面编程思想：
在面向对象编程（oop）思想中，我们将事物纵向抽成一个个的对象。而在面向切面编程中，
我们将一个个的对象某些类似的方面横向抽成一个切面，对这个切面进行一些如权限控制、事物管理，记录日志等公用操作处理的过程。
切面：简单说就是那些与业务无关，却为业务模块所共同调用的逻辑或责任封装起来，便于减少系统的重复代码，
降低模块之间的耦合度，并有利于未来的可操作性和可维护性。
AOP 底层：动态代理。
如果是接口采用 JDK 动态代理，如果是类采用CGLIB 方式实现动态代理。

4. AOP的一些场景应用；
AOP用来封装横切关注点，具体可以在下面的场景中使用:

Authentication 权限
Caching 缓存
Context passing 内容传递
Error handling 错误处理
Lazy loading　懒加载
Debugging　　调试
logging, tracing, profiling and monitoring　记录跟踪　优化　校准
Performance optimization　性能优化
Persistence　　持久化
Resource pooling　资源池
Synchronization　同步
Transactions 事务


5. spring注入的几种方式

（1）构造方法注入
（2）setter注入
（3）基于注解
6. Spring容器的加载顺序？
7. spring如何实现事务管理的
8. Spring中Bean的作用域有哪些

作用域：用于确定spring创建bean实例个数
取值（常用的两个）：
singleton 单例，默认值。
prototype 多例，一个 bean 的定义可以有多个实例。每执行一次getBean将获得一个实例。
9. 请介绍一下bean的生命周期
（1）bean 定义：在配置文件里面用来进行定义。
（2）bean 初始化：有两种方式初始化:
在配置文件中通过指定 init-method 属性来完成
实现 org.springframwork.beans.factory.InitializingBean 接口
（3）bean 调用：有三种方式可以得到 bean 实例，并进行调用
（4）bean 销毁：销毁有两种方式
使用配置文件指定的 destroy-method 属性
实现 org.springframwork.bean.factory.DisposeableBean 接口

10. Spring中自动装配的方式有哪些

no：不进行自动装配，手动设置Bean的依赖关系。
byName：根据Bean的名字进行自动装配。
byType：根据Bean的类型进行自动装配。
constructor：类似于byType，不过是应用于构造器的参数，如果正好有一个Bean与构造器的参数类型相同则可以自动装配，否则会导致错误。
autodetect：如果有默认的构造器，则通过constructor的方式进行自动装配，否则使用byType的方式进行自动装配。
（自动装配没有自定义装配方式那么精确，而且不能自动装配简单属性（基本类型、字符串等），在使用时应注意。）

11. @Resource 和 @Autowired 区别？分别用在什么场景？
（1）共同点：两者都可以写在字段和setter方法上。两者如果都写在字段上，那么就不需要再写setter方法。
（2）不同点：
@Autowired
@Autowired为Spring提供的注解，需要导入包org.springframework.beans.factory.annotation.Autowired;只按照byType注入。
@Autowired注解是按照类型（byType）装配依赖对象，默认情况下它要求依赖对象必须存在，如果允许null值，可以设置它的required属性为false。
如果我们想使用按照名称（byName）来装配，可以结合@Qualifier注解一起使用。
@Resource
@Resource默认按照ByName自动注入，由J2EE提供，需要导入包javax.annotation.Resource。
@Resource有两个重要的属性：name和type，而Spring将@Resource注解的name属性解析为bean的名字，
而type属性则解析为bean的类型。所以，如果使用name属性，则使用byName的自动注入策略，
而使用type属性时则使用byType自动注入策略。如果既不制定name也不制定type属性，这时将通过反射机制使用byName自动注入策略。

12. 静态代理和动态代理的区别？

13. Hibernate和mybatis的区别？
（1）两者最大的区别
　　针对简单逻辑，Hibernate与MyBatis都有相应的代码生成工具，可以生成简单基本的DAO层方法。
　　针对高级查询，MyBatis需要手动编写SQL语句，以及ResultMap，而Hibernate有良好的映射机制，
   开发者无需关心SQL的生成与结果映射，可以更专注于流程。
（2）开发难度对比
　　Hibernate的开发难度大于MyBatis，主要由于Hibernate比较复杂，庞大，学习周期比较长。
　　MyBatis则相对简单，并且MyBatis主要依赖于生气了的书写，让开发者刚进更熟悉。
（3）sql书写比较
　　Hibernate也可以自己写sql来指定需要查询的字段，但这样就破坏了Hibernate开发的简洁性，不过Hibernate具有自己的日志统计。
　　MyBatis的sql是手动编写的，所以可以按照要求指定查询的字段，不过没有自己的日志统计，所以要借助Log4j来记录日志。
（4）数据库扩展性计较
　　Hibernate与数据库具体的关联在XML中，所以HQL对具体是用什么数据库并不是很关心
　　MyBatis由于所有sql都是依赖数据库书写的，所以扩展性、迁移性比较差。
（5）缓存机制比较
　　Hibernate的二级缓存配置在SessionFactory生成配置文件中进行详细配置，然后再在具体的表对象映射中配置那种缓存。
　　MyBatis的二级缓存配置都是在每个具体的表对象映射中进行详细配置，这样针对不同的表可以自定义不同的缓冲机制，
并且MyBatis可以在命名空间中共享相同的缓存配置和实例，通过Cache-ref来实现。

https://blog.csdn.net/u014745069/article/details/80788127

15. Hibernate对象有几个状态值？
Transient 瞬时 ：对象刚new出来，还没设id，设了其他值。
Persistent 持久：调用了save()、saveOrUpdate()，就变成Persistent，有id
Detached 脱管 ： 当session close()完之后，变成Detached。

16. 对ajax的理解
17. session和cookie的区别和联系，session的生命周期，多个服务部署时session管理

18. 简述Springmvc的流程；
参考博客 https://blog.csdn.net/qinqigang/article/details/78540543

19. spring中beanFactory和ApplicationContext的联系和区别

20. Springmvc和Springboot有什么区别？
Spring MVC 是基于Spring的一个 MVC 框架 ；
Spring Boot 是基于Spring4的条件注册的一套快速开发整合包。

21. Springboot为什么配置简单？（即它自动做了什么操作才能简化程序员的操作）
主要是使用了spring3之后提供的注解，来代替xml文件的配置，最核心的是以下两个注解
@Configuration，标注在类上，相当于定义一个配置类，一份spring的配置文件
@Bean，类似于spring配置文件中的
通过这两个注解就可以用java代码的方式来完成相关spring配置

22. 持久层设计要考虑的问题有哪些？请谈一下你用过的持久层框架都有哪些？
"持久"就是将数据保存到可掉电式存储设备中以便今后使用，简单的说，就是将内存中的数据保存到关系型数据库、文件系统、消息队列等提供持久化支持的设备中。持久层就是系统中专注于实现数据持久化的相对独立的层面。

持久层设计的目标包括：

数据存储逻辑的分离，提供抽象化的数据访问接口。
数据访问底层实现的分离，可以在不修改代码的情况下切换底层实现。
资源管理和调度的分离，在数据访问层实现统一的资源调度（如缓存机制）。
数据抽象，提供更面向对象的数据操作。
持久层框架有： Hibernate、MyBatis、TopLink、 Guzz、 jOOQ、 Spring Data、ActiveJDBC

spring工作的流程
https://blog.csdn.net/qinqigang/article/details/78540543

1. 用户发起请求到前端控制器（DispatcherServlet），该控制器会过滤出哪些请求可以访问Servlet、哪些不能访问。就是url-pattern的作用，并且会加载springmvc.xml配置文件。
1. 前端控制器会找到处理器映射器（HandlerMapping），通过HandlerMapping完成url到controller映射的组件，
   简单来说，就是将在springmvc.xml中配置的或者注解的url与对应的处理类找到并进行存储，用map<url,handler>这样的方式来存储。
1. HandlerMapping有了映射关系，并且找到url对应的处理器，HandlerMapping就会将其处理器（Handler）返回，在返回前，会加上很多拦截器。
1. DispatcherServlet拿到Handler后，找到HandlerAdapter（处理器适配器），通过它来访问处理器，并执行处理器。
1. 执行处理器
1. 处理器会返回一个ModelAndView对象给HandlerAdapter
1. 通过HandlerAdapter将ModelAndView对象返回给前端控制器(DispatcherServlet)
1. 前端控制器请求视图解析器(ViewResolver)去进行视图解析，根据逻辑视图名解析成真正的视图(jsp)，
   其实就是将ModelAndView对象中存放视图的名称进行查找，找到对应的页面形成视图对象
1. 返回视图对象到前端控制器。
1. 视图渲染，就是将ModelAndView对象中的数据放到request域中，用来让页面加载数据的。
1. 通过第8步，通过名称找到了对应的页面，通过第10步，request域中有了所需要的数据，那么就能够进行视图渲染了。最后将其返回即可。



































"""









