blankApp.service('insightService', ['$http', '$localStorage', 'urls', '$q', function ($http, $localStorage, urls, $q) {
    self = this;
    self.id = null;
    self.insights = null;


    self.get_collection = function () {
        return $http.get(urls.BASE + "/inspiration-corner/insights")
            .then(function (response) {
                if (typeof response.data === 'object') {
                    return response.data
                } else {
                    return $q.reject(response.data)
                }
            }, function (response) {
                return $q.reject(response.data)
            });

    };

    self.isKeyword = function (word) {
        console.log(word);
        return word;
    }

    self.validate = function (id) {
        return $http.put(urls.BASE + "/inspiration-corner/admin/insights/" + id + "/validate")
            .then(function (response) {
                return response.data
            }, function (response) {
                return $q.reject(response.data)
            });

    }
    
    self.validate = function (id) {
        return $http.put(urls.BASE + "/inspiration-corner/admin/insights/" + id + "/validate")
            .then(function (response) {
                return response.data
            }, function (response) {
                return $q.reject(response.data)
            });

    }
    


}]);

blankApp.service('personalInsightSerivce', ['$http', '$localStorage', 'urls', '$q', function ($http, $localStorage, urls, $q) {
    self = this;
    self.id = null;
    self.insights = null;

    self.create = function (insight) {
        
        insight.personal = true;
        
        return $http.post(urls.BASE + "/inspiration-corner/insights", insight)
            .then(function (response) {
                return response.data
            }, function (response) {
                return $q.reject(response.data)
            });

    }

}]);