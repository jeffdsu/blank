blankApp.service('momentService', ['$http', '$localStorage', 'urls', '$q', function ($http, $localStorage, urls, $q) {
    self = this;
    self.id = null;
    self.insights = null;

    self.create = function (moment) {
        
        return $http.post(urls.BASE + "/inspiration-corner/moments", moment)
            .then(function (response) {
                return response.data
            }, function (response) {
                return $q.reject(response.data)
            });

    }

}]);