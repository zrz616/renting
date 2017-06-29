<template>
    <div class="ui vertical basic segment displaywindow">
        <div class="ui container displaywindow">
            <!-- first row -->
            <h1 class="ui header in-displaywindow">精选优质房源</h1>
            <div class="ui three column grid in-displaywindow">
                <div v-for="house in fav_houses" class="column in-displaywindow">
                    <div class="ui card in-displaywindow">
                        <a class="image in-card">
                            <a class="label in-card">{{ house.house_type }}</a>
                            <img :src="house.house_show_url" alt="" />
                        </a>
                        <div class="content in-card">
                            <a class="header in-card" href="#">{{ house.address }}</a>
                            <div class="ui divider in-card"></div>
                            <div class="description in-card">
                                {{ house.transport }}
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
            <!--<div class="ui three column grid in-displaywindow">-->
                 <!--first item -->
                <!--<div class="column in-displaywindow">-->
                    <!--<div class="ui card in-displaywindow">-->
                        <!--<a class="image in-card">-->
                            <!--<a class="label in-card">温馨两居</a>-->
                            <!--<img src="/static/image/租房项目切图/1首页/img1.png" alt="" />-->
                        <!--</a>-->
                        <!--<div class="content in-card">-->
                            <!--<a class="header in-card" href="#">人民大学附近房源</a>-->
                            <!--<div class="ui divider in-card"></div>-->
                            <!--<div class="description in-card">-->
                                <!--宇宙中心五道口附近，方便出行、购物，适合陪读、考研、校外住宿。-->
                            <!--</div>-->
                        <!--</div>-->
                    <!--</div>-->
                <!--</div>-->
                <!--&lt;!&ndash; second item &ndash;&gt;-->
                <!--<div class="column in-displaywindow">-->
                    <!--<div class="ui card in-displaywindow">-->
                        <!--<a class="image in-card">-->
                            <!--<a class="label in-card">朝南</a>-->
                            <!--<img src="/static/image/租房项目切图/1首页/img2.png" alt="" />-->
                        <!--</a>-->
                        <!--<div class="content in-card">-->
                            <!--<a class="header in-card" href="#">清华大学附近房源</a>-->
                            <!--<div class="ui divider in-card"></div>-->
                            <!--<div class="description in-card">-->
                                <!--宇宙中心五道口附近，方便出行、购物，适合陪读、考研、校外住宿。-->
                            <!--</div>-->
                        <!--</div>-->
                    <!--</div>-->
                <!--</div>-->
                <!--&lt;!&ndash; third item &ndash;&gt;-->
                <!--<div class="column in-displaywindow">-->
                    <!--<div class="ui card in-displaywindow">-->
                        <!--<a class="image in-card">-->
                            <!--<a class="label in-card">舒适一居</a>-->
                            <!--<img src="/static/image/租房项目切图/1首页/img3.png" alt="" />-->
                        <!--</a>-->
                        <!--<div class="content in-card">-->
                            <!--<a class="header in-card" href="#">北京大学附近房源</a>-->
                            <!--<div class="ui divider in-card"></div>-->
                            <!--<div class="description in-card">-->
                                <!--宇宙中心五道口附近，方便出行、购物，适合陪读、考研、校外住宿。-->
                            <!--</div>-->
                        <!--</div>-->
                    <!--</div>-->
                <!--</div>-->
            <!--</div>-->
            <!-- second row -->
            <h1 class="ui header in-displaywindow">毗邻学校周边</h1>
            <div class="ui three column grid in-displaywindow">
                <!-- first item -->
                <div class="column in-displaywindow">
                    <div class="ui card in-displaywindow">
                        <a class="image in-card">
                            <img src="/static/image/租房项目切图/1首页/img4.png" alt="" />
                        </a>
                        <div class="content in-card">
                            <a class="header in-card" href="#">北京大学附近房源</a>
                            <div class="ui divider in-card"></div>
                            <div class="description in-card">
                                宇宙中心五道口附近，方便出行、购物，适合陪读、考研、校外住宿。
                            </div>
                        </div>
                    </div>
                </div>
                <!-- second item -->
                <div class="column in-displaywindow">
                    <div class="ui card in-displaywindow">
                        <a class="image in-card">
                            <img src="/static/image/租房项目切图/1首页/img5.png" alt="" />
                        </a>
                        <div class="content in-card">
                            <a class="header in-card" href="#">清华大学附近房源</a>
                            <div class="ui divider in-card"></div>
                            <div class="description in-card">
                                宇宙中心五道口附近，方便出行、购物，适合陪读、考研、校外住宿。
                            </div>
                        </div>
                    </div>
                </div>
                <!-- third item -->
                <div class="column in-displaywindow">
                    <div class="ui card in-displaywindow">
                        <a class="image in-card">
                            <img src="/static/image/租房项目切图/1首页/img6.png" alt="" />
                        </a>
                        <div class="content in-card">
                            <a class="header in-card" href="#">北京邮电大学附近房源</a>
                            <div class="ui divider in-card"></div>
                            <div class="description in-card">
                                宇宙中心五道口附近，方便出行、购物，适合陪读、考研、校外住宿。
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    import reqwest from 'reqwest';
    export default {
        data () {
            return {
                fav_houses: ''
            };
        },
        methods: {
            show () {
                let self = this;
                reqwest({
                    url: 'http://localhost:8000/api/index_show',
                    type: 'json',
                    method: 'GET',
                    success (resp) {
                        self.fav_houses = resp;
                    }
                });
            }
        },
        mounted () {
            this.show();
        }
    };
</script>

<style>
    .ui.vertical.basic.segment.displaywindow {
        height: 753px;
        background-image: url('/static/image/租房项目切图/1首页/photo_bg.png');
        background-size: cover;
        background-repeat: no-repeat;
        background-position: bottom;
        padding: 0;
        /*doubt: confusing why bg-image has an invisible margin 60px*/
        margin: 0;
        /*note: search "缩小窗口时CSS背景图出现右侧空白" for more info*/
        width:expression(document.body.clientWidth <= 960? "960px": "auto");
        min-width:960px;
    }

    .ui.container.displaywindow {
        width: 879px;
        /*note: height is uncessary for a container*/
        /*height: 753px;*/
        /*note: better to use padding for a container than margin*/
        padding-top: 60px;
        margin: 0;
    }

    .ui.header.in-displaywindow {
        min-width: 156px;
        height: 38px;
        font-size: 26px;
        color: #000000;
        margin-top: 0;
        margin-bottom: 23px;
    }

    .ui.three.column.grid.in-displaywindow {
        margin-bottom: 40px;
    }

    .column.in-displaywindow {

    }

    .ui.card.in-displaywindow {
        /*note: gutter first before column width*/
        /*width: 280px;*/
        height: 228px;
        border-radius: 10px;
        box-shadow: none;
    }

    .image.in-card {

    }

    .label.in-card {
        width: 74px;
        min-width: 56px;
        height: 26px;
        border-radius: 0 10px 0 0;
        font-size: 14px;
        text-align: center;
        padding-top: 3px;
        color: #ffffff;
        background-color: #f4c32a;
        position: absolute;
        left: 100%;
        transform: translate(-100%,0);
    }

    .content.in-card {
        padding-left: 26px !important;
        padding-right: 26px !important;
        padding-bottom: 17px !important;
    }

    .header.in-card {
        min-width: 144px;
        height: 27px;
        font-size: 18px;
        color: #000000;
        padding-top: 2px;
        margin-bottom: 5px;
        text-align: center;
    }

    .ui.divider.in-card {
        width: 110px;
        border: solid 1px #d6d6d6;
        margin-top: 0;
        margin-bottom: 18px;
        margin-left: 55px;
    }

    .description.in-card {
        min-width: 227px;
        height: 40px;
        font-size: 14px;
        color: #9b9b9b;
    }
</style>
