blankApp.controller('adminMediaController', ['$scope', '$resource', '$routeParams', '$http', 'mediaService', 'contributorService', 'mediumTypeService', function ($scope, $resource, $routeParams, $http, mediaService, contributorService, mediumTypeService) {
    
    contributorService.get_collection()
    .then(function(data){
        $scope.authors = data;
    }, function(err){});
    
    mediumTypeService.get_collection()
    .then(function(data){
        $scope.medium_types = data;
    }, function(err){});

    $scope.add_medium = function (medium) {
        mediaService.create(medium).then(function(data) {
            
        }, function (err){})
    }
}]);