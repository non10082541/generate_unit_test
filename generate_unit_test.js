import {modules} from "./module.js";
import * as fs from 'fs';

const obj_module = new modules();

class unit_test{
    constructor()
    {
        this.file_name = './fb-game.json';
    }

    async run() {

        // to do load json
        let data = fs.readFileSync(this.file_name, 'utf-8');
        data = JSON.parse(data);

        // loop for
        let i = 0;
        // console.log(data.modules.f_member)

        for (let modules in data){
            // console.log(i)
            // console.log(modules)
            if(modules != "description"){

                for(let module in data[modules]){
                    // console.log("module:", module)
                    let fields = data.modules[module].class // โยนเข้าไปใน fields

                    await obj_module.execute(module, fields);

                    // console.log(data_in_module)
                }
            }
        }
        // console.log(data.modules)
        // await obj_module.execute(data);

        // end loop for


    }

}

export {unit_test};