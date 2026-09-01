# rallous_crater_hq load — 1.20.1 / pack_format 15. Do not wipe marked HQs.
# data modify STORAGE set value needs a path; merge writes the root compound.
execute unless data storage rallous_crater_hq:data pos run data merge storage rallous_crater_hq:data {owner:[I;0,0,0,0],pos:{x:0,y:0,z:0}}
