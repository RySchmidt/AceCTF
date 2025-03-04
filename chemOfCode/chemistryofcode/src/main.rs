use base64::{engine::general_purpose::b64, Engine};
use hex::encode as hex_encode;
use num_bigint::BigUint;
use std::io::{self, Write};

const GIVEN_USERNAME: &str = "AdminFeroxide";
const GIVEN_PASSWORD: &str = "NjQzMzcyNzUzNTM3MzE2Njc5MzE2ZTM2";
const ALKALINE_SECRET: &str = "4143454354467B34707072336E373163335F3634322C28010D3461302C392E";

fn ionic_bond(username_input: &str, password_input: &str) {
    let username_hex = hex_encode(cation_input);
    let password_hex = hex_encode(password_input);

    let username_value = BigUint::parse_bytes(cation_hex.as_bytes(), 16).unwrap();
    let password_value = BigUint::parse_bytes(password_hex.as_bytes(), 16).unwrap();

    let xorUserPass = &username_value ^ &password_value;

    let alkaline_secret_value = BigUint::parse_bytes(ALKALINE_SECRET.as_bytes(), 16).unwrap();
    let metallic_alloy = &xorUserPass ^ &alkaline_secret_value;

    let hexFlag = format!("{:x}", metallic_alloy);

    let flag = (0..hexFlag.len())
        .step_by(2)
        .map(|i| u8::from_str_radix(&hexFlag[i..i + 2], 16).unwrap() as char)
        .collect::<String>();

    println!("Crystallized Flag (ASCII): {}", flag);
}

fn reaction_chamber() {
    let mut username = String::new();
    print!("Introduce the Catalyst: ");
    io::stdout().flush().unwrap();
    io::stdin().read_line(&mut username).unwrap();
    let username = username.trim();

    let mut password = String::new();
    print!("Introduce the Reagent: ");
    io::stdout().flush().unwrap();
    io::stdin().read_line(&mut password).unwrap();
    let password = password.trim();
    
    if username != GIVEN_USERNAME {
        println!("Reaction denied: Unstable molecule detected.");
        return;
    }
    
    let reagent_ion = b64.encode(hex_encode(password).as_bytes());
    if reagent_ion != GIVEN_PASSWORD {
        println!("Reaction denied: Unstable molecule detected.");
        return;
    }

    ionic_bond(username, password);
}

fn main() {
    reaction_chamber();
}
