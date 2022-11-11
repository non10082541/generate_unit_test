import {data_model} from "./data_model.js";
import {utils} from "./utils.js"

const obj_data_model = new data_model();
const common_utils = new utils();

class modules{
    constructor(data)
    {
        this.insert_file_name = 'test_case_insert_module.py';
        this.edit_file_name = 'test_case_edit_module.py';
        this.delete_file_name = 'test_case_delete_module.py';
        this.list_file_name = 'test_case_list_module.py';
        this.search_file_name = 'test_case_search_module.py';     
        
        this.data_template_insert = '';
        this.data_template_edit = '';
        this.data_template_delete = '';
        this.data_template_list = '';
        this.data_template_search = '';

        this.template_insert_file_name = 'template_insert.py';
        this.template_edit_file_name = 'template_edit.py';
        this.template_delete_file_name = 'template_delete.py';
        this.template_list_file_name = 'template_list.py';
        this.template_search_file_name = 'template_search.py';
        
        
        this.module_name = ''; // เก็บเฉพาะชื่อ module name เช่น f_member

        this.fields = {}; //  มีค่า first_name password email
        this.insert = true;
        this.edit = true;
        this.delete = true;
        this.list = true;
        this.search = true;

        // this.module_name = data.modules;
        // console.log('module : ' + this.module_name);
        
        // this.fields = data.fields;
        
        // this.insert = data.insert;
        // this.update = data.edit;
        // this.delete = data.delete;
        // this.list = data.list;
        // this.search = data.search;        
    }

    async load_all_template() {

        if (this.insert === true)
            this.data_template_insert = await common_utils.load_data_from_template(this.template_insert_file_name);

        if (this.edit === true) 
            this.data_template_edit = await common_utils.load_data_from_template(this.template_edit_file_name);

        if (this.delete === true) 
            this.data_template_delete = await common_utils.load_data_from_template(this.template_delete_file_name);

        if (this.list === true) 
            this.data_template_list = await common_utils.load_data_from_template(this.template_list_file_name);

        if (this.search === true) 
            this.data_template_search = await common_utils.load_data_from_template(this.template_search_file_name);
            
    }

    async create_all_file() {

        await this.create_file_insert;
        await this.create_file_edit;
        await this.create_file_delete;
        await this.create_file_list;
        await this.create_file_search;

    }

    async create_file_insert() {

        let file_data = '';

        if (this.insert === true) {

            file_data = await this.process_script_data(this.data_template_insert);
            await common_utils.create_file(this.insert_file_name);

            return true;

        } else {

            return false;
        }
    }

    async create_file_edit() {

        let file_data = '';

        if (this.edit === true) {

            file_data = await this.process_script_data(this.data_template_edit);
            await common_utils.create_file(this.edit_file_name);

            return true;

        } else {

            return false;
        }
    }

    async create_file_delete() {

        let file_data = '';

        if (this.delete === true) {

            file_data = await this.process_script_data(this.data_template_delete);
            await common_utils.create_file(this.delete_file_name);

            return true;

        } else {

            return false;
        }
    }

    async create_file_list() {

        let file_data = '';

        if (this.list === true) {

            file_data = await this.process_script_data(this.data_template_list);
            await thcommon_utilsis.creat_file(this.list_file_name);

            return true;

        } else {

            return false;
        }
    }

    async create_file_search() {

        let file_data = '';

        if (this.search === true) {

            file_data = await this.process_script_data(this.data_template_search);
            await common_utils.create_file(this.search_file_name);

            return true;

        } else {

            return false;
        }
    }

    async execute(data) {
        
        this.module_name = data.name;
        console.log('module : ' + this.module_name);

        this.insert = data.insert;
        console.log("insert:", this.insert)

        this.edit = data.edit;
        console.log("edit:", this.edit)

        this.delete = data.delete;
        console.log("delete:", this.delete)

        this.list = data.list;
        console.log("list:", this.list)
        
        this.search = data.search;
        console.log("search:", this.search)

        this.fields = data.model;
        console.log("fields:", this.fields);


        // console.log("execute func")

        await obj_data_model.set_field(this.fields);

        await obj_data_model.execute();

        await this.load_all_template();
        await this.create_all_file();

        
        return true;

    }

    async process_script_data(data) {

        let script_data = data;

        // replace fields name
        const regex = /fields_name/i;
        console.log(script_data.replace(regex, obj_data_model.fields_name.toString()));

        // replace fields value
        regex = /fields_value/i;
        console.log(script_data.replace(regex, obj_data_model.fields_value.toString()));


        return script_data;
    }
    
}

export {modules};