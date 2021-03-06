/**
 * Created by WMW on 14-8-25.
 */

$(document).ready(function(){

    var myDate = new Date();
    var selectyear = myDate.getFullYear();
    var selectmonth = myDate.getMonth()+1;
    var selectyearmonth = selectyear+"年"+selectmonth + "月";
    $("#yearmonth_id").text(selectyearmonth);
    showhideday(selectyear,selectmonth);
    Judge_week(selectyear,selectmonth);

    $("#left_select").click(function(){

        if(selectmonth>1)
          selectmonth--;
        else{
          selectmonth = 12;
          selectyear--;
        }

        selectyearmonth = selectyear+"年"+selectmonth + "月";
        $("#yearmonth_id").text(selectyearmonth);
        showhideday(selectyear,selectmonth);
        Judge_week(selectyear,selectmonth);

    });

    $("#right_select").click(function(){

        if(selectmonth<12)
          selectmonth++;
        else{
          selectmonth = 1;
          selectyear++;
        }

        selectyearmonth = selectyear+"年"+selectmonth + "月";
        $("#yearmonth_id").text(selectyearmonth);
        showhideday(selectyear,selectmonth);
        Judge_week(selectyear,selectmonth);

    });

    for(var i=1;i<=31;i++){
        $("#day"+i).click(function(){
            var id = this.id.substr(3);
            var time = selectyear+"年" + selectmonth + "月" + id + "日";
            if(selectmonth < 10){
                selectmonthM = '0' + selectmonth;
            }
            if (id < 10){
                var day = selectyear+"-"+selectmonthM+"-0"+id;
            }
            else{
                var day = selectyear+"-"+selectmonthM+"-"+id;
            }

            //这里填写你要进行的操作
            $("#everydaylist").data('day',day);
            $("#msBox_record").load("/enrich/milestone_history_msBox_record?select_day="+day);
        })
    }

  });


//判断每个月多少天，显示和隐藏不需要的号
function showhideday(year,month){

    if(month==1||month==3||month==5||month==7||month==8||month==10||month==12){
        $("#day29").show();
        $("#day30").show();
        $("#day31").show();
    }
    //将只有30天的月份的31号隐藏
    if(month==4||month==6||month==9||month==11){
      $("#day29").show();
      $("#day30").show();
      $("#day31").hide();
    }
    //如果是二月，需要判断是否是闰年
    if(month==2){
        //如果是闰年
        if((year%100!=0 &&year%4==0)||year%100==0&&year%400==0){
          $("#day29").show();
          $("#day30").hide();
          $("#day31").hide();
        }
        else{
          $("#day29").hide();
          $("#day30").hide();
          $("#day31").hide();
        }
    }
}


//判断星期六，星期天
function Judge_week(year,month){
      for(var i=1;i<=31;i++){
        var dt = new Date(year,month-1, i);
        var week = dt.getDay();
        //0或6表示周日和周六，然后改变颜色
        if(week==0||week==6){
            $("#day"+i).css({"background":"#58d68d"});
        }
        else
        $("#day"+i).css({"background":"#cccccc"});
      }
}
