class data_model{
    constructor()
    {
        this.id = 0;
        this.field_name = '';
        this.field_type = '';
        this.field_value = '';
        this.field_validate = true;

        this.fields_name = '';
        this.fields_value = '';
        this.max_length = 0

    }

    async set_field(data) {
        this.field_name = data.field_name;
        this.field_type = data.field_type;
        this.field_value = data.field_value;
        this.field_validate = data.field_validate;
    }

    async execute() {
        // return true
    }

    
}

export {data_model};