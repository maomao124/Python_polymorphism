"""
 * Project name(项目名称)：Python多态
 * Package(包名): 
 * File(文件名): test1
 * Author(作者）: mao
 * Author QQ：1296193245
 * GitHub：https://github.com/maomao124/
 * Date(创建日期)： 2022/3/27 
 * Time(创建时间)： 21:02
 * Version(版本): 1.0
 * Description(描述)：
 类的多态特性，满足以下 2 个前提条件：
继承：多态一定是发生在子类和父类之间；
重写：子类重写了父类的方法。
 """


class A:
    def say(self, who):
        who.say()


class B:
    def say(self):
        print("调用的是 B 类的say方法")


class C(B):
    def say(self):
        print("调用的是 C 类的say方法")


class D(B):
    def say(self):
        print("调用的是 D 类的say方法")


if __name__ == '__main__':
    a = A()
    a.say(B())
    a.say(C())
    a.say(D())
