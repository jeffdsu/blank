blankApp.service('momentService', ['$http', '$localStorage', 'urls', '$q', function ($http, $localStorage, urls, $q) {
    self = this;
    self.id = null;
    self.insights = null;
    self.new_moment = Object();
    
    
    self.get_collection = function (id) {
        
        return $http.get(urls.BASE + "/inspiration-corner/moments")
            .then(function (response) {
                return response.data
            }, function (response) {
                return $q.reject(response.data)
            });

    }

    self.get = function (id) {
        
        return $http.get(urls.BASE + "/inspiration-corner/moments/" + id)
            .then(function (response) {
                return response.data
            }, function (response) {
                return $q.reject(response.data)
            });

    }
    
    self.create = function (moment) {
        
        return $http.post(urls.BASE + "/inspiration-corner/moments", moment)
            .then(function (response) {
                return response.data
            }, function (response) {
                return $q.reject(response.data)
            });

    }
    
    self.update = function (moment) {
        
        return $http.put(urls.BASE + "/inspiration-corner/moments/" + moment.id, moment)
            .then(function (response) {
                return response.data
            }, function (response) {
                return $q.reject(response.data)
            });

    }

}]);