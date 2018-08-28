(function(){
    var exp={};
    var name="x";
    exp.make=function(){
        return name;
    };
    window.ex=exp;

    exp.logout = function () {
        window.location.href = '/logout';
    }

    exp.makePageFoot = function(current, pages, pageVars) {
        if(pageVars==null) {
            pageVars=[];
            for(var i=0;i<pages;i++)
                pageVars.push(i);
        }
        var foot = $('.pagefoot');
        foot.empty();
        //first
        var first = $('<div class="first">')
        first.append('<span>首页</span>');
        foot.append(first);
        //prev
        var prev = $('<div class="prev">')
        if(current > 1) {
            prev.append('<a href="javascript:ex.last()">上一页</a>');
        }else{
            prev.append('<span>上一页</span>') ;
        }
        foot.append(prev);

        for(var i=1;i<=pages;i++) {
            var pageNoBlock = $('<div class="pageNoBlock">')
            var pageSpan = $('<span>');
            pageSpan.text(pageVars[i]);
            pageNoBlock.append(pageSpan);
            foot.append(pageNoBlock);
        }

        //next
        var next = $('<div class="next">');
        console.log(current);
        if(current < pages) {
            next.append('<a href="javascript:ex.next()">下一页</a>');
        }else{
            next.append('<span>下一页</span>') ;
        }
        foot.append(next);
        //last
        var last = $('<div class="last">')
        last.append('<span>末页</span>');
        foot.append(last);
    }
})();

$(document).ready(function() {
    ex.makePageFoot(1,10,['a','b','c','d','e','f','g','h','i','j']);
    var pgn = new Pagination($('#qqpage'),10);
    pgn.render(function(event){
        var ul_div = event.udiv;
        ul_div.empty();
        var ul = $('<ul class="nop QQul">');
        var index = event.json.index;
        var pages = event.json.pages;
        var items = event.json.items;

        items.forEach(item => {
            var li = $('<li id="'+item.id+'" class="QQli">');
            var QQicon = $('<div class="QQicon">');
            li.append(QQicon);
            var QQNo = $('<div class="QQNo">');
            QQNo.text(item.qq_no);
            li.append(QQNo);
            console.log(JSON.stringify(item));
            ul.append(li);
        });
        ul_div.append(ul);
    });
    pgn.navi_to('/api/qq/page/2?size='+pgn.size);
});
console.log(ex.make())