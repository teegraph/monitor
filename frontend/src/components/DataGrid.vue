<template>
    <v-container>
        <v-row class="text-center">
            <v-col cols="2">
                <v-text-field
                    v-model="aggr.min"
                    label="Минимум"
                ></v-text-field>
            </v-col>
            <v-col cols="2">
                <v-text-field
                    v-model="aggr.max"
                    label="Максимум"
                ></v-text-field>
            </v-col>
            <v-col cols="2">
                <v-text-field
                    v-model="aggr.avg"
                    label="Среднее"
                ></v-text-field>
            </v-col>
            <v-col cols="2">
                <v-text-field
                    v-model="aggr.min100"
                    label="Минимум из 100"
                ></v-text-field>
            </v-col>
            <v-col cols="2">
                <v-text-field
                    v-model="aggr.max100"
                    label="Максимум из 100"
                ></v-text-field>
            </v-col>
            <v-col cols="2">
                <v-text-field
                    v-model="aggr.avg100"
                    label="Среднее из 100"
                ></v-text-field>
            </v-col>
        </v-row>
        <v-row class="text-center">
            <v-col cols="12">
                <v-data-table
                    :headers="headers"
                    :items="items"
                    :options.sync="options"
                    :server-items-length="totalItems"
                    :loading="loading"
                ></v-data-table>
            </v-col>
        </v-row>
    </v-container>
</template>

<script>
import axios from 'axios'
export default {
    name: "DataGrid",
    data () {
        return {
            headers: [
                {text: "ID", sortable: true, value: "id"},
                {text: "Дата", sortable: true, value: "date"},
                {text: "Нагрузка", sortable: true, value: "utilize"}
            ],
            items: [],
            options: {},
            loading: true,
            totalItems: 0,
            aggr: {
                min: 0,
                max: 0,
                avg: 0,
                min100: 0,
                max100: 0,
                avg100: 0
            }
        }
    },
    watch: {
        options: {
            handler () {
                this.getDataFromApi().then(data => {
                    this.items = data.items
                    this.totalItems = data.total
                })
            },
            deep: true,
        }
    },
    mounted() {
        this.getData()
        setInterval(() => this.getData(), 15000)
    },
    methods: {
        getData () {
            this.getDataFromApi().then(data => {
                this.items = data.items
                this.totalItems = data.total
                this.aggr = data.aggr
            })
        },
        getDataFromApi () {
            this.loading = true
            return new Promise((resolve) => {
                const { sortBy, sortDesc, page, itemsPerPage } = this.options
                let payload = {
                    page: page,
                    page_size: itemsPerPage,
                    sort: sortBy,
                    sort_desc: sortDesc,
                }
                axios.get("/api/v1/data", {params: payload} ).then(function(data){
                    let total = data.data.total
                    let items = data.data.items
                    let aggr = data.data.aggr
                    resolve({
                        items,
                        total,
                        aggr,
                    })
                })
                this.loading = false
            })
        }
    }
}
</script>

<style scoped>

</style>