import pkg from 'web3-utils';
const { toBN } = pkg; 
const scale = toBN(10).pow(toBN(18)); 

const initial_supply = toBN(660_000_000);
const total_supply = toBN(1_000_000_000)
const rate_reduction = toBN(550000000000000000);

const initial_rate = total_supply.sub(initial_supply).mul(scale.sub(rate_reduction)).div(scale);

let supply = initial_supply; 
let rate = initial_rate; 
console.log(0, supply.toString());
for (let i = 1; i <= 10; i += 1) {
    supply = supply.add(rate); 
    rate = rate.mul(rate_reduction).div(scale);
    console.log(i, supply.toString());
}
