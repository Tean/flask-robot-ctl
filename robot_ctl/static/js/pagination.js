function Pagination(ul_div,pagesize) {
    this._handlers = [];
    this.size = pagesize;
    this.render = function(callback) {
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

    this.navi_to=function(req_url) {
        var pthis = this;
        $.get({url:req_url,context:ul_div,success:function(e){
            console.log(e);
            pthis.emit({'udiv':$(this),'json':e});
            $(this).append($('<div>'));
        }})
    }

}