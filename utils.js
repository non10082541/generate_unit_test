class utils {

    async create_file(file_name, file_data) {

        let fs = require('fs');

        fs.writeFile(file_name, file_data, function (err) {
          if (err) throw err;
          console.log('Replaced!');
        });

    }
    
    async load_data_from_template(file_name) {

        const fs = require("fs");

        const buffer = fs.readFileSync(file_name);

        const fileContent = buffer.toString();

        return fileContent;

    }    
}

export {utils};