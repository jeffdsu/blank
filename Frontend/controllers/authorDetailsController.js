blankApp.controller('authorDetailsController', ['$scope', '$resource', '$routeParams', '$http', '$interval', 'authorService', function ($scope, $resource, $routeParams, $http, $interval, authorService) {
    
    self = this;
    console.log("asdfasd");
    authorId = $routeParams.authorId;
        
     authorService.get(authorId)
        .then(function (data) {
                $scope.author = data;
            }
            , function (err) {

            }
        );
    
    authorService.get_books(authorId)
    .then(function (data) {
                $scope.books = data;
            }
            , function (err) {

            }
        );

    
}]);
