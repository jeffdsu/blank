blankApp.controller('signUpContr2oller', ['urls', '$rootScope', '$scope', '$resource', '$routeParams', '$http', '$localStorage', '$location', 'Auth', function (urls, $rootScope, $scope, $resource, $routeParams, $http, $localStorage, $location, Auth) {


    $scope.signin = function () {

        var formData = {
            username: $scope.username
            , password: $scope.password
        };

        Auth.signin(formData, successAuth, function () {
            $rootScope.error = 'Invalid credentials.';
        })
    };
    
    $scope.signup = function () {
        
    }

    

}]);