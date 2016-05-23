blankApp.controller('contributorsController', ['$scope', '$resource', '$routeParams', '$http', '$interval', 'authorService', function ($scope, $resource, $routeParams, $http, $interval, authorService) {
    
     authorService.get_collection()
        .then(function (data) {
                $scope.authors = data;
            }
            , function (err) {

            }
        );

    
}]);
