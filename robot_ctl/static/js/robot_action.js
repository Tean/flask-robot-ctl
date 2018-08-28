(function () {
    var exp = {};
    var name = "x";
    exp.pgn_list = {};
    exp.make = function () {
        return name;
    };
    window.ex = exp;

    exp.logout = function () {
        window.location.href = '/logout';
    }

    exp.makePageFoot = function (current, pages, pageVars) {
        if (pageVars == null) {
            pageVars = [];
            for (var i = 0; i < pages; i++)
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
        if (current > 1) {
            prev.append('<a href="javascript:ex.last()">上一页</a>');
        } else {
            prev.append('<span>上一页</span>');
        }
        foot.append(prev);

        for (var i = 1; i <= pages; i++) {
            var pageNoBlock = $('<div class="pageNoBlock">')
            var pageSpan = $('<span>');
            pageSpan.text(pageVars[i]);
            pageNoBlock.append(pageSpan);
            foot.append(pageNoBlock);
        }

        //next
        var next = $('<div class="next">');
        console.log(current);
        if (current < pages) {
            next.append('<a href="javascript:ex.next()">下一页</a>');
        } else {
            next.append('<span>下一页</span>');
        }
        foot.append(next);
        //last
        var last = $('<div class="last">')
        last.append('<span>末页</span>');
        foot.append(last);
    }

    exp.makePage = function (div, apiurlformat, renderfc) {
        var pgn = new Pagination(div, 10);
        pgn.format_url(apiurlformat);
        var pgnid = div.attr('id');
        exp.pgn_list[pgnid] = pgn;
        pgn.render(function (event) {
            renderfc(event, pgn, pgnid)
        });
        pgn.navi_to(1, pgn.size);
    }

    exp.to = function (pgnid, index, size) {
        console.log('act');
        var pgn = exp.pgn_list[pgnid];
        if (index < 1) index = 1;
        if (index > pgn.pages) index = pgn.pages;
        pgn.navi_to(index, size);
    }
})();

$(document).ready(function () {
    // ex.makePageFoot(1, 10, ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']);
    ex.makePage($('#qqpage'), '/api/qq/page/<index>?size=<size>',
        function (event, pgn, pgnid) {
            var ul_div = event.udiv;
            ul_div.empty();
            var ul = $('<ul class="nop QQul">');
            var index = event.json.index;
            var pages = event.json.pages;
            var items = event.json.items;
            pgn.re_paginate(index, pages);

            items.forEach(item => {
                var li = $('<li id="' + item.id + '" class="QQli">');
                var QQicon = $('<div class="QQicon">');
                li.append(QQicon);
                var QQNo = $('<div class="QQNo">');
                QQNo.text(item.qq_no);
                li.append(QQNo);
                // console.log(JSON.stringify(item));
                ul.append(li);
            });
            ul_div.append(ul);

            var footer = $('<ul class="pagination">');
            var prevtext = '上一页';
            var prevlink = $('<a class="btn" href="javascript:ex.to(\'' + pgnid + '\',' + (index - 1) + ',' + pgn.size + ');">').text(prevtext);
            var prev = $('<li>').append(prevlink);
            if (index <= 1) {
                prev.addClass('disabled');
                prevlink.addClass('disabled');
                prevlink.prop('disabled', true);
            }
            footer.append(prev);
            for (var i = 1; i <= pages; i++) {
                var plink = $('<a class="btn" href="javascript:ex.to(\'' + pgnid + '\',' + i + ',' + pgn.size + ');">').text(i);
                var p = $('<li>').append(plink);
                if (i == index) {
                    p.addClass('active');
                    plink.addClass('disabled');
                    plink.prop('disabled', true);
                }
                footer.append(p);
            }
            var nexttext = '下一页'
            var nextlink = $('<a class="btn" href="javascript:ex.to(\'' + pgnid + '\',' + (index + 1) + ',' + pgn.size + ');">').text(nexttext);
            var next = $('<li>').append(nextlink);
            if (index >= pages) {
                next.addClass('disabled');
                nextlink.addClass('disabled');
                nextlink.prop('disabled', true);
            }
            footer.append(next);
            ul_div.append(footer);
        });
    ex.makePage($('#wxpage'), '/api/wx/page/<index>?size=<size>',
        function (event, pgn, pgnid) {
            var ul_div = event.udiv;
            ul_div.empty();
            var ul = $('<ul class="nop QQul">');
            var index = event.json.index;
            var pages = event.json.pages;
            var items = event.json.items;
            pgn.re_paginate(index, pages);

            items.forEach(item => {
                var li = $('<li id="' + item.id + '" class="QQli">');
                var QQicon = $('<div class="QQicon">');
                li.append(QQicon);
                var QQNo = $('<div class="QQNo">');
                QQNo.text(item.wx_name);
                li.append(QQNo);
                // console.log(JSON.stringify(item));
                ul.append(li);
            });
            ul_div.append(ul);

            var footer = $('<ul class="pagination">');
            var prevtext = '上一页';
            var prevlink = $('<a class="btn" href="javascript:ex.to(\'' + pgnid + '\',' + (index - 1) + ',' + pgn.size + ');">').text(prevtext);
            var prev = $('<li>').append(prevlink);
            if (index <= 1) {
                prev.addClass('disabled');
                prevlink.addClass('disabled');
                prevlink.prop('disabled', true);
            }
            footer.append(prev);
            for (var i = 1; i <= pages; i++) {
                var plink = $('<a class="btn" href="javascript:ex.to(\'' + pgnid + '\',' + i + ',' + pgn.size + ');">').text(i);
                var p = $('<li>').append(plink);
                if (i == index) {
                    p.addClass('active');
                    plink.addClass('disabled');
                    plink.prop('disabled', true);
                }
                footer.append(p);
            }
            var nexttext = '下一页'
            var nextlink = $('<a class="btn" href="javascript:ex.to(\'' + pgnid + '\',' + (index + 1) + ',' + pgn.size + ');">').text(nexttext);
            var next = $('<li>').append(nextlink);
            if (index >= pages) {
                next.addClass('disabled');
                nextlink.addClass('disabled');
                nextlink.prop('disabled', true);
            }
            footer.append(next);
            ul_div.append(footer);
        });
});
console.log(ex.make())