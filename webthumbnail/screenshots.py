#-* coding:UTF-8 -*      
'''
Created on 2013年8月29日

@author: ezioruan
'''
import sys
import time
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtWebKit import *

class Screenshot(QWebView):
    def __init__(self):
        self.app = QApplication(sys.argv)
        QWebView.__init__(self)
        self._loaded = False
        self.loadFinished.connect(self._loadFinished)

    def capture(self, url, output_file,width, height):
        self.load(QUrl(url))
        self.wait_load()
        # set to webpage size
        frame = self.page().mainFrame()
        self.page().setViewportSize(frame.contentsSize())
        # render image
        image = QImage(self.page().viewportSize(), QImage.Format_ARGB32)
        painter = QPainter(image)
        frame.render(painter)
        painter.end()
        print 'saving', output_file
        scaled = self.scale(image, width, height)
        scaled.save(output_file)
        
    def capture_content(self,content,output_file,width, height):
        self.setContent(content)
        self.wait_load()
        # set to webpage size
        frame = self.page().mainFrame()
        self.page().setViewportSize(frame.contentsSize())
        # render image
        image = QImage(self.page().viewportSize(), QImage.Format_ARGB32)
        painter = QPainter(image)
        frame.render(painter)
        painter.end()
        print 'saving', output_file
        scaled = self.scale(image, int(width), int(height))
        scaled.save(output_file)
    
        
    def scale(self, image, width=None, height=None):
        if width is None and height is None:
            scaled = image
        elif width is None:
            scaled = image.scaledToHeight(height, Qt.SmoothTransformation)
        elif height is None:
            scaled = image.scaledToWidth(width, Qt.SmoothTransformation)
        else:
            scaled = image.scaled(width, height,
                    Qt.KeepAspectRatioByExpanding,
                    Qt.SmoothTransformation)
            scaled = scaled.copy(0, 0, width, height)
        return scaled

    def wait_load(self, delay=0):
        # process app events until page loaded
        while not self._loaded:
            self.app.processEvents()
            time.sleep(delay)
        self._loaded = False

    def _loadFinished(self, result):
        self._loaded = True
if __name__ == '__main__':
    s = Screenshot()
    s.capture('http://webscraping.com', 'website.png',300,200)
    s.capture('http://webscraping.com/blog', 'blog.png',300,300)


    content = """ 
    
    <!Doctype html><html xmlns=http://www.w3.org/1999/xhtml><head><meta http-equiv=Content-Type content="text/html;charset=utf-8"><meta http-equiv=X-UA-Compatible content=IE=EmulateIE7><title>百度一下，你就知道 </title><style type="text/css">body,h1,h2,h3,h4,h5,h6,hr,p,blockquote,dl,dt,dd,ul,ol,li,pre,form,fieldset,legend,button,input,textarea,th,td{margin:0;padding:0}html{color:#000;overflow-y:scoll;overflow:-moz-scrollbars-vertical}body,button,input,select,textarea{font-size:12px;font-family:arial,\5b8b\4f53,sans-serif}h1,h2,h3,h4,h5,h6{font-size:100%}em{font-style:normal}small{font-size:12px}ul,ol{list-style:none}a{text-decoration:none}a:hover{text-decoration:underline}legend{color:#000}fieldset,img{border:0}button,input,select,textarea{font-size:100%}table{border-collapse:collapse;border-spacing:0}img{-ms-interpolation-mode:bicubic}textarea{resize:vertical}.left{float:left}.right{float:right}.overflow{overflow:hidden}.hide{display:none}.block{display:block}.inline{display:inline}.error{color:#F00;font-size:12px}label,button{cursor:pointer}.grid-5,.grid-30,.grid-39,.grid-42,.grid-50,.grid-56,.grid-62,.grid-71,.grid-73,.grid-92,.grid-98{overflow:hidden;margin:0 auto;padding:0}.grid-5{width:50px}.grid-30{width:300px}.grid-39{width:390px}.grid-42{width:420px}.grid-50{width:500px}.grid-56{width:560px}.grid-62{width:620px}.grid-71{width:710px}.grid-73{width:730px}.grid-92{width:920px}.grid-98{width:980px}.clearfix:after{content:'\20';display:block;height:0;clear:both}.clearfix{zoom:1}.clear{clear:both;height:0;line-height:0;font-size:0;visibility:hidden;overflow:hidden}.wordwrap{word-break:break-all;word-wrap:break-word}pre.wordwrap{white-space:pre-wrap}body{text-align:center}body,form,#s_fm{position:relative}td{text-align:left}img{border:0}#u{color:#999;padding:4px 10px 5px 0;text-align:right}#u a{color:#00c;text-decoration:underline;margin:0 5px}#u a.last{margin-right:0}#m{width:680px;margin:0 auto}#nv{margin:0 0 5px;_margin-bottom:4px;padding:2px 0 0;text-align:left;text-indent:72px}#nv a,#nv b{margin-left:12px}#nv a,#nv b,.btn,#lk{font-size:14px}#s_fm{text-align:left;padding-left:61px;z-index:300;height:35px}#kw,.btn,.btn_wr,#mCon{background:url(http://su.bdimg.com/static/superpage/img/spis_9762e054.png) no-repeat #fff}#kw{width:529px;height:22px;padding:4px 7px;padding:6px 7px 2px\9;font:16px arial;border:1px solid #cdcdcd;border-color:#9a9a9a #cdcdcd #cdcdcd #9a9a9a;vertical-align:top;outline:none}.btn{width:95px;height:32px;padding:0;padding-top:2px\9;border:0;background-position:0 -35px;background-color:#ddd;cursor:pointer}.btn_h{background-position:-100px -35px}#kw,.btn_wr{margin:0 3px 0 0}.btn_wr{background-position:-202px -33px;width:97px;height:34px;display:inline-block;_margin-top:1px}#lk{margin:33px 0}#lk span{font:14px "\5b8b\4f53"}#lh{margin:16px 0 5px;word-spacing:3px}#mCon{position:absolute;right:5px;top:10px;height:15px;line-height:15px;width:25px;cursor:pointer;padding:0 16px 0 0;background-position:right -206px}#mCon span{color:#00c;cursor:default;display:block}#mCon .hw{text-decoration:underline;cursor:pointer}#mMenu{width:56px;border:1px solid #9B9B9B;list-style:none;position:absolute;right:2px;top:28px;display:none;background:#fff;box-shadow:1px 1px 2px #ccc;-moz-box-shadow:1px 1px 2px #ccc;-webkit-box-shadow:1px 1px 2px #ccc;filter:progid:DXImageTransform.Microsoft.Shadow(Strength=2, Direction=135, Color="#cccccc")\9}#mMenu a,#mMenu a:visited{color:#00C;width:100%;height:100%;display:block;line-height:22px;text-indent:6px;text-decoration:none;filter:none\9}#mMenu a:hover{background:#ebebeb}#mMenu .ln{height:1px;background:#ebebeb;overflow:hidden;font-size:1px;line-height:1px;margin-top:-1px}#cp,#cp a{color:#77c}#tb_mr{color:#00C;cursor:pointer;position:relative;z-index:200}#tb_mr b{font-weight:normal}#nv a,#tb_mr b{text-decoration:underline}#nv a{color:#00C}#hwr_div,#loading{z-index:3000}#mHolder{display:none}.user-name-top{cursor:pointer;line-height:20px;color:#00C;font-weight:bold;padding-right:11px;background:url(http://su.bdimg.com/static/superpage/img/spis_9762e054.png) no-repeat right -221px}html{overflow:-moz-scrollbars-vertical;overflow-y:scroll}.main{display:none}#s_feed{display:none}.s-ps-sug{border:1px solid #817F82;position:absolute;top:32px;left:0}.s-ps-sug table{width:100%;background:#fff;cursor:default}.s-ps-sug td{color:#000;font:14px arial;height:25px;line-height:25px;padding:0 8px}.s-ps-sug td b{color:#000}.s-ps-sug .mo{background:#ebebeb}.s-ps-sug .ml{background:#fff}.s-ps-sug td.sug_storage{color:#7A77C8}.s-ps-sug td.sug_storage b{color:#7A77C8}.s-ps-sug .sug_del{font-size:12px;color:#666;text-decoration:underline;float:right;cursor:pointer;display:none}.s-ps-sug .sug_del{font-size:12px;color:#666;text-decoration:underline;float:right;cursor:pointer;display:none}.s-ps-sug .mo .sug_del{display:block}.s-ps-sug .sug_ala{border-bottom:1px solid #e6e6e6}.s-ps-sug td h3{line-height:14px;margin:6px 0 4px 0;font-size:12px;font-weight:normal;color:#7B7B7B;padding-left:20px;background:url(img/sug_bd.png) no-repeat left center}.s-ps-sug td p{font-size:14px;font-weight:bold;padding-left:20px}.s-ps-sug td p span{font-size:12px;font-weight:normal;color:#7B7B7B}#s_user_center{font-weight:normal;background-position:right -223px\9}#s_user_center_menu{right:131px}</style><link rel=stylesheet id=s_superpage_css_lnk type=text/css href="http://su.bdimg.com/static/superpage/css/index_min_857b3fd6.css"><link href="http://su.bdimg.com/static/nav/css/nav_min_dcb1b309.css" type=text/css rel=stylesheet><link href="http://su.bdimg.com/static/msg/css/mt_min_2d8df993.css" type=text/css rel=stylesheet><link href="http://su.bdimg.com/static/pack/css/supercube_d1fc7cc5.css" type=text/css rel=stylesheet><link href="http://su.bdimg.com/static/skin/css/skin_d49e6c55.css" type=text/css rel=stylesheet><script>
    
    window.sysTime=1377764224;
    </script><noscript><meta http-equiv=refresh content="0; url=http://www.baidu.com/baidu.html?from=noscript"></noscript></head><body  class="s-skin-user "><div class=s-skin-container ></div><p id=u class=s-weather-border><a class=user-name-top id=s_username_top href="/p/ezioruan?from=super">ezioruan</a>|<a class=user-name-top id=s_user_center href=http://i.baidu.com/center>个人中心</a>|<a href=/gaoji/preferences.html>搜索设置</a>|<a id=s_tradditional_link class=last href="/home/page/show/classic">传统首页</a></p><div id=s_username_menu class=s-username-menu style="display:none;right:201px;+right:199px;_right:198px;"><a href="/p/ezioruan?from=super">我的主页</a><a href="http://passport.baidu.com/">个人资料</a><a href=/home/page/show/setting>首页设置</a><a class=sep style=overflow:hidden href="https://passport.baidu.com/?logout&u=http://www.baidu.com">退出</a></div><div id=s_user_center_menu class=s-username-menu style="display:none;"><a href=http://i.baidu.com/my/collect>我的收藏</a><a href=http://i.baidu.com/my/cal>我的日历</a><a href=http://i.baidu.com/my/track>浏览记录</a> </div><div class=clear></div><div id=m style=width:720px><p id=lg> <img src="http://www.baidu.com/img/bdlogo.gif" width=270 height=129  ></p><p id=nv><a href=http://news.baidu.com>新闻</a><b>网页</b><a href=http://tieba.baidu.com>贴吧</a><a href=http://zhidao.baidu.com>知道</a><a href=http://music.baidu.com>音乐</a><a href=http://image.baidu.com>图片</a><a href=http://v.baidu.com>视频</a><a href=http://map.baidu.com>地图</a><a href=http://baike.baidu.com>百科</a><a href=http://wenku.baidu.com>文库</a><a style="font-family: \5b8b\4f53;" href=http://www.baidu.com/more/>更多>></a></p><div id=s_fm><form name=f id=s_ps_form action=http://www.baidu.com/s  onsubmit="javascript:F.call('ps/sug','pssubmit');"><input type=text name=wd id=kw maxlength=100 style="width:474px;"><input type=hidden name=rsv_spt value=1> <input type=hidden name=issp value=1><input type=hidden name=rsv_bp value=0><input type=hidden name=ie value=utf-8><input type=hidden name=tn  value=baiduhome_pg ><span class=btn_wr><input type=submit value="百度一下" id=su class=btn onmousedown="this.className='btn btn_h'" onmouseout="this.className='btn'"></span></form><span id=mHolder><div id=mCon><span>输入法</span></div></span><ul id=mMenu><li><a href="#" name=ime_hw>手写</a><li><a href="#" name=ime_py>拼音</a><li class=ln><li><a href="#" name=ime_cl>关闭</a></ul></div><div id=lm></div></div><div id=s_wl  style="display:none;" ></div><p class=s-skin-lm></p><div id=s_wrap style="margin:15px auto auto;"><div id=s_main class="main mod-main-old clearfix"> <div id=s_modules>              <div class=s-notify-pnl>  <div class=s-pk-mod data-pkid='31'> <div class=pk-content><div class=pk-loading>正在加载中...</div></div> </div> </div>  <div style="" isViewMod="" class="mod-sc s-mod mod-pk-nav" id=s_mod_nav data-modid=1><a name=shortcut class=s-mod-hida id=shortcut>&nbsp;</a> <div class=s-container> <div class=s-title id=s_mod_nav_titleBar style=""> <a title="隐藏" id=s_mod_nav_close class="s-mod-close-view nav-close-pack" href="javascript:;"></a> <a id=s_mod_nav_b_settings href="javascript:;" onclick="return false;" title="编辑"  class=s-mod-set-view hidefocus><b id=b_edit_text>编辑</b><em id=s_b_settings_icon> </em> </a> <a id=s_mod_nav_add class=s-shortcut-add href="javascript:;" onclick="return false;"  hidefocus><em>添加</em></a><em class=s-mod-nav>我的导航</em><span class=s-nav-cur-edit-tab style="display:none;"></span><div class=s-title-bg></div></div> <div class=s-content id=s_mod_nav_content style="text-align: center;">       <div class="s-nori" id=s_nav_area>  <ul class=s-nori-navs id=s_nori_navs_0>  <li id="s_nav_10843486" class=s-nori-nav > <a href="http://tieba.baidu.com/" class=s-nav-name target=_blank title="百度贴吧" hidefocus> <img width=16 height=16 data-src="http://5.su.bdimg.com/icon/2556.png?3" > <em class=sc-dragitem>百度贴吧</em></a>   <li id="s_nav_4502220" class=s-nori-nav > <a href="http://www.taobao.com/" class=s-nav-name target=_blank title="淘宝网" hidefocus> <img width=16 height=16 data-src="http://7.su.bdimg.com/icon/10062.png" > <em class=sc-dragitem>淘宝网</em></a>   <li id="s_nav_904305" class=s-nori-nav > <a href="http://weibo.com/" class=s-nav-name target=_blank title="新浪微博" hidefocus> <img width=16 height=16 data-src="http://7.su.bdimg.com/icon/54.png?1" > <em class=sc-dragitem>新浪微博</em></a>   <li id="s_nav_5915062" class=s-nori-nav > <a href="http://www.youku.com/" class=s-nav-name target=_blank title="优酷网" hidefocus> <img width=16 height=16 data-src="http://6.su.bdimg.com/icon/10605.png" > <em class=sc-dragitem>优酷网</em></a>   <li id="s_nav_10801713" class=s-nori-nav > <a href="http://www.hao123.com/" class=s-nav-name target=_blank title="hao123" hidefocus> <img width=16 height=16 data-src="http://5.su.bdimg.com/icon/8604.png" > <em class=sc-dragitem>hao123</em></a>   <li id="s_nav_3567131" class=s-nori-nav > <a href="http://www.360buy.com/" class=s-nav-name target=_blank title="京东商城" hidefocus> <img width=16 height=16 data-src="http://4.su.bdimg.com/icon/95475.png" > <em class=sc-dragitem>京东商城</em></a>   <li id="s_nav_3170376" class=s-nori-nav > <a href="http://www.mop.com/" class=s-nav-name target=_blank title="猫扑" hidefocus> <img width=16 height=16 data-src="http://1.su.bdimg.com/icon/1584.png?1" > <em class=sc-dragitem>猫扑</em></a>   <li id="s_nav_1794054" class=s-nori-nav > <a href="http://qzone.qq.com/" class=s-nav-name target=_blank title="qq空间" hidefocus> <img width=16 height=16 data-src="http://4.su.bdimg.com/icon/7083.png" > <em class=sc-dragitem>qq空间</em></a>   <li id="s_nav_6969151" class=s-nori-nav > <a href="http://www.amazon.cn/" class=s-nav-name target=_blank title="亚马逊" hidefocus> <img width=16 height=16 data-src="http://3.su.bdimg.com/icon/7594.png" > <em class=sc-dragitem>亚马逊</em></a>   <li id="s_nav_5499087" class=s-nori-nav > <a href="http://www.tmall.com/" class=s-nav-name target=_blank title="淘宝商城" hidefocus> <img width=16 height=16 data-src="http://3.su.bdimg.com/icon/10138.png?1" > <em class=sc-dragitem>淘宝商城</em></a>   <li id="s_nav_12396517" class=s-nori-nav > <a href="http://app.baidu.com/app/enter?appid=101074" class=s-nav-name target=_blank title="快递查询" hidefocus> <img width=16 height=16 data-src="http://2.su.bdimg.com/icon/11345.png?1" > <em class=sc-dragitem>快递查询</em></a>    <li id=s_nori_add_btn class=s-nori-add-btn><a hidefocus href="#" onclick="return false;"></a>  </ul>  </div>   </div> </div></div> <div style="" id=s_mod_topsearch class="mod-sc s-mod mod-pk-hot" data-modid=6><a name=topsearch class=s-mod-hida id=hithot>&nbsp;</a> <div class=s-container> <div class=s-title id=s_mod_topsearch_titleBar style=""> <a title="隐藏" id=s_mod_topsearch_close class=s-mod-close-view href="#" onclick="return false;" hidefocus></a> <a title="换一换" id=s_mod_topsearch_change class=s-topsearch-change href="#" onclick="return false;" hidefocus>换一换</a><span class=s-topsearch-title>实时热点</span><span id=s_topsearch_nu_tip style="display:none;">亿万网友都在搜什么？</span><div class=s-title-bg></div></div><div class=s-content id=s_mod_topsearch_content><div class=s-topsearch-data-waiter>资源加载中，请稍后！</div><span class=s-topsearch-more>查看更多：<a href=http://top.baidu.com/buzz.php?p=top10 target=_blank hidefocus>百度风云榜</a></span></div> </div></div><textarea id="hot_news_data" style="display:none">
        {"errNo":"0","hotSearchWords" : [{"detailurl":"http://www.baidu.com/baidu?cl=3&tn=baidutop10&fr=top1000&wd=%E6%96%B9%E6%BB%A8%E5%85%B4%E7%9A%84%E5%A2%99%E5%86%85%E5%A2%99%E5%A4%96","cut":"","key":"方滨兴的墙内墙外","isnew":"true","isred":"0","ispm":"0"},{"detailurl":"http://www.baidu.com/baidu?cl=3&tn=baidutop10&fr=top1000&wd=%E5%A7%9C%E6%96%87%E8%80%81%E5%A9%86","cut":"","key":"姜文老婆","isnew":"true","isred":"0","ispm":"0"},{"detailurl":"http://www.baidu.com/baidu?cl=3&tn=baidutop10&fr=top1000&wd=%E5%BC%A0%E9%A6%A8%E4%BA%88%E6%9D%8E%E6%99%A8","cut":"","key":"张馨予李晨","isnew":"true","isred":"0","ispm":"0"},{"detailurl":"http://www.baidu.com/baidu?cl=3&tn=baidutop10&fr=top1000&wd=%E8%96%9B%E8%9B%AE%E5%AD%90+%E7%A7%A6%E7%81%AB%E7%81%AB","cut":"","key":"薛蛮子 秦火火","isnew":"false","isred":"0","ispm":"0"},{"detailurl":"http://www.baidu.com/baidu?cl=3&tn=baidutop10&fr=top1000&wd=%E5%A5%B3%E6%8E%92%E5%A4%A7%E5%A5%96%E8%B5%9B%E6%80%BB%E5%86%B3%E8%B5%9B","cut":"","key":"女排大奖赛总决赛","isnew":"false","isred":"0","ispm":"0"},{"detailurl":"http://www.baidu.com/baidu?cl=3&tn=baidutop10&fr=top1000&wd=%E8%A5%BF%E7%8F%AD%E7%89%99%E8%B6%85%E7%BA%A7%E6%9D%AF","cut":"","key":"西班牙超级杯","isnew":"false","isred":"0","ispm":"0"},{"detailurl":"http://www.baidu.com/baidu?cl=3&tn=baidutop10&fr=top1000&wd=%E5%A5%B3%E5%AD%90%E7%82%92%E5%9C%B0%E7%82%92%E6%88%90%E6%B8%85%E6%B4%81%E5%B7%A5","cut":"","key":"女子炒地炒成清洁工","isnew":"false","isred":"0","ispm":"0"},{"detailurl":"http://www.baidu.com/baidu?cl=3&tn=baidutop10&fr=top1000&wd=%E5%8D%8E%E4%B8%BA%E7%A7%98%E7%9B%92","cut":"","key":"华为秘盒","isnew":"false","isred":"0","ispm":"0"},{"detailurl":"http://www.baidu.com/baidu?cl=3&tn=baidutop10&fr=top1000&wd=%E8%B0%8B%E5%9C%A3%E9%AC%BC%E8%B0%B7%E5%AD%90","cut":"","key":"谋圣鬼谷子","isnew":"false","isred":"0","ispm":"0"},{"detailurl":"http://www.baidu.com/baidu?cl=3&tn=baidutop10&fr=top1000&wd=%E8%AF%BA%E5%9F%BA%E4%BA%9A515","cut":"","key":"诺基亚515","isnew":"false","isred":"0","ispm":"0"},{"detailurl":"http://www.baidu.com/baidu?cl=3&tn=baidutop10&fr=top1000&wd=%E6%9D%A8%E7%B4%AB%E6%99%92%E6%B3%B3%E8%A3%85%E7%85%A7","cut":"","key":"杨紫晒泳装照","isnew":"false","isred":"0","ispm":"0"},{"detailurl":"http://www.baidu.com/baidu?cl=3&tn=baidutop10&fr=top1000&wd=%E5%9B%BD%E4%BA%94%E6%B1%BD%E6%B2%B9","cut":"","key":"国五汽油","isnew":"false","isred":"0","ispm":"0"},{"detailurl":"http://www.baidu.com/baidu?cl=3&tn=baidutop10&fr=top1000&wd=%E7%99%BE%E5%BA%A6%E5%AF%BC%E8%88%AA","cut":"","key":"百度导航","isnew":"false","isred":"0","ispm":"0"},{"detailurl":"http://www.baidu.com/baidu?cl=3&tn=baidutop10&fr=top1000&wd=%E5%B9%B3%E8%83%B8%E5%A4%A7%E8%B5%9B","cut":"","key":"平胸大赛","isnew":"false","isred":"0","ispm":"0"},{"detailurl":"http://www.baidu.com/baidu?cl=3&tn=baidutop10&fr=top1000&wd=%E6%96%B0%E7%96%86%E5%9C%B0%E9%9C%87","cut":"","key":"新疆地震","isnew":"false","isred":"0","ispm":"0"},{"detailurl":"http://www.baidu.com/baidu?cl=3&tn=baidutop10&fr=top1000&wd=%E6%8B%93%E4%B9%9F%E5%93%A5+%E5%8F%A3%E6%8A%80","cut":"","key":"拓也哥 口技","isnew":"false","isred":"0","ispm":"0"},{"detailurl":"http://www.baidu.com/baidu?cl=3&tn=baidutop10&fr=top1000&wd=%E6%9D%8E%E5%A4%A9%E4%B8%80%E6%A1%88%E5%8F%97%E5%AE%B3%E4%BA%BA%E8%8B%8F%E9%86%92","cut":"","key":"李天一案受害人苏醒","isnew":"false","isred":"0","ispm":"0"},{"detailurl":"http://www.baidu.com/baidu?cl=3&tn=baidutop10&fr=top1000&wd=%E8%8B%B1%E5%9B%BD%E5%9F%8E%E7%AE%A1","cut":"","key":"英国城管","isnew":"false","isred":"0","ispm":"0"},{"detailurl":"http://www.baidu.com/baidu?cl=3&tn=baidutop10&fr=top1000&wd=%E5%9B%BD%E9%97%A8%E6%9D%A8%E6%99%BA%E5%9C%A8%E6%A5%BC%E9%A1%B6%E8%BF%9D%E5%BB%BA","cut":"","key":"国门杨智在楼顶违建","isnew":"false","isred":"0","ispm":"0"},{"detailurl":"http://www.baidu.com/baidu?cl=3&tn=baidutop10&fr=top1000&wd=%E8%BF%9012%E9%A3%9E%E8%BF%91%E9%92%93%E9%B1%BC%E5%B2%9B","cut":"","key":"运12飞近钓鱼岛","isnew":"false","isred":"0","ispm":"0"},{"detailurl":"http://www.baidu.com/baidu?cl=3&tn=baidutop10&fr=top1000&wd=%E6%96%B0%E7%96%86%E6%9A%B4%E5%8A%9B%E6%A1%88%E4%B8%80%E7%89%B9%E8%AD%A6%E7%89%BA%E7%89%B2","cut":"","key":"新疆暴力案一特警牺牲","isnew":"false","isred":"0","ispm":"0"},{"detailurl":"http://www.baidu.com/baidu?cl=3&tn=baidutop10&fr=top1000&wd=%E5%BC%A0%E5%BF%85%E6%B8%85%E5%AE%B6%E5%86%85%E9%83%A8%E7%85%A7%E6%9B%9D%E5%85%89","cut":"","key":"张必清家内部照曝光","isnew":"false","isred":"0","ispm":"0"},{"detailurl":"http://www.baidu.com/baidu?cl=3&tn=baidutop10&fr=top1000&wd=%E9%99%88%E5%A6%8D%E5%B8%8C%E5%B0%8F%E9%BE%99%E5%A5%B3","cut":"","key":"陈妍希小龙女","isnew":"false","isred":"0","ispm":"0"},{"detailurl":"http://www.baidu.com/baidu?cl=3&tn=baidutop10&fr=top1000&wd=%E6%9D%8E%E5%A4%A9%E4%B8%80%E6%A1%88%E4%BB%8A%E5%BC%80%E5%BA%AD","cut":"","key":"李天一案今开庭","isnew":"false","isred":"0","ispm":"0"},{"detailurl":"http://www.baidu.com/baidu?cl=3&tn=baidutop10&fr=top1000&wd=%E4%B8%AD%E7%9F%B3%E6%B2%B9%E4%BA%BA%E4%BA%8B%E5%9C%B0%E9%9C%87","cut":"","key":"中石油人事地震","isnew":"false","isred":"0","ispm":"0"},{"detailurl":"http://www.baidu.com/baidu?cl=3&tn=baidutop10&fr=top1000&wd=%E5%8D%8E%E4%B8%BA%E8%8D%A3%E8%80%803%E5%8F%91%E5%B8%83%E4%BC%9A","cut":"","key":"华为荣耀3发布会","isnew":"false","isred":"0","ispm":"0"},{"detailurl":"http://www.baidu.com/baidu?cl=3&tn=baidutop10&fr=top1000&wd=%E4%B8%AD%E5%9B%BD%E6%B8%B8%E5%AE%A2%E9%A1%BA%E8%88%AA%E7%8F%AD%E5%88%80%E5%8F%89","cut":"","key":"中国游客顺航班刀叉","isnew":"false","isred":"0","ispm":"0"},{"detailurl":"http://www.baidu.com/baidu?cl=3&tn=baidutop10&fr=top1000&wd=%E5%9B%9B%E5%B7%9D%E4%BA%91%E5%8D%97%E4%BA%A4%E7%95%8C%E5%9C%B0%E9%9C%87","cut":"","key":"四川云南交界地震","isnew":"false","isred":"0","ispm":"0"},{"detailurl":"http://www.baidu.com/baidu?cl=3&tn=baidutop10&fr=top1000&wd=%E5%A4%A7%E8%BF%9E%E8%88%B9%E8%88%B6%E9%87%8D%E5%B7%A5%E9%9B%86%E5%9B%A2","cut":"","key":"大连船舶重工集团","isnew":"false","isred":"0","ispm":"0"},{"detailurl":"http://www.baidu.com/baidu?cl=3&tn=baidutop10&fr=top1000&wd=%E6%B7%B1%E5%9C%B3%E5%85%AC%E5%8E%95%E5%B0%BF%E6%AD%AA","cut":"","key":"深圳公厕尿歪","isnew":"false","isred":"0","ispm":"0"},{"detailurl":"http://www.baidu.com/baidu?cl=3&tn=baidutop10&fr=top1000&wd=%E8%85%BE%E8%AE%AF%E5%BE%AE%E4%BA%9110t","cut":"","key":"腾讯微云10t","isnew":"false","isred":"0","ispm":"0"},{"detailurl":"http://www.baidu.com/baidu?cl=3&tn=baidutop10&fr=top1000&wd=%E8%8E%AB%E6%96%AF%E7%A7%91%E8%88%AA%E5%B1%95%E5%BC%80%E5%B9%95","cut":"","key":"莫斯科航展开幕","isnew":"false","isred":"0","ispm":"0"},{"detailurl":"http://www.baidu.com/baidu?cl=3&tn=baidutop10&fr=top1000&wd=%E4%BA%91%E9%9C%84%E7%89%A9%E4%BB%B7%E5%B1%80%E9%95%BF","cut":"","key":"云霄物价局长","isnew":"false","isred":"0","ispm":"0"},{"detailurl":"http://www.baidu.com/baidu?cl=3&tn=baidutop10&fr=top1000&wd=%E8%8B%8F%E5%B7%9E%E8%BD%A8%E4%BA%A45%E5%8F%B7%E7%BA%BF","cut":"","key":"苏州轨交5号线","isnew":"false","isred":"0","ispm":"0"},{"detailurl":"http://www.baidu.com/baidu?cl=3&tn=baidutop10&fr=top1000&wd=%E5%8D%81%E5%85%AB%E5%B1%8A%E4%B8%89%E4%B8%AD%E5%85%A8%E4%BC%9A11%E6%9C%88%E5%8F%AC%E5%BC%80","cut":"","key":"十八届三中全会11月召开","isnew":"false","isred":"0","ispm":"0"},{"detailurl":"http://www.baidu.com/baidu?cl=3&tn=baidutop10&fr=top1000&wd=%E9%B2%81%E8%B1%AB%E6%9C%89%E7%BA%A6%E6%9E%97%E4%B9%A6%E8%B1%AA","cut":"","key":"鲁豫有约林书豪","isnew":"false","isred":"0","ispm":"0"},{"detailurl":"http://www.baidu.com/baidu?cl=3&tn=baidutop10&fr=top1000&wd=crv%E5%8F%AC%E5%9B%9E","cut":"","key":"crv召回","isnew":"false","isred":"0","ispm":"0"},{"detailurl":"http://www.baidu.com/baidu?cl=3&tn=baidutop10&fr=top1000&wd=%E6%96%B0%E7%96%86%E5%96%80%E4%BB%80%E6%9A%B4%E5%8A%9B%E4%BA%8B%E4%BB%B6","cut":"","key":"新疆喀什暴力事件","isnew":"false","isred":"0","ispm":"0"},{"detailurl":"http://www.baidu.com/baidu?cl=3&tn=baidutop10&fr=top1000&wd=%E9%99%88%E6%9C%89%E8%A5%BF%E5%85%A8%E9%9D%A2%E8%A7%A3%E6%9E%90%E6%9D%8E%E5%A4%A9%E4%B8%80%E6%A1%88","cut":"","key":"陈有西全面解析李天一案","isnew":"false","isred":"0","ispm":"0"},{"detailurl":"http://www.baidu.com/baidu?cl=3&tn=baidutop10&fr=top1000&wd=%E6%B1%A0%E9%97%B4%E6%99%B6%E5%AD%90","cut":"","key":"池间晶子","isnew":"false","isred":"0","ispm":"0"},{"detailurl":"http://www.baidu.com/baidu?cl=3&tn=baidutop10&fr=top1000&wd=%E5%BE%AE%E4%BA%9110t","cut":"","key":"微云10t","isnew":"false","isred":"0","ispm":"0"},{"detailurl":"http://www.baidu.com/baidu?cl=3&tn=baidutop10&fr=top1000&wd=%E7%BE%8E%E5%9B%BD%E6%88%96%E5%AF%B9%E5%8F%99%E5%BC%80%E6%88%98","cut":"","key":"美国或对叙开战","isnew":"false","isred":"0","ispm":"0"},{"detailurl":"http://www.baidu.com/baidu?cl=3&tn=baidutop10&fr=top1000&wd=%E5%9C%B0%E9%93%81%E7%BB%84%E5%90%88%E6%8B%B3","cut":"","key":"地铁组合拳","isnew":"false","isred":"0","ispm":"0"},{"detailurl":"http://www.baidu.com/baidu?cl=3&tn=baidutop10&fr=top1000&wd=s3%E5%A5%96%E5%8A%B1","cut":"","key":"s3奖励","isnew":"false","isred":"0","ispm":"0"},{"detailurl":"http://www.baidu.com/baidu?cl=3&tn=baidutop10&fr=top1000&wd=%E6%97%A9%E8%A1%B0%E5%B0%91%E5%B9%B4","cut":"","key":"早衰少年","isnew":"false","isred":"0","ispm":"0"},{"detailurl":"http://www.baidu.com/baidu?cl=3&tn=baidutop10&fr=top1000&wd=%E7%96%AF%E7%8B%82%E7%9A%84%E5%AF%BC%E6%BC%94","cut":"","key":"疯狂的导演","isnew":"false","isred":"0","ispm":"0"},{"detailurl":"http://www.baidu.com/baidu?cl=3&tn=baidutop10&fr=top1000&wd=%E5%A5%B3%E9%A9%B4%E5%8F%8B%E6%91%86%E6%8B%8D%E5%9D%A0%E5%B4%96","cut":"","key":"女驴友摆拍坠崖","isnew":"false","isred":"0","ispm":"0"},{"detailurl":"http://www.baidu.com/baidu?cl=3&tn=baidutop10&fr=top1000&wd=%E6%B5%99%E6%B1%9F%E7%99%BE%E5%BC%BA%E4%BC%81%E4%B8%9A","cut":"","key":"浙江百强企业","isnew":"false","isred":"0","ispm":"0"},{"detailurl":"http://www.baidu.com/baidu?cl=3&tn=baidutop10&fr=top1000&wd=%E5%AE%9C%E5%AE%BE%E8%BD%A6%E7%A5%B8","cut":"","key":"宜宾车祸","isnew":"false","isred":"0","ispm":"0"},{"detailurl":"http://www.baidu.com/baidu?cl=3&tn=baidutop10&fr=top1000&wd=%E6%9D%A8%E8%BE%BE%E6%89%8D%E6%A1%8830%E6%97%A5%E5%BC%80%E5%BA%AD","cut":"","key":"杨达才案30日开庭","isnew":"false","isred":"0","ispm":"0"},{"detailurl":"http://www.baidu.com/baidu?cl=3&tn=baidutop10&fr=top1000&wd=%E9%A6%99%E6%A0%BC%E9%87%8C%E6%8B%89%E5%9C%B0%E9%9C%87","cut":"","key":"香格里拉地震","isnew":"false","isred":"0","ispm":"0"},{"detailurl":"http://www.baidu.com/baidu?cl=3&tn=baidutop10&fr=top1000&wd=%E4%B8%80%E5%BC%A0%E4%B8%8D%E5%A0%AA%E5%9B%9E%E9%A6%96%E7%9A%84%E7%AB%A5%E5%B9%B4%E7%85%A7%E7%89%87","cut":"","key":"一张不堪回首的童年照片","isnew":"false","isred":"0","ispm":"0"},{"detailurl":"http://www.baidu.com/baidu?cl=3&tn=baidutop10&fr=top1000&wd=%E6%9D%8E%E5%A8%9C%E9%80%80%E5%BD%B9","cut":"","key":"李娜退役","isnew":"false","isred":"0","ispm":"0"},{"detailurl":"http://www.baidu.com/baidu?cl=3&tn=baidutop10&fr=top1000&wd=%E7%94%B7%E7%AB%A5%E8%A2%AB%E6%8C%96%E5%8E%BB%E5%8F%8C%E7%9C%BC","cut":"","key":"男童被挖去双眼","isnew":"false","isred":"0","ispm":"0"},{"detailurl":"http://www.baidu.com/baidu?cl=3&tn=baidutop10&fr=top1000&wd=%E8%A3%B8%E8%83%B8%E8%AE%BF%E9%97%AE%E5%B8%82%E9%95%BF","cut":"","key":"裸胸访问市长","isnew":"false","isred":"0","ispm":"0"},{"detailurl":"http://www.baidu.com/baidu?cl=3&tn=baidutop10&fr=top1000&wd=%E9%99%88%E5%AE%9D%E6%88%90%E5%AE%B6%E4%B8%8D%E5%86%8D%E6%8B%86%E8%BF%81","cut":"","key":"陈宝成家不再拆迁","isnew":"false","isred":"0","ispm":"0"},{"detailurl":"http://www.baidu.com/baidu?cl=3&tn=baidutop10&fr=top1000&wd=%E7%92%80%E7%92%A8%E4%BA%BA%E7%94%9F","cut":"","key":"璀璨人生","isnew":"false","isred":"0","ispm":"0"},{"detailurl":"http://www.baidu.com/baidu?cl=3&tn=baidutop10&fr=top1000&wd=%E6%9C%8B%E5%8F%8B%E5%9C%88%E8%BD%AC%E5%8F%91%E8%B0%A3%E8%A8%80%E8%BF%9D%E6%B3%95","cut":"","key":"朋友圈转发谣言违法","isnew":"false","isred":"0","ispm":"0"}]}</textarea><div class=clear></div><div class='mod-pk mod-pk-old'>                <div class='s-pk-col pk-old-col' style='width:auto;'>    <div class='s-pk-mod music-line-mod' data-pkid=2402 style='height:38px;'> <h5 class='music-line-title pk-line-title'><span class='music-btn-wrap bd-fm-title'><a class=jump-link href=http://fm.baidu.com hidefocus target=_blank></a></span><span class='music-btn-wrap bd-fm-jump'><a class=jump-link href=http://fm.baidu.com target=_blank hidefocus title='新窗口打开'></a></span><span class='pk-title-tab pk-title-tab-0'></span><a href='#' onclick='return false;' class='s-mod-close-view pk-close' title='隐藏' hidefocus></a></h5> <div class=pk-content style='display:none;overflow:hidden;height:0px;'><div class=pk-loading>正在加载中...</div></div> </div>        </div>   <div class='left s-pk-col' style='padding-right:10px;'>  </div>  <div class='left s-pk-col pack-right-col' style='padding-left:10px;'>  </div>  <div class=clear></div> <textarea style='display:none;'>
                                                                    [           {   "id":    "2402"   , "title":    "百度随心听"   , "type":    "音乐"   , "source":    "2"   }     ,         {   "id":    "31"   , "title":    "天气"   , "type":    "天气"   , "source":    "2"   }     ,         {   "id":    "2400"   , "title":    "我的导航"   , "type":    "我的导航"   }     ,         {   "id":    "30"   , "title":    "实时热点"   , "type":    "新闻"   }     ,         {   "id":    "10000"   , "title":    "我的提醒"   , "type":    "消息"   }     ,         {   "id":    "10001"   , "title":    "我的提醒"   , "type":    "消息"   }     ]   
        </textarea></div></div><textarea id = "nav_data" style="display:none">
        {"errNo":"0","data" :[{"dirId":"0","dirName":"","resPath":"","navs": [{"id":"10843486","name":"百度贴吧","url":"http%3A//tieba.baidu.com/","iconUrl":"http://5.su.bdimg.com/icon/2556.png?3","type":"2","time":"1366261440","source":"s_rec","src_extra": "","shortname":"百度贴吧","score":"","clean":"","ubsSource":"s_rec"},{"id":"4502220","name":"淘宝网","url":"http%3A//www.taobao.com/","iconUrl":"http://7.su.bdimg.com/icon/10062.png","type":"4","time":"1366261440","source":"s_rec","src_extra": "","shortname":"淘宝网","score":"","clean":"","ubsSource":"s_rec"},{"id":"904305","name":"新浪微博","url":"http%3A//weibo.com/","iconUrl":"http://7.su.bdimg.com/icon/54.png?1","type":"3","time":"1366261440","source":"s_rec","src_extra": "","shortname":"新浪微博","score":"","clean":"","ubsSource":"s_rec"},{"id":"5915062","name":"优酷网","url":"http%3A//www.youku.com/","iconUrl":"http://6.su.bdimg.com/icon/10605.png","type":"8","time":"1366261440","source":"s_rec","src_extra": "","shortname":"优酷网","score":"","clean":"","ubsSource":"s_rec"},{"id":"10801713","name":"hao123","url":"http%3A//www.hao123.com/","iconUrl":"http://5.su.bdimg.com/icon/8604.png","type":"1","time":"1366261440","source":"s_rec","src_extra": "","shortname":"hao123","score":"","clean":"","ubsSource":"s_rec"},{"id":"3567131","name":"京东商城","url":"http%3A//www.360buy.com/","iconUrl":"http://4.su.bdimg.com/icon/95475.png","type":"4","time":"1366261440","source":"s_rec","src_extra": "","shortname":"京东商城","score":"","clean":"","ubsSource":"s_rec"},{"id":"3170376","name":"猫扑","url":"http%3A//www.mop.com/","iconUrl":"http://1.su.bdimg.com/icon/1584.png?1","type":"3","time":"1366261440","source":"s_rec","src_extra": "","shortname":"猫扑","score":"","clean":"","ubsSource":"s_rec"},{"id":"1794054","name":"qq空间","url":"http%3A//qzone.qq.com/","iconUrl":"http://4.su.bdimg.com/icon/7083.png","type":"3","time":"1366261440","source":"s_rec","src_extra": "","shortname":"qq空间","score":"","clean":"","ubsSource":"s_rec"},{"id":"6969151","name":"亚马逊","url":"http%3A//www.amazon.cn/","iconUrl":"http://3.su.bdimg.com/icon/7594.png","type":"4","time":"1366261440","source":"s_rec","src_extra": "","shortname":"亚马逊","score":"","clean":"","ubsSource":"s_rec"},{"id":"5499087","name":"淘宝商城","url":"http%3A//www.tmall.com/","iconUrl":"http://3.su.bdimg.com/icon/10138.png?1","type":"4","time":"1366261440","source":"s_rec","src_extra": "","shortname":"淘宝商城","score":"","clean":"","ubsSource":"s_rec"},{"id":"12396517","name":"快递查询","url":"http%3A//app.baidu.com/app/enter%3Fappid%3D101074","iconUrl":"http://2.su.bdimg.com/icon/11345.png?1","type":"11","time":"1367486511","source":"u_app","src_extra": "","shortname":"快递查询","score":"","clean":"","ubsSource":"u_app"}] }],"state":"","isNavEmpty":"0","showCommTab":"","defaultDirId":"12"}    </textarea><textarea id="s_skin_conf" style='display:none;'>
            [
                    {
                    "name": "雨夜",
                    "color": "#2a1541",
                    "filename": "21",
                    "defaultOpacity": "80",
                    "dataindex": "21",
                    "isNew": "off"
                }
                ,                {
                    "name": "水墨江南",
                    "color": "#67707f",
                    "filename": "22",
                    "defaultOpacity": "65",
                    "dataindex": "22",
                    "isNew": "off"
                }
                ,                {
                    "name": "城市之光",
                    "color": "#090907",
                    "filename": "23",
                    "defaultOpacity": "75",
                    "dataindex": "23",
                    "isNew": "off"
                }
                ,                {
                    "name": "三叶草",
                    "color": "#3b7b1e",
                    "filename": "24",
                    "defaultOpacity": "75",
                    "dataindex": "24",
                    "isNew": "off"
                }
                ,                {
                    "name": "在路上",
                    "color": "#343659",
                    "filename": "19",
                    "defaultOpacity": "60",
                    "dataindex": "19",
                    "isNew": "off"
                }
                ,                {
                    "name": "白色飞羽",
                    "color": "#132702",
                    "filename": "18",
                    "defaultOpacity": "60",
                    "dataindex": "18",
                    "isNew": "off"
                }
                ,                {
                    "name": "千山雪",
                    "color": "#81b1dd",
                    "filename": "16",
                    "defaultOpacity": "65",
                    "dataindex": "16",
                    "isNew": "off"
                }
                ,                {
                    "name": "锦鲤",
                    "color": "#000000",
                    "filename": "20",
                    "defaultOpacity": "70",
                    "dataindex": "20",
                    "isNew": "off"
                }
                ,                {
                    "name": "海之梦",
                    "color": "#2f6a98",
                    "filename": "17",
                    "defaultOpacity": "65",
                    "dataindex": "17",
                    "isNew": "off"
                }
                ,                {
                    "name": "梦里水乡",
                    "color": "#121108",
                    "filename": "5",
                    "defaultOpacity": "65",
                    "dataindex": "5",
                    "isNew": "off"
                }
                ,                {
                    "name": "银汉迢迢",
                    "color": "#001720",
                    "filename": "2",
                    "defaultOpacity": "65",
                    "dataindex": "2",
                    "isNew": "off"
                }
                ,                {
                    "name": "紫色郁金香",
                    "color": "#8d0578",
                    "filename": "3",
                    "defaultOpacity": "75",
                    "dataindex": "3",
                    "isNew": "off"
                }
                ,                {
                    "name": "飞瀑如练",
                    "color": "#0b0604",
                    "filename": "4",
                    "defaultOpacity": "65",
                    "dataindex": "4",
                    "isNew": "off"
                }
                ,                {
                    "name": "原野",
                    "color": "#1d7300",
                    "filename": "10",
                    "defaultOpacity": "70",
                    "dataindex": "1",
                    "isNew": "off"
                }
                ,                {
                    "name": "长天一色",
                    "color": "#18082f",
                    "filename": "6",
                    "defaultOpacity": "65",
                    "dataindex": "6",
                    "isNew": "off"
                }
                ,                {
                    "name": "春意浓",
                    "color": "#071f45",
                    "filename": "7",
                    "defaultOpacity": "75",
                    "dataindex": "7",
                    "isNew": "off"
                }
                ,                {
                    "name": "暮色四合",
                    "color": "#2a131b",
                    "filename": "8",
                    "defaultOpacity": "65",
                    "dataindex": "8",
                    "isNew": "off"
                }
                ,                {
                    "name": "出水芙蓉",
                    "color": "#358102",
                    "filename": "9",
                    "defaultOpacity": "75",
                    "dataindex": "9",
                    "isNew": "off"
                }
                ,                {
                    "name": "壁立千仞",
                    "color": "#5f220f",
                    "filename": "1",
                    "defaultOpacity": "70",
                    "dataindex": "10",
                    "isNew": "off"
                }
                ,                {
                    "name": "廊桥遗梦",
                    "color": "#111488",
                    "filename": "11",
                    "defaultOpacity": "70",
                    "dataindex": "11",
                    "isNew": "off"
                }
                ,                {
                    "name": "寥落星河",
                    "color": "#010a0e",
                    "filename": "12",
                    "defaultOpacity": "60",
                    "dataindex": "12",
                    "isNew": "off"
                }
                ,                {
                    "name": "层林尽染",
                    "color": "#4e1a04",
                    "filename": "13",
                    "defaultOpacity": "75",
                    "dataindex": "13",
                    "isNew": "off"
                }
                ,                {
                    "name": "晨曦",
                    "color": "#1f1f42",
                    "filename": "14",
                    "defaultOpacity": "65",
                    "dataindex": "14",
                    "isNew": "off"
                }
                ,                {
                    "name": "早梅争春",
                    "color": "#6c401f",
                    "filename": "15",
                    "defaultOpacity": "75",
                    "dataindex": "15",
                    "isNew": "off"
                }
                        ]
    </textarea><textarea id="s_skin_custom" style='display:none;'>
                    {   "21":    "80"   , "22":    "65"   , "23":    "75"   , "24":    "75"   , "19":    "60"   , "18":    "60"   , "16":    "65"   , "20":    "70"   , "17":    "65"   , "5":    "65"   , "2":    "65"   , "3":    "75"   , "4":    "65"   , "10":    "70"   , "6":    "65"   , "7":    "75"   , "8":    "65"   , "9":    "75"   , "1":    "70"   , "11":    "70"   , "12":    "60"   , "13":    "75"   , "14":    "65"   , "15":    "75"   }   
    </textarea></div><div id=bottom_container class="bottom bottom_ct1"><div id=s_seth><a onclick="this.style.behavior='url(#default#homepage)';this.setHomePage('http://www.baidu.com/');_onS_sethClick();return false;" href="#">把百度设为主页</a></div> <div id=s_bottom_prline1 class=bottom-line1 style="padding-bottom: 9px;"><a href=http://e.baidu.com/?refer=888>加入百度推广</a> | <a href=http://top.baidu.com>搜索风云榜</a> | <a href=http://home.baidu.com>关于百度</a> | <a href=http://ir.baidu.com>About Baidu</a> | <a href=http://www.baidu.com/home/p/open target=_blank>加入开放首页</a></div><div class=bottom-line2>&#169;2013 Baidu <a href=/duty/>使用百度前必读</a> <span>京ICP证030173号</span> <em class=s-bottom-copyright>&nbsp;&nbsp;&nbsp;&nbsp;</em></div></div></div><div id=s_tips class=tip></div><div id=s_menu class=s-menu style="display:none;"><div class=s-menu-inner></div></div><input type=hidden id=bsToken name=bsToken value="10e60fc87f079e081a4163930ca17985"><script>
    var s_domain={"staticUrl":"http://su.bdimg.com/","base":"home","baseuri":"/home","passconf":"http://passport.baidu.com/ubrwsbas","logout":"https://passport.baidu.com/?logout&u=","bs":"http://www.baidu.com","login":"http://passport.baidu.com/?login&tpl=super&u=","sp":"http://hi.baidu.com/"},s_session={"logId":"2461526988","seqId":"0xf81cb0d006605daa","debug":false,"portrait":"d3ce657a696f7275616e4d2f","userProp":{"sawVideoGuide":false,"navClean":true,"appOffline":true,"toResGuide":true,"editNavGuide":true,"backToIndexGuide":true,"customAddGuide":true,"customAddTipGuide":true,"resciteGuide":true,"resvideoGuide":true,"emptyNavGuide":true,"resreadGuide":true,"nplusGuide":true,"nplusToEditGuide":true,"nplusSortGuide":true,"nplusViewChoice":true,"nplusViewChoosed":true,"newResFuncGuide":true,"isNplus":false,"nplusExchangeGuide":true,"resGoodMusicGuide":false,"appendVideo":false,"resTiebaGuide":true,"isPhotoAlbum":false,"packRecGuide":true,"packAddMoreGuide":true,"searchAgroupGuide":false,"toNplusGuide":false},"userTips":{"rpUpdateGuide":true,"rpUpdatePack":true,"ncrGuide":false,"hideIndexLink":true,"ipadLastAccess":true,"navRecommendGuide":true,"bdKuaiJieGuide":true,"tbEncourageGuide":false,"commTab":false,"currentWebTab":"myweb","rpShowNewNavGuide":true,"resFirstAddGuide":true,"navMywebTip":true,"blowBirthday":true,"packCloseGuide":true,"isNewVersion":false,"showFmSearchGuide":true,"tbEncourageEndGuide":true,"shopingBannerGuide":true,"shopingBirdGuide":true,"shopingBirdDailyGuide":true,"shopingDefaultGuide":false,"browserPluginGuide":false,"addFromPsGuide":false,"tiebaStarPkGuide":false,"isCustomDir":false,"customFirstGuide":true,"customSecondGuide":true,"customThirdGuide":true,"rpIndividualGuide":false,"rpIndividualContentGuide":false,"nplusClean":true,"nplusCleanKey":true,"recommendGuide":true,"addToBaiduSideGuide":true,"addToBaiduBannerGuide":true,"noManualNavsGuide":"0_1357089117","msgVideoKey":false,"msgNbaKey":false,"msgLotteryKey":false,"msgStateKey":true,"msgModKey":true,"msgGuideKey":true,"msgFirstSeeKey":false,"msgHeadTipKey":true,"telephoneOpen":true,"telephoneNewYearGuide":true,"telephoneValentineGuide":true,"emptyUserGuide":"7","emptyHotNavsAdded":true,"newUserHotGuide":"3","addLayerDelTip":true,"hotChangeTip":false,"autoClassifyGuide":false,"navClfTipAdd":true,"navClfTipEdit":true,"newWeatherUser":false,"newWeatherGuide":false,"navAddHighLightTip":true,"msgCslTipKey":true,"msgCslKey":false,"msgGuoanKey":false,"msgBCKey":false,"msgFocusKey":true,"msgLocalKey":true,"footStateKey":false,"msgSetTipKey":true,"tiebaLikeGuide":true,"msgAddFocusKey":true,"navNoClickClean":false,"emptyUserFirTime":"1366163562","msgSnsTipKey":true,"topModKey":true,"msgGameKey":false,"msgGameCtrlKey":false,"skinGuide":true,"skinLogoGuide":true,"skinLogoBackGuide":true,"skinChangeToFes":false,"msgModuleTip":true,"skinUpdateGuide":true,"bxUrFirst":true,"treasureUserGuide":true,"skinLogoHasSkined":false,"msgWeiboRebindKey":false,"skinAjustGuide":true,"newsGuideTip":true,"isNavUsed":true,"navUsedTip":true,"navUsedUpdateTip":false,"navUsedDelTip":true,"skinNewPicGuide":true,"newsIdioTip":true,"msgTagKey":true,"news2GuideTip":true},"userAttr":Number("0")|| 0,"username":"ezioruan","unametype":"1","userIsSkined":"off","userIsNewSkined":"off","userSkinName":"0","userLogoSrc":"http:\/\/www.baidu.com\/img\/bdlogo.gif","usertype":"0","userFirst":"","logoCode":false,"isFesLogo":false,"userNavEmpty":"0","bgUNE":"","isEmptyRpRec":"1","userBirthday":"","modules":["0","1","7"],"modules_load":["0","1","7"]};
    </script><script src="http://su.bdimg.com/static/superpage/js/sbase_c07375db.js"></script><script src="http://su.bdimg.com/static/pack/js/config_91f44401.js"></script><script src="http://su.bdimg.com/static/nav/js/min_nav_896b77f8.js"></script><script src="http://su.bdimg.com/static/msg/js/min_mt_03c3d694.js"></script><script src="http://su.bdimg.com/static/skin/js/config_1bbf1b08.js"></script><script src="http://su.bdimg.com/static/superpage/js/min_index_924e4250.js"></script><script>
    baidu.g("kw")&&F.call('page/analyse', 'runSpeedTest');
    function ns_c(){};
    setTimeout(function(){if(document.getElementById("s_main").offsetWidth==0 && typeof(F)=='undefined'){new Image().src=s_domain.baseuri+'/page/data/pageserver?errno=2015&msg=cdn_failed'}},2000);
    </script>
    """
    
    
    s.capture_content(content, 'baidu.png',300,300)






