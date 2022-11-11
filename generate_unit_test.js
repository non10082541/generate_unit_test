import {modules} from "./module.js";
import * as fs from 'fs';

import {new_modules} from "./new_module.js"
const new_module = new new_modules();

const obj_module = new modules();

class unit_test{
    constructor()
    {
        this.file_name = './fb-game.json';
    }

    isObject = (obj) => {
        return typeof obj === 'object' && !Array.isArray(obj) && obj !== null;
      }
      
    objToArray = (obj) => {
        return Object.keys(obj).map((key) => {
          return [
            key, isObject(obj[key]) ? 
              objToArray(obj[key]) :
              obj[key]
          ];
        });    
      }

    async run() {

        let data = fs.readFileSync(this.file_name, 'utf-8');
        data = JSON.parse(data);

        let count_modules = Object.keys(data).length;
        console.log("count : " + count_modules);
        
        // console.log("data:", data[0].name)

        // await new_module.execute(data[1]);

        for (let i = 0; i < count_modules; i++){

          console.log("count:", i)
          console.log("***** begin module *****");

          try{

            await new_module.execute(data[i]);

          }catch(err){

            console.log(err)

          }          
          console.log("***** end module *****");
          console.log("");
        }

        // for (let i=0; i<count_modules; i++) {

        //     console.log("***** begin module *****");
        //     console.log("name : " + data[i].name);
        //     for (let c=0; c<data[i].model.length; c++) {

        //         console.log("begin field( " + (c+1) + " )");
        //         console.log(data[i].model[c]);
        //         console.log("end field");
                
        //     }            
        //     console.log("***** end module *****");
        //     console.log("");
        // }

        //console.log("begin field");
        //console.log(data[0].model[0]);
        //console.log(data[0].model[1]);
        //console.log("end field");

    }

}

export {unit_test};