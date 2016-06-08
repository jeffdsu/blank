blankApp.controller('adminContributorController', ['$scope', '$resource', '$routeParams', '$http', 'mediaService', 'contributorService', 'mediumTypeService', function ($scope, $resource, $routeParams, $http, mediaService, contributorService, mediumTypeService) {
    
    contributorService.create()
    .then(function(data){
        $scope.authors = data;
    }, function(err){});
    
}]);