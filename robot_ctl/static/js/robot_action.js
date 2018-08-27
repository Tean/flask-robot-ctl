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

    exp.makePageFoot = function(current, pages) {
        var foot = $('.pagefoot');
        foot.empty();
        //first
        var first = $('<div class="first">')
        first.append('<span>首页</span>');
        foot.append(first);
        //prev
        var prev = $('<div class="prev">')
        if(current > 1) {
            prev.append('<a href="javascript:ex.makePageFoot('+(current-1)+','+pages+')">上一页</a>');
        }else{
            prev.append('<span>上一页</span>') ;
        }
        foot.append(prev);

        if(pages>5){
            var displayPN = 3
            if(current>displayPN) {
                var pageNoBlock = $('<div class="pageNoBlock">')
                var pageSpan = $('<span>');
                pageSpan.text('.');
                pageNoBlock.append(pageSpan);
                foot.append(pageNoBlock);
            }
            var prevPN = 1;
            if(current >= pages)
                prevPN = 2;
            var nextPN=1;
            if(current <=0)
                nextPN=2;
            for(var i=current-prevPN;i<current+prevPN;i++) {
                if(i>0 && i<=pages) {
                    var pageNoBlock = $('<div class="pageNoBlock">');
                    var pageSpan = $('<span>');
                    if(current == i){
                        pageSpan = $('<a href="#">'+i+'/</a>');
                    }else{
                        pageSpan.text(i+'/');
                    }
                    pageNoBlock.append(pageSpan);
                    foot.append(pageNoBlock);
                }
            }

            if(current>pages-displayPN) {
                var pageNoBlock = $('<div class="pageNoBlock">')
                var pageSpan = $('<span>');
                pageSpan.text('.');
                pageNoBlock.append(pageSpan);
                foot.append(pageNoBlock);
            }
        }else{
            for(var i=1;i<=pages;i++) {
                var pageNoBlock = $('<div class="pageNoBlock">')
                var pageSpan = $('<span>');
                pageSpan.text(i);
                pageNoBlock.append(pageSpan);
                foot.append(pageNoBlock);
            }
        }

        //next
        var next = $('<div class="next">');
        console.log(current);
        if(current < pages) {
            next.append('<a href="javascript:ex.makePageFoot('+(current+1)+','+pages+')">下一页</a>');
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

ex.makePageFoot(1,10);
console.log(ex.make())