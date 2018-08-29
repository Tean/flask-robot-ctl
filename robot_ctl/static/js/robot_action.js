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
    var makePageHtml = function (text, pgnid, pageindex, pagesize, disabled = false, active = false) {
        var link = $('<a class="btn" href="javascript:ex.to(\'' + pgnid + '\',' + pageindex + ',' + pagesize + ');">').text(text);
        var li = $('<li>').append(link);
        if (disabled) {
            if (!active)
                li.addClass('disabled');
            link.addClass('disabled');
            link.prop('disabled', true);
        }
        if (active)
            li.addClass('active')
        return li;
    };
    var makePageHtmlSpan = function (text, disabled = true) {
        var link = $('<a class="btn" href="#">').text(text);
        var li = $('<li>').append(link);
        if (disabled) {
            li.addClass('disabled');
            link.addClass('disabled');
            link.prop('disabled', true);
        }
        return li;
    };
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
                var li = $('<li class="QQli">');
                li.attr('data-id', item.id);
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

            if (pages > 7) {
                if (index > 1) {
                    var elem = makePageHtml('1', pgnid, 1, pgn.size, index <= 1);
                    footer.append(elem);
                }

                if ((index > 3 && index < pages) || index > 3) {
                    var elem = makePageHtmlSpan('...');
                    footer.append(elem);
                }

                if (index > pages - 1) {
                    var to = index - 4;
                    var elem = makePageHtml(to + '', pgnid, to, pgn.size, index <= 1);
                    footer.append(elem);
                }

                if (index > pages - 2) {
                    var to = index - 3;
                    var elem = makePageHtml(to + '', pgnid, to, pgn.size, index <= 1);
                    footer.append(elem);
                }

                if (index > pages - 3) {
                    var to = index - 2;
                    var elem = makePageHtml(to + '', pgnid, to, pgn.size, index <= 1);
                    footer.append(elem);
                }

                if (index > 2) {
                    var to = index - 1;
                    var elem = makePageHtml(to + '', pgnid, to, pgn.size, index <= 1);
                    footer.append(elem);
                }

                var elem = makePageHtml(index + '', pgnid, index, pgn.size, true, true);
                footer.append(elem);

                if (index < pages - 1) {
                    var to = index + 1;
                    var elem = makePageHtml(to + '', pgnid, to, pgn.size, index >= pages);
                    footer.append(elem);
                }

                if (index < 4) {
                    var to = index + 2;
                    var elem = makePageHtml(to + '', pgnid, to, pgn.size, index >= pages);
                    footer.append(elem);
                }

                if (index < 3) {
                    var to = index + 3;
                    var elem = makePageHtml(to + '', pgnid, to, pgn.size, index >= pages);
                    footer.append(elem);
                }

                if (index < 2) {
                    var to = index + 4;
                    var elem = makePageHtml(to + '', pgnid, to, pgn.size, index >= pages);
                    footer.append(elem);
                }

                if ((index < pages - 2 && index > 1) || pages > index + 3) {
                    var elem = makePageHtmlSpan('...');
                    footer.append(elem);
                }

                if (index < pages) {
                    var to = pages;
                    var elem = makePageHtml(to + '', pgnid, to, pgn.size, index >= pages);
                    footer.append(elem);
                }
            } else {
                for (var i = 1; i <= pages; i++) {
                    var to = i;
                    if (i == index) {
                        var elem = makePageHtml(to + '', pgnid, to, pgn.size, false, true);
                        footer.append(elem);
                    } else {
                        var elem = makePageHtml(to + '', pgnid, to, pgn.size, false);
                        footer.append(elem);
                    }
                }
            }

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
                var li = $('<li class="QQli">');
                li.attr('data-id', item.id);
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

            if (pages > 7) {
                if (index > 1) {
                    var elem = makePageHtml('1', pgnid, 1, pgn.size, index <= 1);
                    footer.append(elem);
                }

                if ((index > 3 && index < pages) || index > 3) {
                    var elem = makePageHtmlSpan('...');
                    footer.append(elem);
                }

                if (index > pages - 1) {
                    var to = index - 4;
                    var elem = makePageHtml(to + '', pgnid, to, pgn.size, index <= 1);
                    footer.append(elem);
                }

                if (index > pages - 2) {
                    var to = index - 3;
                    var elem = makePageHtml(to + '', pgnid, to, pgn.size, index <= 1);
                    footer.append(elem);
                }

                if (index > pages - 3) {
                    var to = index - 2;
                    var elem = makePageHtml(to + '', pgnid, to, pgn.size, index <= 1);
                    footer.append(elem);
                }

                if (index > 2) {
                    var to = index - 1;
                    var elem = makePageHtml(to + '', pgnid, to, pgn.size, index <= 1);
                    footer.append(elem);
                }

                var elem = makePageHtml(index + '', pgnid, index, pgn.size, true, true);
                footer.append(elem);

                if (index < pages - 1) {
                    var to = index + 1;
                    var elem = makePageHtml(to + '', pgnid, to, pgn.size, index >= pages);
                    footer.append(elem);
                }

                if (index < 4) {
                    var to = index + 2;
                    var elem = makePageHtml(to + '', pgnid, to, pgn.size, index >= pages);
                    footer.append(elem);
                }

                if (index < 3) {
                    var to = index + 3;
                    var elem = makePageHtml(to + '', pgnid, to, pgn.size, index >= pages);
                    footer.append(elem);
                }

                if (index < 2) {
                    var to = index + 4;
                    var elem = makePageHtml(to + '', pgnid, to, pgn.size, index >= pages);
                    footer.append(elem);
                }

                if ((index < pages - 2 && index > 1) || pages > index + 3) {
                    var elem = makePageHtmlSpan('...');
                    footer.append(elem);
                }

                if (index < pages) {
                    var to = pages;
                    var elem = makePageHtml(to + '', pgnid, to, pgn.size, index >= pages);
                    footer.append(elem);
                }
            } else {
                for (var i = 1; i <= pages; i++) {
                    var to = i;
                    if (i == index) {
                        var elem = makePageHtml(to + '', pgnid, to, pgn.size, index >= pages, true);
                        footer.append(elem);
                    } else {
                        var elem = makePageHtml(to + '', pgnid, to, pgn.size, index >= pages);
                        footer.append(elem);
                    }
                }
            }

            ul_div.append(footer);
        });
});
console.log(ex.make())