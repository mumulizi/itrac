/**
 * Created by Administrator on 2018/1/31.
 */
$(document).ready(function() {
 $(".model-button").click(function() {
    var value = $(this).parent().children();

     $('#inputid').val(value.eq(0).text());
     $('#inputhostname').val(value.eq(1).text());
     $('#inputipaddress').val(value.eq(2).text());
     $('#inputproblemuser').val(value.eq(3).text());
     $('#inputproblemtime').val(value.eq(4).text());
     $('#inputissue').val(value.eq(5).text().trim());
     $('#inputresolve').val(value.eq(6).text().trim());

     //for (var i=0;i<8;i++){
     //    var last_value1 = "td" +i + ":"
     //    var last_value = value.eq(i).text()
     //    console.log(last_value)
     //}
     //¶¡ÓÏ2.2.13
     //10+2+2   ¿²
     //14+8     ¿²
     //
     //Ö÷ØÔ  ¿²ØÔ ÊôË®
     //»¥ØÔ  ÒÃØÔ ôÞÍÁÕðÄ¾
     //±äØÔ  À§ØÔ ¶Ò½ð¿²Ë®
     //ÌåØÔ  ¿²ØÔ ÓÃØÔ¿²ØÔ
     //
     //
     //
     //14/8 6        ¿²ØÔ
     //Î´Ê± 8        À¤ØÔ
     //14+8=22/6=4   ¶ÒØÔ
     //
     //Ö÷ØÔ£º±ÈØÔ ¿²Ë®À¤ÍÁ
     //»¥ØÔ£º°þØÔ ôÞÍÁÀ¤ÍÁ
     //±äØÔ£ºÝÍØÔ ¶Ò½ðÀ¤ÍÁ
     //
     //ÌåØÔ£ºÀ¤ØÔ ÓÃØÔ£º¿²ØÔ
     //Ìå¿ËÓÃ£¬ÍÁ¿ËË®£¬


     //var last_value123 = value.eq(0).text()
     //console.log(last_value123)
  })
});