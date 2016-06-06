blankApp.service('Auth', ['$http', '$localStorage', 'urls', '$q', function ($http, $localStorage, urls, $q) {
    self = this;
    
    
   
   self.signin = function (data, success) {
        return $http.post(urls.BASE + '/rest-auth/login/', data)
            .then(function (response) {
                
               success(response.data);
                
            }, function (response) {
                return $q.reject(response.data)
            });

    };

    self.signout = function (success) {
        return $http.post(urls.BASE + '/rest-auth/logout/')
            .then(function (response) {
                if (typeof response.data === 'object') {
                    $localStorage.token = null;
                    success(response.data);
                } else {
                    return $q.reject(response.data)
                }
            }, function (response) {
                return $q.reject(response.data)
            });

    };
    
    self.signup = function (data) {
        return $http.post(urls.BASE + '/rest-auth/registration/', data)
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
    
}]);
