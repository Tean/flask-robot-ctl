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
})();

console.log(ex.make())