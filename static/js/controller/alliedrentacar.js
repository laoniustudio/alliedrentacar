/**
 * Created by sun on 7/18/2017.
 */

var alliedApp = angular.module('allied',['ngMaterial','ngMessages']);


//main controller
alliedApp.controller("alliedController",function ($scope,$http,$filter) {

            // get func
            $http.get("/api/get")
                .then(function (response) {
                    $scope.posts = response.data;

                });
            // // post func
            //  var data = $.param({
            //     fName: $scope.firstName,
            //     lName: $scope.lastName
            // });
            //
            // var config = {
            //     headers : {ww
            //         'Content-Type': 'application/x-www-form-urlencoded;charset=utf-8;'
            //     }
            // }
            //
            // $http.post('/ServerRequest/PostDataResponse', data, config)
            // .success(function (data, status, headers, config) {
            //     $scope.PostDataResponse = data;
            // })

            /**
             * filter
             */

            //date picker
            $scope.changeInOut = function(status) {
                $scope.searchDate = {};
                if(status === "Date out"){
                    $scope.searchStatus = "dateOutTime"
                }else{
                    $scope.searchStatus = "dateInTime"
                }
            }
            $scope.changeStatus = function(status) {
                if(status === "All"){
                    $scope.searchText = {};
                }else{
                    $scope.searchText = status
                }
                console.log($scope.searchText);
            }
            //convert Mon Jul 24 2017 00:00:00 GMT-0700 (Pacific Daylight Time) to normal date
            $scope.convertDate = function(selection) {
                $scope.searchDate[$scope.searchStatus] = $filter('date')(selection, "MM/dd/yyyy");
            }

});

