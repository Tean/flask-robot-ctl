function Pagination(ul_div, pagesize) {
    this._handlers = [];
    this.size = pagesize;
    this.index = 1;
    this.pages = 10;
    this.f_url = '';
    this.render = function (callback) {
        if (!this._handlers) {
            this._handlers = [];
        }
        this._handlers.push(callback);
        return callback;
    }

    this.unrender = function () {
        for (let i = 0; i < this._handlers.length; i++) {
            this._handlers[i] = null;
        }
        this._handlers.length = 0;
    };

    this.emit = function (event) {
        if (this._handlers) {
            var __handlers = this._handlers;
            for (var i = 0; i < __handlers.length; i++) {
                __handlers[i](event);
            }
        }
    };

    this.navi_to = function (index, size) {
        console.log(this.f_url);
        var pthis = this;
        console.log("f_url:" + this.f_url + ":" + index);
        var req_url = this.f_url.replace('<index>', index);
        console.log(req_url);
        req_url = req_url.replace('<size>', size);
        console.log(req_url);
        $.get({
            url: req_url,
            context: ul_div,
            success: function (e) {
                pthis.emit({
                    'udiv': $(this),
                    'json': e
                });
                $(this).append($('<div>'));
            }
        })
    }

    this.re_paginate = function (i, p) {
        this.index = i;
        this.pages = p;
    }

    this.format_url = function (format_url) {
        this.f_url = format_url;
    }

}