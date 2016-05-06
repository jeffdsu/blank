blankApp.controller('adminBooksController', ['$scope', '$resource', '$routeParams', '$http', 'bookService', 'authorService', function ($scope, $resource, $routeParams, $http, bookService, authorService) {
    
    authorService.get_collection()
    .then(function(data){
        $scope.authors = data;
    }, function(err){});
    


}]);