import * as fs from "fs"

class utils {

    async create_file(file_name, file_data) {

        fs.writeFile(file_name, file_data, function (err) {
          if (err) throw err;
          console.log('Replaced!');
        });

    }
    
    async load_data_from_template(file_name) {

        // const buffer = fs.readFileSync(file_name, "utf-8");

        // const fileContent = buffer.toString();

        // return fileContent;
        // console.log("load data from template")

    }    
}

export {utils};