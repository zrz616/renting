<template>
    <div>
        <!--头部开始-->
        <v-header></v-header>
        <!--头部结束-->
        <!--中间开始-->
        <div class="ui basic vertical segment mid_content">
            <div class="ui vertical list_content">
                <div class="ui grid">
                    <!--左边开始-->
                    <div class="four wide column shaixuan">
                        <div @click="submit" class="ui shaixuan">
                          <a style="color: #191711">筛选</a>
                        </div>
                        <div class="ui basic segment leixing">
                            <div class="ui" style="margin-left:15px;">
                                按类型 <i class="angle yellow right icon" style="margin-left:10px;"></i>
                            </div>
                            <div class="ui form" style="margin-top:15px; margin-left:15px;">
                                <div class="inline fields">
                                    <div class="field">
                                        <div class="ui radio checkbox">
                                            <input v-model="rentType" type="radio" name="frequency" value="whole">
                                            <label>整租</label>
                                        </div>
                                    </div>
                                    <div class="field">
                                        <div class="ui radio checkbox">
                                            <input v-model="rentType" type="radio" value="share" name="frequency">
                                            <label>合租</label>
                                        </div>
                                    </div>
                                    <div class="field">
                                        <div class="ui radio checkbox">
                                            <input v-model="rentType" type="radio" value="month" name="frequency">
                                            <label>月租</label>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <div class="ui basic segment leixing">
                            <div class="ui" style="margin-left:15px;">
                                按户型 <i class="angle yellow right icon" style="margin-left:10px;"></i>
                            </div>
                            <div class="ui form" style="margin-top:15px; margin-left:15px;">
                                <div class="grouped fields">
                                    <div class="field">
                                        <div class="ui checkbox">
                                        <input type="checkbox" name="example">
                                        <label>一居</label>
                                        </div>
                                    </div>
                                    <div class="field">
                                        <div class="ui checkbox">
                                            <input type="checkbox" name="example" checked="checked">
                                            <label>二居</label>
                                        </div>
                                    </div>
                                    <div class="field">
                                        <div class="ui checkbox">
                                            <input type="checkbox" name="example">
                                            <label>三居</label>
                                        </div>
                                    </div>
                                    <div class="field">
                                        <div class="ui checkbox">
                                            <input type="checkbox" name="example">
                                            <label>四居</label>
                                        </div>
                                    </div>
                                    <div class="field">
                                        <div class="ui checkbox">
                                            <input type="checkbox" name="example">
                                            <label>其他</label>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <div class="ui basic segment leixing">
                            <div class="ui" style="margin-left:15px;">
                                按价格 <i class="angle yellow right icon" style="margin-left:10px;"></i>
                            </div>
                        </div>
                        <div class="ui basic segment leixing">
                            <div class="ui" style="margin-left:15px;">
                                按设施 <i class="angle yellow right icon" style="margin-left:10px;"></i>
                            </div>
                            <div class="ui form" style="margin-top:15px; margin-left:15px;">
                                <div class="grouped fields">
                                    <div v-for="device in deviceList" class="field">
                                        <div class="ui checkbox">
                                        <input v-model="device.active" type="checkbox" name="example">
                                        <label>{{ device.device_name }}</label>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                    <!--左边结束-->
                    <!--右边开始-->

                    <div class="twelve wide column">
                        <div class="ui basic segment" style="padding-bottom:0px;">
                            <div class="ui paixu">
                                排序
                            </div>
                            <div class="ui compact menu" style="margin-top:5px;">
                              <div class="ui simple dropdown item">
                                默认排序
                                <img src="/static/image/down_icon.png" style="height:13px;width:13px; margin-left:5px;" alt="" />
                                <div class="menu">
                                  <div @click="sortedWithDistance" class="item">距离</div>
                                  <div @click="sortedWithPraise" class="item">评价</div>
                                  <div class="item">综合</div>
                                </div>
                              </div>
                            </div>
                            <div class="ui compact menu" style="margin-top:5px;margin-left:5px;">
                              <div class="ui simple dropdown item">
                                按价格
                                <img src="/static/image/down_icon.png" style="height:13px;width:13px; margin-left:5px;" alt="" />
                                <div class="menu">
                                  <div @click="sortedWithPrice" class="item">底到高</div>
                                  <div @click="reversedWithPrice" class="item">高到底</div>
                                </div>
                              </div>
                            </div>
                        </div>
                        <div class="ui divider" style="margin-top:0px; margin-left:15px;margin-right:15px;"></div>
                        <div class="ui vertical mid_img">
                            <div class="ui three column grid first1">
                                <div v-for="house in filterHouseList" class="column_image">
                                    <div class="image_mid" :style="{background: 'url(' + house.house_show_url + ')'}" style="background-position:left;background-size: cover;">
                                        <div class="ui price">
                                            <div style="color: white;font-size: 15px; position:relative;">
                                                {{ house.price }}
                                            </div>
                                        </div>
                                        <div class="ui center aligned vertical segment address">
                                            <div style="margin:2px 0 1px 0;">
                                                <a href="#"style="color:black">{{ house.address }} {{ house.rent_type }}</a>
                                            </div>
                                            <div v-for="point in house.position" style="font-size:12px; color:rgb(83, 82, 82)">
                                                <span v-if="point.school === searchSchool">
                                                  距{{ point.school }}{{ point.distance }}米
                                                </span>

                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                            <!--<v-paginate>
                              :page-count="5"
                              :click-handler="functionName"
                              :prev-text="Prev"
                              :next-text="Next"
                              :container-class="className">
                            </v-paginate>-->
                             <div class="ui vertical container segment page" style="position:relative;top:-1px;bottom:400px;">
                               <div class="ui three column grid first1">
                                    <div class="column left aligned page " style="position:relative; top:5px;">
                                        <button class="page button" type="button" name="button"><i class="angle left big icon"></i></button>
                                    </div>
                                    <div class="column page">
                                        <div @click="switchPage(page)" v-for="page in pageList" :class="{ active: isActive(page) }" class="ui button num">
                                            {{ page }}
                                        </div>
                                    </div>
                                    <div class="column right aligned page" style="position:relative; top:-1px;">
                                        <button class="page button" type="button" name="button"><i class="angle right big icon"></i></button>
                                    </div>
                                </div>
                             </div>

                        </div>
                    </div>
                </div>
            </div>
            <!--右边结束-->
        </div>
        <!--中间结束-->
    </div>

</template>

<script>
    import reqwest from 'reqwest';
    import Paginate from 'vuejs-paginate';
    import header from '../components/header/header';
    export default {
        data () {
            return {
                houseList: [1, 2, 3],
                deviceList: '',
                seleted_devices: '',
                rentType: 'whole',
                paginate: ['houseList'],
                searchSchool: '',
                pageNums: 1,
                currentPage: 0,
                pageList: []
            };
        },
        methods: {
            sortedWithDistance () {
                let self = this;
                this.houseList = this.houseList.sort((a, b) => {
                    // console.log(a.position[0].distance);
                    let indexA = 0;
                    let indexB = 0;
                    a.position.forEach((elem, index) => {
                        if (elem.school === self.searchSchool) {
                            indexA = index;
                        }
                    });
                    b.position.forEach((elem, index) => {
                        if (elem.school === self.searchSchool) {
                            indexB = index;
                        }
                    });
                    return a.position[indexA].distance - b.position[indexB].distance;
                });
                console.log(this.houseList);
            },
            sortedWithPraise () {
                this.houseList.sort((a, b) => {
                    return a.favorite_nums - b.favorite_nums;
                });
            },
            sortedWithPrice () {
                this.houseList.sort((a, b) => {
                    return a.price - b.price;
                });
            },
            reversedWithPrice () {
                this.houseList.sort((a, b) => {
                    return b.price - a.price;
                });
            },
            submit () {
                let self = this;
                let selectDevice = [];
                // 将选择的设备转换为字符串发送
                this.deviceList.forEach((elem) => {
                    if (elem.active) {
                        selectDevice.push(elem.device_name);
                    }
                });
                reqwest({
                    // TODO
                    url: 'http://127.0.0.1:8000/api/v1.0/selected_devices/',
                    type: 'json',
                    method: 'GET',
                    data: {
                        device_list: selectDevice,
                        rent_type: self.rentType
                    },
                    success (resp) {
                        console.log(resp);
                        self.houseList = resp;
                    }
                });
            },
            switchPage (page) {
                this.currentPage = page - 1;
                console.log(this.currentPage);
            },
            isActive (page) {
                return (page - 1 === this.currentPage);
            }
        },
        components: {
            'v-header': header,
            'v-paginate': Paginate
        },
        watch: {
//            currentPage () {
//                console.log(this.currentPage);
//                return this.houseList.slice((this.currentPage - 1) * 9, 9);
//            }
        },
        computed: {
            filterHouseList () {
                this.pageNums = Math.floor(this.houseList.length / 9) + 1;
                for (let index = 0; index < this.pageNums; index++) {
                    this.pageList[index] = index + 1;
                }
                console.log((this.currentPage) * 9);
                return this.houseList.slice(this.currentPage * 9, (this.currentPage + 1) * 9);
            }
        },
        mounted () {
            this.searchSchool = this.$route.params.school_name;
            let self = this;
            reqwest({
                url: 'http://127.0.0.1:8000/api/v1.0/house_cards/' + self.$route.params.school_name,
                type: 'json',
                // method默认是get
                method: 'GET',
                success (resp) {
                    console.log(resp);
                    self.houseList = resp;
                }
            });
            reqwest({
                url: 'http://127.0.0.1:8000/api/v1.0/devices',
                type: 'json',
                method: 'GET',
                success (resp) {
                    console.log(resp);
                    self.deviceList = resp;
                    self.deviceList.forEach((elem) => {
                        elem.active = false;
                    });
                }
            });
        }
    };
</script>

<!-- 加上scoped表示css只影响局部 -->
<style scoped>
    ul {
        list-style-type: none;
        padding: 0;
        text-align: center;
    }
    .number.active {
        width: 35px;
        padding-left:14px;
        background-color: #fcc416;
    }
    .ui.basic.vertical.segment.mid_content{
        width: 100%;
        height: 925px;
        position: relative;
        left:50%;
        top:220px;
        margin-bottom: 220px;
        transform: translate(-50%);
        background-color: rgb(243, 243, 243);
    }

    /*左边垂直区块*/
    .ui.vertical.list_content{
        width: 888px;
        height: 900px;
        background-color: white;
        position: absolute;
        left:50%;
        top:-40px;
        transform: translate(-50%);
        border-radius:10px;
    }

    .four.wide.column.shaixuan{
        height: 75px;
        background-color: #fcc416;
        position: relative;
        top: 14px;
        left: 14px;
        border-radius:10px 10px 0 0;
    }

    .ui.shaixuan{
        position: relative;
        top: 30%;
        left: 85%;
        transform: translate(-50%);
        font-family:Microsoft YaHei;
        font-size: 20px;
    }

    .ui.basic.segment.leixing{
        width: 227px;
        position: relative;
        top: 60%;
        left: 50%;
        transform: translate(-50%);
        font-family:Microsoft YaHei;
        font-size: 16px;
        padding: 30px 0px 0 0;
    }

    #title{
        font-family:Microsoft YaHei;
    }

    .ui.radio.checkbox input:checked ~ .box:after,
    .ui.radio.checkbox input:checked ~ label:after {
      background-color: #fcc416;
    }


    .ui.radio.checkbox input:focus:checked ~ .box:after,
    .ui.radio.checkbox input:focus:checked ~ label:after {
      background-color: #fcc416;
    }



    .ui.checkbox input:indeterminate ~ .box:after,
    .ui.checkbox input:indeterminate ~ label:after {
      opacity: 1;
      color: #fcc416;
    }

    .ui.checkbox input:checked ~ .box:after,
    .ui.checkbox input:checked ~ label:after {
      opacity: 1;
      color: #fcc416;
    }


    .ui.checkbox input:indeterminate:focus ~ .box:after,
    .ui.checkbox input:indeterminate:focus ~ label:after,
    .ui.checkbox input:checked:focus ~ .box:after,
    .ui.checkbox input:checked:focus ~ label:after {
      color: #fcc416;
    }

    /*中间区块*/
    .ui.paixu{

        width: 70px;
        line-height: 35px;
        float: left;
        margin-top: 6px;
        font-family:Microsoft YaHei;
        font-size: 20px;
    }

    .column_image{
        width:200px;
        height:200px;
        margin-left: 15px;
        background-color: rgb(237, 236, 236);
        background-repeat: no-repeat;
        border-radius:10px;
        margin-bottom: 15px;
    }


    .image_mid{
        height: 150px;
        width: 200px;
        margin: 0px;
        position: relative;
        left:-14px;
        border-radius:10px 10px 0 0;
    }

    .ui.price{
        width: 90px;
        height: 30px;
        background:rgba(22, 22, 21, 0.5) none repeat;

        padding: 5px;
        position: relative;
        top:120px;
    }

    .ui.center.aligned.vertical.segment.address{
        position: relative;
        top:110px;
        font-family:Microsoft YaHei;
    }

    .ui.three.column.grid.first1{
        margin-top: 5px;
        margin-bottom: 30px;
    }


    .ui.vertical.mid_img{
        height:823px;
        border-left: solid rgb(193, 195, 195) 1px;
        padding:15px;
        position: relative;
        top: -15px;
    }

    .column.page{
        width: 200px;
        height: 40px;
        margin: 0px;
        margin: 5px 0 0 0;
    }

    .ui.vertical.mid_img > .ui.vertical.container.segment.page {

        /*bottom: 400px !important;*/
    }

    /*数字按钮*/
    .ui.button.active.num{
        width: 35px;
        padding-left:14px;
        background-color: #fcc416;
    }

    .ui.button.num {
        width: 35px;
        padding-left: 14px;
        margin-left: 5px;
        background-color: #f6f6f6;
    }


    .page.button{
        border: none;
        background-color:transparent;
    }
</style>
