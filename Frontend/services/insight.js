blankApp.service('insightService', ['$http', '$localStorage', 'urls', '$q', function ($http, $localStorage, urls, $q) {
    self = this;
    self.id = null;
    self.insights = null;
    
    self.isKeyword = function(word){
        console.log(word);
        return word;
    }
}]);