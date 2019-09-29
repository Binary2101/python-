#Kali Linux系统的安装以及局域网内渗透的实现中遇到的困难以及解决办法
##安装Kali
在将Kali安装到U盘中时，可谓是踩了无数的坑。  
先是使用MiniTool Partition Wizard软件将U盘清空并分区，再用win32diskimager将镜像文件写入U盘，这个软件中有个校验的功能，我尝试使用了一下，结果它给出的sha256哈希值与官网中给出的镜像哈希值不同，但我也没在意。最后进入电脑bios更改启动方式。最后成功进入Kali系统，在终端输入gparted更改U盘分区，却发现U盘只有unallocated无法进行分区操作，心生疑惑。回到Windows系统中，重新进入MiniTool Partition Wizard软件查看U盘分区，发现在用镜像写入工具后，对U盘的分区产生影响，于是更改方法。  
换用镜像写入工具universal-usb-installer,进行一番操作后，发现usb启动后直接进入黑色grub界面，引导好像出了什么问题。于是再换用方法。  
此时我想起之前sha256校验值不匹配的问题，怀疑是镜像文件损坏，于是重新在官网下载了一遍，还是不同，心生疑惑的我上网查询windows下查看文件哈希值的方法，在命令行中使用命令'certuil -hashfile yourfilename sha256'来测出的哈希值和官网一样。用现成的ubuntu虚拟机使用命令sudo dd if="（这里是镜像文件）" of="（这里是你的u盘，例如/dev/sdb）"将镜像拷贝到U盘，一番操作后，我竟然装成双系统。此时开始怀疑人生。
经过考虑与学习后，终于找到正确的方法。鉴于之前的分区软件分区速度太慢，换用软件disk genius，将U盘分为3个区，在VMware虚拟机新建Kali虚拟机，然后在设置中弹出预分配的20G硬盘（后来发现此操作是为了防止在后面选择错本地磁盘和U盘，可以不用），点击运行开始安装Kali，在后面选择安装磁盘时选择U盘，3个分区分别设置为根目录，存储区和swap交换区。针对于开机后无法入进系统的问题的解决：在启动页面按e键进入编辑，更改linux行的根目录为之前分配时的分区，并在改行结尾加上nouveau.modeset=0,这是为了禁用独立显卡以解决Kali系统在双显卡下启动失败的问题。
##使用Kali
在使用Kali进行系统设置（如更新源，更新系统，更新软件，安装中文输入法，配置ssr，校准时间等）时，遇到了很多困难，在这里不详讲。主要是时使用Kali工具进行wifi破解以及局域网内渗透时的困难和解决方法。
###破解wifi
wifi破解大致可以分为两种方法，一是暴力破解，二是钓鱼。  
在暴力破解时，遇到的困难就是破解率低，解决方法是换用字典。还有方法就是采用社会工程学，利用cupp工具，输入目标的信息，如“wifi所有人的姓名，生日”等信息，cupp会自动生成一个字典，关于cupp还有其他功能，可以自行了解。  
使用fluxion框架搭建钓鱼网页，因为版本可能不一致，我的fluxion在使用时需要先用aircrack生成握手包，然后在用fluxion选择握手包来搭建框架，可能因为电脑网卡的原因，和同学交流在操作上没什么问题，但是结果总是报错。
###局域网内的渗透
Kali中的ettetcap是一款现有流行的网络抓包软件，利用它可以实现同局域网下利用他人cookie来登录网站，或是配合driftnet来监听他人的图片流量。遇到的困难：有时操作失败可能是因为网卡被其他程序占用，这时需要检查占用并清除。
##参考教程
[安装KAli教程](http://www.pianshen.com/article/3693482337/)

[暴力破解wifi教程](https://blog.csdn.net/kinnisoy/article/details/90240575)

[fluxion钓鱼参考教程](https://blog.csdn.net/ljt101222/article/details/84109302)

[cupp](https://www.freebuf.com/sectool/144740.html)

[ettercap的使用](https://blog.csdn.net/zc19930620/article/details/61642372/)

[ghs?](https://www.cnblogs.com/lvchenfeng/p/5596572.html)

[干货分享](https://www.shiyanlou.com/courses/698)