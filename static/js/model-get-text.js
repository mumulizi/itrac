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
     //����2.2.13
     //10+2+2   ��
     //14+8     ��
     //
     //����  ���� ��ˮ
     //����  ���� ������ľ
     //����  ���� �ҽ�ˮ
     //����  ���� ���Կ���
     //
     //
     //
     //14/8 6        ����
     //δʱ 8        ����
     //14+8=22/6=4   ����
     //
     //���ԣ����� ��ˮ����
     //���ԣ����� ��������
     //���ԣ����� �ҽ�����
     //
     //���ԣ����� ���ԣ�����
     //����ã�����ˮ��


     //var last_value123 = value.eq(0).text()
     //console.log(last_value123)
  })
});