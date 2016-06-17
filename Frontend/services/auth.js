blankApp.service('Auth', ['$http', '$localStorage', 'urls', '$q', function ($http, $localStorage, urls, $q) {
    self = this;
    self.logged_in = false;
    
    self.is_logged_in = function() {
        return self.logged_in;
    };
   
   self.signin = function (data) {
        return $http.post(urls.BASE + '/rest-auth/login/', data)
            .then(function (response) {
                self.logged_in = true;
               return response.data;
                
            }, function (response) {
                return $q.reject(response.data)
            });

    };
    
    
    self.signout = function () {
        return $http.post(urls.BASE + '/rest-auth/logout/')
            .then(function (response) {
                if (typeof response.data === 'object') {
                    $localStorage.token = null;
                    self.logged_in = false;
                    return response.data;
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
