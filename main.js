import {unit_test} from "./generate_unit_test.js";

const obj = new unit_test();

(async () => {
    
    await obj.run();

})().catch(e => {
    
});