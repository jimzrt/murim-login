<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0091.txt",
      "sha256": "814f4900e98f607e3eb7ea8dce48db43cecb1f9f81c573c22a7997cec42b755e",
      "bytes": 13891
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "5e7895f28ed750e1f7c599e974cd45511bedfa34554038ccfbcdbc305d98b73e",
      "bytes": 3312
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "71d82c31440c543cac54cd8882b5217bee1f64b6e91a038d3b36037efee03785",
      "bytes": 9605
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "061ad0c78f92879910ea1538b573ed2c79461a050ef55170e9c9665e036f7e4b",
      "bytes": 23901
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "16c00401bd97b227b0f17df4658ebb5a5b09cb99c58b674c9c052727e501b8eb",
      "bytes": 8900
    }
  ],
  "estimated_tokens": 13698
}
-->

# Durable State Update — Chapter 91

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 91. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 20 concise items, `open_questions` to at most 8
items, and `temporary_decisions` to at most 8 items. Keep the serialized context
under 16384 UTF-8 bytes. Use only chapter
numbers through 91. `profile_updates` may replace one exact, uniquely occurring
complete line in a listed profile, and only an Aliases, Role, Personality, Voice, or
Relationships line. Use `profile_creations` only for a newly introduced named
character without a listed profile. Filenames must be plain `.md` basenames.
`names` contains only newly required Korean-to-English rows; Korean keys must occur
in the source. `address_pairs` contains only newly required speaker→addressee rows;
each Korean key must occur in the source or already appear in the address ledger,
and at least one endpoint must occur in the source (first-person narrators may be
ledger-only). Do not invent risk-register rows. Beat
plot paragraphs are plain strings; continuity and translation decisions are concise
list items.
Return this exact shape:

{
  "chapter": 91,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 91,
    "continuity_sources": [91],
    "active_continuity": ["active fact"],
    "open_questions": ["unresolved question"],
    "temporary_decisions": ["temporary translation decision"]
  },
  "names": [
    {"korean": "source spelling", "english": "English rendering", "notes": "brief note"}
  ],
  "address_pairs": [
    {
      "speaker": "speaker Korean",
      "addressee": "addressee Korean",
      "kinship": "kinship or role relation",
      "normal_address": "established English address",
      "speech_level": "speech level",
      "notes": "brief note"
    }
  ],
  "profile_updates": [
    {
      "path": "characters/Listed Profile.md",
      "current": "- **Role:** exact current full line",
      "replacement": "- **Role:** finished replacement full line"
    }
  ],
  "profile_creations": [
    {
      "filename": "English Name.md",
      "korean": "source name",
      "english": "English Name",
      "aliases": [],
      "role": "stable role",
      "personality": "stable traits",
      "voice": "stable voice",
      "relationships": "stable relationships"
    }
  ]
}

Use empty arrays when no name, address-pair, or profile change is required.

## Prior durable context

```json
{
  "active_continuity": [
    "The party sells The Minotaur's Labyrinth byproducts and Magic Gems to the Administration.",
    "Im Kkeokjeong warns that Sangdong Guild is a powerful local Guild capable of threatening Peace Guild.",
    "Im Chunsoo is Sangdong Guild's A-rank Guild Master and founder, known as Frozen for his exceptional ice magic.",
    "Im Changsoo transferred the promised four billion won to Jin Taekyung after Im Chunsoo learned about his transfers and beat him.",
    "Hayeon knows Kim Jeonghee had secretly worked in a restaurant kitchen for over a year; Kim Jeonghee is Taekyung and Hayeon's mother.",
    "Taekyung's father died when a Gate opened downtown during the Great Cataclysm.",
    "Kim Jeonghee quit her restaurant kitchen job after the owner insulted and attacked Taekyung, then left with him.",
    "Kim Minsu is the restaurant owner's son, a D-rank Hunter in Sangdong Guild, and is not known personally by Im Changsoo.",
    "Jin Taekyung is a C-rank Hunter rather than the F-rank Hunter the restaurant owner believed him to be; Im Changsoo confirmed Taekyung received four billion won.",
    "Taekyung can use the Jin Family's Cultivation Technique to perform Circulate Qi for Healing on other people.",
    "Hayeon and Kim Jeonghee recovered substantially after receiving Circulate Qi for Healing from Taekyung.",
    "Taekyung's reality and Murim Inventories are separate.",
    "Hayeon asked Taekyung whether she could drop out of school after learning that he earned four billion won from a raid.",
    "Peace Guild's Guild house remodeling is scheduled to finish in one week, and Taekyung is on paid vacation until then.",
    "Choi Minwoo and Butler Kim suspect that Taekyung may be a third-awakening Hunter; Butler Kim will investigate.",
    "Sangdong Guild is monitoring Peace Guild and has marked Taekyung as a major target; Choi has not warned him because he wants Sangdong's investigation to reveal more.",
    "Taekyung intends to purchase his family's former home in his redeveloped childhood neighborhood.",
    "An unidentified man approached Taekyung outside the childhood supermarket and asked whether Taekyung knew him."
  ],
  "continuity_sources": [
    90
  ],
  "open_questions": [
    "Whether Im Chunsoo or Sangdong Guild will retaliate against Peace Guild remains unresolved.",
    "What will happen to Kim Jeonghee after leaving the restaurant remains unresolved.",
    "Whether Hayeon will actually drop out of school remains unresolved.",
    "Whether third-awakening Hunters exist and whether Taekyung is one remains unresolved.",
    "Who the unidentified man is and how he is connected to Taekyung remains unresolved."
  ],
  "safe_through": 90,
  "temporary_decisions": [
    "Use Frozen for 프로즌 and preserve the tiger-father/dog-son wordplay in 호부견자.",
    "Use ajumma for 아줌마 with an explanatory footnote.",
    "Retain goshiwon with an explanatory footnote.",
    "Use Minsu for 민수 as the short form of Kim Minsu.",
    "Render 운기요상 as Circulate Qi for Healing.",
    "Render 하급 포션 as Lesser Potion.",
    "Render 3차 각성자 as third-awakening Hunter and 3차 각성 as third awakening.",
    "Render 사장님 as Boss in the real-estate context, including young Boss."
  ],
  "version": 1
}
```

## Existing names ledger

# Established Names

Binding Korean → English for names, titles, aliases, and forms established in
accepted chapters. Injected only when the exact Korean appears in the current
chapter. Overrides `compendium.md` on the same Korean key. Add a row at first
use. First use of an unlisted name or title almost always needs a footnote.

| Korean | Preferred English | Notes |
| ------ | ----------------- | ----- |
| 장삼 | **Jang Sam** | Bandit; personal name |
| 천력부 | **Heavenly Axe** | Epithet of Jang Sam; never romanize |
| 천관일 | **Sky-Piercing Strike** | Final form of the Jin Family's Spear Technique; 天貫軼 |
| 녹림십팔채 | **Eighteen Strongholds of Green Forest** | |
| 홍화루 | **Honghwaru** | Lower District Sect Shanxi branch; pleasure house in Taiyuan |
| 하연 | **Hayeon** | Jin Taekyung’s younger sister |
| 응현 | **Eung-hyeon** | Jin Family branch location |
| 산음 | **Saneum** | Jin Family branch location |
| 삭주 | **Sakju** | Jin Family branch location |
| 정양 | **Jeongyang** | Shanxi location |
| 혼주 | **Honju** | Shanxi location |
| 견정 | **Gyeonjeong** | Acupoint |
| 아문 | **Amun** | Acupoint |
| 봉안 | **Bongan** | Acupoint |
| 입동 | **Ip-dong** | Acupoint |
| 갱생권 | **Reformation Fist** | Jin Mukyung's named fist technique |
| 금나수 | **grappling technique** | Close-combat wrist-lock technique; rendered descriptively |
| 삼재검법 | **Three Calamities Sword Technique** | Sword technique Mukyung assumes Taekyung is pretending to use. |
| 약왕당 | **Medicine King Hall** | The Jin Family's medical hall. |
| 이공자 | **Second Young Master** | Title used for Jin Mukyung. |
| 수문각주 | **Master of the Gatekeeper Pavilion** | Office Hyuk Mujin is rumored to receive. |
| 공청석유 | **gongcheong seokyu** | Rare martial-arts elixir; the term also creates a petroleum pun. |
| 군자 | **junzi** | Confucian ideal of a morally upright gentleman. |
| 삼문협 | **Three Questions Gorge** | A distant gorge and route connecting Shanxi with Shaanxi and Henan. |
| 섬서 | **Shaanxi** | Province bordering Shanxi. |
| 삼공자 | **Third Young Master** | Title used for Jin Taekyung. |
| 맹주 | **Alliance Leader** | Leader of the regional Murim alliance. |
| 약왕당주 | **Medicine King Hall Master** | The unnamed physician who runs the Medicine King Hall. |
| 송검문 | **Song Sword Sect** | Small-to-medium sect in central Shanxi. |
| 송검문주 | **Sect Leader of Song Sword Sect** | Title held by Huang. |
| 귀검 | **Ghost Sword** | Wipeng's epithet. |
| 황 모 | **Huang** | Surname-style self-reference by the Sect Leader of Song Sword Sect. |
| 아스모데우스 | **Asmodeus** | Demon King referenced in Taekyung's sarcastic comparison; does not appear directly. |
| 낙류검 | **Falling Flow Sword** | Named sword technique discovered by Mukyung in the archives of Heaven's Gate Temple; its name evokes a waterfall. |
| 질풍십이권 | **Twelve Gale Fists** | Named fist technique Mukyung threatens to use against Taekyung. |
| 화염신장 | **Flame Divine Palm** | Jopil's deadly palm technique, noted when Taekyung compares Jopil with Mukyung. |
| 마혈 | **Paralysis Acupoint** | System condition label for temporary paralysis. |
| 아혈 | **Mute Acupoint** | System condition label preventing speech. |
| 분근착골 | **Tendon-Splitting and Bone-Twisting** | Cruel immobilization technique described by Mukyung. |
| 일문일살 | **One Question, One Kill** | Jopil's alias. |
| 군자검 | **Junzi Sword** | Epithet Jin Wikyung begins receiving after the war. |
| 칠득이 | **Childeuk** | Jin Family servant. |
| 천자문 | **Thousand Character Classic** | Classical text Childeuk cannot complete. |
| 천무지체 | **Heavenly Martial Physique** | Named physique or constitution mentioned hypothetically by Jin Mukyung. |
| 장칠득 | **Jang Childeuk** | Personal-name form of Childeuk; he is newly appointed as a martial artist directly under Jin Wikyung. |
| 최 팀장 | **Team Leader Choi** | Team Leader who owns the café where Taekyung signs a contract. |
| 명품충 | **Designer-Brand Junkie** | Display name used by Team Leader Choi in a text message. |
| 평화 | **Peace Guild** | Guild name. |
| 김 집사 | **Butler Kim** | Choi's butler and limousine driver. |
| 히말라야 | **Himalayas** | Mountain region referenced as the source of the bottled water. |
| 히말라야의 정수 | **Essence of the Himalayas** | System-named consumable that temporarily raises Intelligence. |
| 부천 | **Bucheon** | City with a dense concentration of Gates and Guild headquarters. |
| 강남 | **Gangnam** | Formerly valuable Seoul-area real estate. |
| 분당 | **Bundang** | Formerly valuable Korean real estate area. |
| 대한민국 | **Korea** | Country reference. |
| 순이 | **Sooni** | Former owner of Sooni's Super. |
| 순이네 수퍼 | **Sooni's Super** | The Peace Guild's Guild house. |
| 송 양 | **Miss Song** | The Peace Guild's final member; full identity not yet given. |
| 아레스 | **Ares Guild** | The leading Guild in Korea; formerly employed Team Leader Choi and Song Song. |
| 논산 | **Nonsan** | Location of Korea's Hunter training center. |
| 임혁준 | **Im Hyeokjun** | Im Kkeokjeong's personal name, shown in the System Level window. |
| 미노타우로스 | **Minotaur** | B-rank monster species. |
| 부천터미널 길드 | **Bucheon Terminal Guild** | Guild whose raid footage is shown. |
| 미노타우로스의 미로 | **The Minotaur's Labyrinth** | B-rank Gate. |
| 상동 길드 | **Sangdong Guild** | Mid-sized Guild near Bucheon that joins Peace Guild's first official raid. |
| 헌터 협회 | **Hunter Association** | Organization investigating the Bucheon Terminal Guild fatality. |
| 흑색 드레이크 | **Black Drake** | B-rank monster whose leather and spine are used for Taekyung's loaned equipment. |
| 장인의 흑색 드레이크 가죽 세트 | **Masterwork Black Drake Leather Set** | Peak-grade armor set loaned to Taekyung. |
| 장인의 검은 가시 창 | **Masterwork Black Thorn Spear** | Peak-grade spear loaned to Taekyung. |
| 출혈 | **Bleeding** | Effect with a 90% activation chance on a successful spear hit. |
| 니콜라스 | **Nicholas** | North American craftsman associated with the space-expansion suitcase. |
| K사 | **K Company** | Manufacturer of the space-expansion suitcase. |
| 혜린 | **Hye-rin** | C-rank female mage and member of Im Changsoo's Sangdong Guild team. |
| 청담동 | **Cheongdam-dong** | District mentioned as a luxury shopping location. |
| 투우사의 전신 갑옷 | **Matador’s Full-Body Armor** | Peak-grade armor equipped by Im Kkeokjeong; grants bonuses against bovine-type monsters. |
| 투우사의 방패 | **Matador’s Shield** | Peak-grade shield equipped by Im Kkeokjeong; can activate Taunt and Hallucination against bovine-type monsters. |
| 도발 | **Taunt** | System effect that the Matador’s Shield can activate against bovine-type monsters. |
| 환각 | **Hallucination** | System effect that the Matador’s Shield can activate against bovine-type monsters. |
| 미노타우로스 전사 | **Minotaur Warrior** | Level-window designation for the first Minotaur encountered in the labyrinth. |
| 발설지옥 | **tongue-pulling hell** | Buddhist hell associated with punishment for liars and slanderers; explained in a footnote. |
| 껄떡쇠 | **Horndog** | Im Changsoo’s nickname for his womanizing. |
| 강원도 | **Gangwon Province** | Province named in Taekyung’s joke about the Minotaur’s next life. |
| 횡성 | **Hoengseong** | Place in Gangwon Province named in Taekyung’s joke. |
| 자일리톤 | **Xyliton** | Finnish equipment manufacturer whose custom helmet records video. |
| 유네스코 | **UNESCO** | Organization referenced in Taekyung’s cultural-heritage joke. |
| 일섬 | **One Annihilation** | Named spear technique Taekyung uses to kill the Boss Zone monster in one blow. |
| 미노타우로스 대전사 | **Minotaur Warrior** | Level 70 B-rank boss monster of The Minotaur's Labyrinth. |
| 임 팀장님 | **Team Leader Im** | Formal address for Im Changsoo used by a Sangdong Guild teammate. |
| 프로즌 | **Frozen** | Im Chunsoo's epithet as an A-rank ice mage. |
| K은행 | **K Bank** | Bank where Im Changsoo's transfer is reported. |
| 김정희 | **Kim Jeonghee** | Jin Taekyung and Hayeon's mother; restaurant kitchen worker |
| 아줌마 | **ajumma** | Familiar term for a middle-aged or married woman, used for Kim Jeonghee |
| 사장님 | **Boss** | Address for the restaurant owner; contextually rendered as ma'am in one reply |
| 김민수 | **Kim Minsu** | The restaurant owner's son; D-rank Hunter in Sangdong Guild. |
| 민수 | **Minsu** | Short form used for Kim Minsu. |
| 운기요상 | **Circulate Qi for Healing** | System-named skill that channels internal energy through another person's body to cleanse accumulated waste and restore health. |
| 하급 포션 | **Lesser Potion** | Low-grade healing potion issued as raid supplies; its System Grade is Third Rate. |
| 3차 각성자 | **third-awakening Hunter** | Hypothetical Hunter classification that would come after reawakening. |
| 재각성 | **reawakening** | Established Hunter awakening category described as having no further stage. |
| 피의 일주일 | **Bloody Week** | The hellish first week after Gates opened, during which casualties reached the tens of millions. |
| 전세 | **jeonse lease** | Korean lump-sum deposit lease used in the family's redevelopment-era housing history. |

## Existing address-pair ledger

# Established Address Pairs

Exceptional speaker → addressee forms established in accepted chapters.
Injected only when both endpoints are present in the current chapter: the
Korean appears in the source, or belongs to a matched compact profile.
Overrides generic relationship prose in character profiles for this pair.

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진무경 | younger_to_older_brother | hyung | casual-but-junior | Retain hyung for 형 in Taekyung's greeting; Mukyung then punishes the casual speech. |
| 진무경 | 진태경 | older_to_younger_brother | youngest | blunt-senior | 막내 / youngest; may taunt that lasting a quarter-hour would make Taekyung the older brother. |
| 진태경 | 진위경 | younger_to_eldest_brother | brother | familiar-but-respectful | Self-corrects from the personal name to kinship: “Jin Wikyung—I mean, my brother?”; 큰형 is eldest brother. |
| 진위경 | 진태경 | eldest_to_youngest_brother | youngest | affectionate-protective | Uses youngest-brother address; openly affectionate beneath a public mask. |
| 진태경 | 성진호 | junior_to_older_friend | Jinho hyung | casual-but-junior | Retain hyung for 형; Jinho is three years older. |
| 성진호 | 진태경 | older_friend | informal / younger-brother | teasing-senior | Speaks informally while demanding respect as the older friend. |
| 진태경 | 임꺽정 | junior_friend | Kkeokjeong hyung | casual-but-junior | After Im asks to be called hyung. |
| 임꺽정 | 진태경 | older_friend | hyung | hearty-casual | “Call me hyung. We’re not even that far apart in age.” |
| 위팽 | 진위경 | retainer_to_lord | my lord | deferential | 주공; Wipeng is Jin Wikyung’s personal guard. |
| 소천 | 진태경 | rescued_survivor_to_benefactor | Benefactor | deferential | Socheon repeatedly addresses Taekyung as 은인. |
| 진무경 | 진위경 | younger_to_older_brother | older brother | formal-but-blunt | Mukyung refers to Wikyung as 형 while remaining emotionally restrained. |
| 진위경 | 진무경 | older_to_younger_brother | little brother | affectionate-casual | Wikyung uses 아우야 and 무경아 with openly affectionate familiarity. |
| 진태경 | 공야청 | junior_to_respected_hero | Great Hero Gong | deferential | Taekyung consistently attaches 대협 when addressing Gong Yacheong. |
| 위팽 | 송검문주 | visitor_to_sect_leader | Sect Leader | formal-polite | Wipeng addresses the Song Sword Sect Leader respectfully while delivering the summons. |
| 송검문주 | 위팽 | sect_leader_to_visiting_master | Great Hero Wipeng | deferential | The Sect Leader addresses Wipeng as 위 대협 while fearing the Ghost Sword's power. |
| 진태경 | 월화 | junior_to_older_female_acquaintance | Wolhwa noona | casual-but-junior | Taekyung uses this address while speaking in his sleep or delirium. |
| 칠득이 | 진위경 | servant_to_lesser_family_head | Lesser Family Head | deferential | Childeuk repeatedly addresses Wikyung as 소가주님. |
| 진위경 | 칠득이 | lesser_family_head_to_servant | you | formal-but-familiar | Wikyung addresses Childeuk with 자네. |
| 진위경 | 장칠득 | lesser_family_head_to_direct_martial_artist | Martial Artist Jang | affectionate and ceremonious | Wikyung embraces and exuberantly praises Childeuk after acknowledging their minor misunderstanding. |
| 혁무진 | 진태경 | squad_subordinate_to_squad_leader | Squad Leader | deferential | Hyuk Mujin says he obeys only his squad leader's orders and identifies Taekyung as the Third Young Master. |
| 진태경 | 혁무진 | squad_leader_to_squad_subordinate | Mujin | familiar-and-commanding | Taekyung calls him 무진아 while summoning him from the driver's box. |
| 진태경 | 최 팀장 | guild_member_to_team_leader | Team Leader | deferential | Taekyung addresses Choi as 팀장님. |
| 최 팀장 | 진태경 | team_leader_to_guild_member | Taekyung | formal-but-familiar | Choi addresses him as 태경 씨. |
| 진태경 | 김 집사 | client_to_butler | Butler Kim | formal-deferential | Taekyung addresses him as 김 집사님. |
| 최 팀장 | 김 집사 | employer_to_butler | Butler Kim | formal-polite | Choi addresses him as 김 집사님. |
| 김 집사 | 진태경 | butler_to_hunter_client | Hunter | deferential | Butler Kim refers to Taekyung as 헌터님. |
| 임꺽정 | 송 양 | older_guild_member_to_younger_female_guild_member | Miss Song | hearty-casual | Im Kkeokjeong calls her 송 양. |
| 진태경 | 송송이 | guild_member_to_guild_member | Miss Song | formal-polite | Taekyung repeatedly uses 송이 씨 while introducing himself and attempting to court Song Song. |
| 송송이 | 진태경 | guild_member_to_guild_member | Taurus | casual-teasing | Song Song refers to Taekyung by his zodiac sign when calling him to the meal. |
| 진태경 | 김 집사 | junior_to_senior_Hunter | Senior | deferential | After learning that Butler Kim trained at the same Nonsan regiment and battalion, Taekyung addresses him as 선배님. |
| 김 집사 | 최 팀장 | butler_to_employer | Young Master | deferential | Butler Kim addresses Choi as 도련님 when agreeing to follow his decision about Guild titles. |
| 임창수 | 혜린 | sponsor_to_sponsored_lover | Hye-rin | condescending-casual | Changsoo refers to himself as this oppa while claiming he will protect her. |
| 최 팀장 | 임꺽정 | guild_team_leader_to_guild_member | Hunter Im | formal-polite | Choi addresses Kkeokjeong as 임 헌터님 while telling him to put on the equipment. |
| 임창수 | 진태경 | rival_guild_team_leader_to_guild_member | Mr. Jang Taekyung | mock-formal and condescending | Changsoo deliberately uses the wrong surname, then dismisses whether Taekyung is Jin or Jang. |
| 진태경 | 임창수 | guild_member_to_rival_guild_team_leader | Shit Changsoo | insulting-casual | Taekyung’s retaliatory surname pun after Changsoo misnames him. |
| 임창수 | 송송이 | rival_guild_team_leader_to_guild_member | Miss Song | mock-polite | Uses 송송이 씨 while proposing that Song Song join Sangdong Guild. |
| 송송이 | 임창수 | guild_member_to_rival_guild_team_leader | Shit Changsoo—no, Im Changsoo | blunt but polite | Insults Changsoo with 씹창 and then corrects herself to his proper name while rejecting him. |
| 송송이 | 김 집사 | guild_member_to_guild_master | Guild Master | formal-polite | Requests the Guild Master’s permission before changing Guilds under the wager. |
| 송송이 | 최 팀장 | guild_member_to_team_leader | Team Leader | formal-polite | Asks Choi whether he accepts her possible Guild transfer if the bet is lost. |
| 송송이 | 임꺽정 | younger_guild_member_to_older_guild_member | Uncle | casual-polite | Song Song uses 아저씨 while asking Im Kkeokjeong to agree that Changsoo is nasty. |
| 김 집사 | 임창수 | guild_master_to_rival_guild_member | Changsoo | mock-polite | Butler Kim uses 창수 씨 while accusing Changsoo of refusing to pay. |
| 지점장 | 임춘수 | bank_branch_manager_to_guild_master | Guild Master | formal-deferential | The K Bank branch manager addresses Im Chunsoo as 길드장님 while reporting Changsoo's transfer. |
| 임춘수 | 임창수 | father_to_son | Changsoo | furious-parental | Im Chunsoo uses Changsoo's name alongside hostile forms such as that bastard and you little shit. |
| 하연 | 진태경 | younger_sister_to_older_brother | oppa | casual-familiar; pleading for important requests | Hayeon habitually puts 오빠 first when making an important request. |
| 김정희 | 사장님 | employee_to_restaurant_owner | Boss | formal-polite, becoming firm | Uses the owner's title while demanding an apology and defending Taekyung. |
| 사장님 | 김정희 | restaurant_owner_to_employee | Ajumma | condescending-casual | Repeatedly uses 아줌마 while berating Kim Jeonghee. |
| 진태경 | 김정희 | son_to_mother | Mom | casual-familiar and affectionate | Taekyung's first words after entering the restaurant and seeing his mother. |
| 김정희 | 진태경 | mother_to_son | Son | affectionate-familiar | Calls Taekyung 아들 when surprised by his visit and later asks whether he has eaten. |
| 진태경 | 사장님 | visitor_to_restaurant_owner | Boss | polite but sarcastic | Maintains a superficially respectful address while baiting the owner during the confrontation. |
| 사장님 | 진태경 | restaurant_owner_to_employee_son | you / you little punk | condescending-aggressive | Uses hostile informal forms while trying to intimidate Taekyung. |
| 부동산 아저씨 | 진태경 | real_estate_agent_to_customer | Boss | polite and sales-friendly | The unnamed real estate agent repeatedly addresses Taekyung as 사장님 while arranging a house viewing. |

## Exact glossary matches

| 진태경    | **Jin Taekyung**   |
| 임창수    | **Im Changsoo**   |
| 홍우진    | **Hong Woojin**   |
| 무인     | **martial artist**                               | Default term                                          |
| 경지     | **realm** / **realm stage**                      | Especially power level                                |
| 시스템              | **System**                     |
| 레벨               | **Level**                      |
| 헌터      | **Hunter**            |
| 게이트     | **Gate**              |
| 길드      | **Guild**             |
| 팀장      | **Team Leader**       |
| 마법사     | **mage**              |
| 하연 | **Hayeon** | Jin Taekyung’s younger sister |
| 사장님 | **Boss** | Address for the restaurant owner; contextually rendered as ma'am in one reply |

## Listed compact profiles

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 90
- **Aliases:** Sleeping Dragon of Shanxi
- **Role:** Modern-world protagonist; recently fired after seven years at his job; C-rank Hunter who defeated eight B-rank Minotaurs and killed a Level 70 B-rank Minotaur Warrior in one blow; First Rate martial artist standing before the Peak realm; youngest son of the Jin Family of Taiyuan
- **Personality:** Hungry, self-aware, dryly observant, and willing to take a questionable opportunity when desperate; treats the impossible as a game until the danger becomes undeniable
- **Voice:** First-person, conversational, dryly self-mocking; uses vivid trap-and-prey imagery, game jargon, and occasional profanity
- **Relationships:** Jin Mukyung’s younger brother and current student; son of a deceased father; supports his mother and younger sibling

## Korean source

```text
＃91화



“혹시 저 아세요?”

성큼성큼 다가온 남자의 말에 내가 되물었다.

“저가 누군데요?”

적어도 자기소개는 하고 물어봐야 하는 거 아니냐?

황당한 마음이 내 표정으로 다 드러났는지 남자가 짙은 색의 선글라스를 슥 내린다. 훈훈한 생김새에 적당히 그을린 얼굴이 드러났다.

“박지훈이요.”

박지훈? 글쎄, 그동안 만난 사람이 한둘이어야지.

무엇보다 낯익은 얼굴이 아니다.

“죄송한데 사람 잘못 보신 것 같아요.”

“아닌데, 분명히 맞는데. 혹시 가람중 나오지 않으셨어요?”

“어?”

내가 다녔던 학교 이름이다. 졸업도 못 하고 이사를 가는 바람에 거기서 인연이 끊겼지만 아직도 기억이 생생했다.

“맞죠? 가람중. 올해 나이가 스물일곱이고.”

“네, 그렇긴 한데…….”

“맞네! 3학년 6반 진태경!”

나도 가물가물한 학년, 반에 이름까지.

이 정도면 인정하지 않을 수 없다. 입이 찢어져라 웃는 선글라스 남에게 물었다.

“……진짜 저 아세요?”

“나 지훈이라고, 박지훈! 중학교 때 맨날 같이 축구하고 그랬잖아! 공부 못해서 허구한 날 우리 둘만 불려 가서 담임한테 얻어터지고. 기억 안 나냐?”

축구? 담임한테 얻어터져?

나는 설마 하는 마음으로 입을 열었다.

“박지황?”

“그래, 인마. 나 박지황이야! 아, 참. 너는 나 개명한 거 몰랐겠구나.”

“당연히 모르지.”

박지훈은 몰라도 박지황은 안다.

중학교 시절 동창을 여기서 만날 줄이야. 반가움에 절로 웃음이 지어졌다.

“이야, 여기서 만나네. 난 처음 보는 놈이 와서 알은체하길래 뭔가 했다.”

“그래도 알아봐야 하는 거 아니냐? 무슨 유치원 때도 아니고 고작해야 10년 전인데.”

“10년이 아니라 5년이었어도 못 알아봤겠다. 얼굴이 너무 변했는데?”

“그런가? 하하.”

부정할 수 없는 사실이다. 까무잡잡한 피부에 왜소한 체격이었던 녀석은 어딜 가도 훈남 소리 들을 법한 외모로 변했다.

“얼굴만 잘생겨진 게 아니라 몸도 좋아졌다?”

“오, 눈썰미 좋은데.”

“기본이지.”

기억으로는 나와는 머리 한 개쯤 차이가 있었던 것 같은데, 이제는 눈높이가 얼추 비슷하다.

“자식, 완전히 용 됐네.”

몰라보게 달라진 얼굴에 단단한 체격, 예쁜 애인과 척 봐도 억은 우습게 나갈 것 같은 외제 차까지.

십여 년 만에 만난 지황이는 많이 달라져 있었고, 나는 그 이유를 알고 있다.

‘이 녀석도 헌터군.’

기감이 경지에 이르자 굳이 시스템을 이용하지 않더라도 상대방을 파악할 수 있게 되었다.

기(氣)가 느껴진다고 해야 되나? 녀석은 분명 헌터다. 얼마 전 만난 임창수와 엇비슷하거나 어쩜 더 강할지도 모르겠다.

‘10년 만에 만난 친구가 헌터라, 신기하네.’

기감을 사용해서 레벨을 읽어 낼 수도 있지만 굳이 그렇게까지 하고픈 마음은 들지 않았다.

추억이 담긴 장소에서 옛 친구를 만났으니까. 지금의 나는 헌터도 무인도 아닌 그냥 평범한 진태경이다.

“아무튼 진짜 반갑다. 너 전학 가자마자 연락 끊겨서 엄청 섭섭했던 거 아냐?”

“그랬나? 그때는 워낙 정신이 없어서.”

당시 내 나이 열여섯. 한창 사춘기를 겪을 나이에 아버지가 돌아가신 직후기까지 해서 머릿속이 복잡했다.

고등학교 진학 후에는 체대를 목표로 운동에만 매진하면서 전에 알던 친구들과는 자연스럽게 연락이 끊어졌었지.

“아, 그래. 그때는 그랬었지. 미안하다.”

실수했다고 생각했는지 지황이, 아니 지훈이의 미소가 어색해진다.

“미안하긴 무슨. 진작 연락 안 한 내 잘못이지. 근데 너 아직도 여기 사냐?”

“지금은 가족들도 전부 서울 산다. 여자 친구랑 여행 다녀오는 길에 생각나서 들른 거야.”

“이야, 금의환향이네.”

“낯간지럽게 무슨. 성공하려면 아직 한참 멀었지.”

“이 정도면 충분히 성공한 거지, 뭘 더 바라?”

그 후로도 우리는 웃으며 이야기를 나눴다. 중학교 시절의 추억이 대부분이었지만 그것만으로도 충분히 즐거운 시간이었다.

지훈이의 여자 친구가 다리가 아프다며 은근히 눈치를 줬을 때는 상당한 시간이 흐른 뒤였다.

“오빠, 나 다리 아픈데.”

“응? 그럼 차에서 기다릴래? 이야기 조금만 더 하고 갈게.”

“……그게 할 소리야?”

친구의 연애 사업을 방해할 생각은 눈곱만큼도 없는 나는 눈치껏 손을 내저었다.

“아냐, 남은 얘기는 다음에 하자.”

“다음에? 너 10년 전에도 비슷한 말 했었던 거 아냐? 다음에 연락할게. 그러고 가더니 한 번도 연락 없었잖아.”

그렇게 말하니까 할 말이 없다. 입맛을 다시는 내게 지훈이가 명함을 내밀었다.

“됐고, 당장 이 번호로 전화 걸어.”



[명동 길드 1팀. 박지훈 헌터.]



명동 길드면 한국의 10대 길드까지는 아니어도 20대 길드에는 충분히 들어가는 대형 길드다.

그중에서도 1팀이면 명동 길드에서도 인정받는 엘리트라는 뜻. 어지간한 중견 길드로 이직해도 팀장 정도는 우습게 할 수 있는 수준이다.

‘어느 정도는 예상했지만 생각 이상인데?’

내심 놀란 마음을 숨기며 적힌 번호로 전화를 걸었다.

우우웅. 스마트폰을 확인한 지훈이가 씩 웃는다.

“전화할게. 술 한잔해야지.”

“봐서. 바쁘면 못 나오는 거고. 시간 괜찮으면 나가는 거고.”

“그런 말이 어디 있어? 안 그래도 지난번 동창회 때 네 얘기 나오더라. 뭐 하고 지내냐고.”

“내 얘기가 나왔다고?”

“반응이 왜 그래? 너 애들한테 인기 많았잖아.”

“내가 그랬었나? 온종일 운동장에 있었으니까 남자애들이랑은 좀 친했던 것 같기도 한데.”

“여자들한테도 인기 많았어. 그때 너 짝사랑하던 애들도 몇 명 있었는데 눈치 못 챘냐?”

“……진짜?”

“반 애들 다 알고 있던데 왜 너만 몰랐냐.”

젠장. 일찍 좀 얘기해 주지……가 아니라, 지금은 송이 씨가 있으니 상관없다. 일편단심. 운명의 상대를 만난 지금은 아무래도 좋다.

“조만간 한번 뭉치기로 했는데 부르면 나와라. 네 팬클럽 얼굴도 좀 보고. 오케이?”

“오, 오케이.”

그래, 얼굴만 보는 건데 뭘. 단순한 동창일 뿐이야.

엉겁결에 대답한 내게 피식 웃어 보인 지훈이가 운전석 문을 열다 말고 멈칫했다.

“만나서 반가웠다.”

“어? 어, 그래.”

“또 보자.”

부우웅.

커다란 엔진음과 함께 멀어지는 차를 보며, 문득 어떤 생각이 들었다.

“그런데 저 녀석, 나랑 이 정도로 친했었나?”



* * *



“아주 죽마고우가 따로 없더라.”

“누구? 아, 태경이?”

“그 사람 말고 누가 있어?”

“말투가 왜 그래. 마음에 안 들었어?”

“응, 오빠 친구라서 말하기 그랬는데. 솔직히 좀 그렇더라.”

“이상하네. 걔 어릴 때 진짜 인기 많았는데.”

“왜?”

“이유야 많지. 키 크고 덩치 좋고 운동도 엄청 잘했고. 또 얼굴도 그만하면 잘생긴 편이잖아. 연애 쪽으로는 영 눈치가 없는 게 문제지만.”

“흠. 나는 별로던데. 보고 있으면 너무 날백수 느낌 나지 않아? 그 사람 직업 뭐래?”

“음. 그걸 안 물어봤네. 저 녀석 어릴 때는 체육 교사가 꿈이었으니까 그쪽으로 가지 않았을까.”

“스물일곱에 남자니까…… 아직 대학생? 고시생?”

“모르지, 나도.”

“오빠랑 만나서 그런가, 다른 남자들은 눈에 안 차. 미남에 성격 좋지, 능력도 완전 최고잖아.”

“립 서비스라도 듣기 좋네.”

“그런 거 아닌데? 허우대만 멀쩡한 그 친구보다 오빠가 백배는 나아.”

“그렇게 말하지 마. 좋은 녀석이야.”

“10년 만에 만난 거라며. 심지어 연락도 그쪽에서 먼저 끊었고. 근데도 그렇게 말해 줄 정도로 절친이었어?”

박지훈이 부드럽게 웃었다.

“아니. 전혀.”



* * *



“어떠세요?”

부동산 아저씨가 가래 낀 목소리로 물었다. 나를 기다리며 한 시간이나 줄 담배를 태웠다는 그의 안색은 영 좋지 않았다.

“좋네요.”

빈말이 아니다. 넓은 잔디 마당이 딸린 2층짜리 단독 주택은 지금까지 본 어느 집보다 좋았다.

‘방 네 개에 화장실 두 개. 거실도 넓고.’

동화 속에 나오는 집이 따로 없다. 나는 옆에서 자세하게 설명해 주는 부동산 아저씨의 말을 주워들으며 집을 구경하고 대문을 나섰다.

“이런 매물 구하기 쉽지 않거든요. 지금 집주인이 건물 몇 개 가지고 있는 양반인데, 이번에 인천에 빌딩 올린다고 급매로 내놨어요.”

“그래서 시세가?”

“인터넷에서 보신 그대로. 33억 8천.”

여전히 욕 나오는 금액이지만 그만큼 충분한 값어치가 있다.

가족들의 안전, 그리고 우리에겐 남다른 의미가 있는 곳이니까.

“연락해 주세요.”

“그럼……?”

“사겠습니다.”

“아이고, 잘 생각하셨습니다. 사장님!”

나는 아저씨가 내민 손을 굳게 맞잡았다.

“그런 의미에서 근처 한 번 더 돌아봐도 될까요?”

“…….”

“농담입니다.”

그거 한마디 했다고 손에 힘 들어가는 것 봐라.



* * *



“조심히 들어가십시오.”

“네, 수고하세요.”

10%의 계약금을 걸어 두고 부동산을 나섰다. 집주인과는 조만간 날짜를 잡아 정식으로 매입 절차를 진행하기로 이야기가 됐다. 저쪽도 급전이 필요한 만큼 빠르게 얘기가 끝났다.

‘이사는 좀 미뤄야겠고.’

지금 가족들이 사는 집에서 한 시간 정도 거리가 있다 보니 매입했다곤 해도 당장 이사하기에는 무리다.

무엇보다 올해에는 하연이의 수능이 있으니까.

이사는 그 직후 깜짝 발표 할 거다.

‘리모델링도 해야지.’

가급적 옛날 그 시절의 집과 흡사하게 만들어 볼 생각이었다. 아주 오래전 일이긴 해도 16년이나 살았기 때문인지 집 구조는 똑똑히 기억난다.

‘정식 계약도 하고, 인테리어 업체도 알아보고…… 또 뭐가 있지?’

게이트에서 창질이나 할 줄 알지, 이쪽으로는 생초짜나 다름없다. 도통 뭐부터 해야 할지 감이 안 잡힌다.

이런저런 생각을 하며 어둑한 골목길로 접어든 그때였다.

‘음?’

목덜미가 간질거린다. 솜털이 곤두서고 공기가 뒤바뀐 느낌.

등 뒤로 누군가의 은밀한 시선이 느껴졌다.

‘인벤토리 오픈. 소환.’

번개처럼 돌아서는 내 손아귀에는 단검 한 자루가 들려 있었다. 그러나…….

미야옹.

“뭐야. 고양이야?”

야옹.

얼룩덜룩한 고양이 한 마리가 담벼락에서 폴짝 뛰어내렸다.

나를 슬쩍 바라본 녀석이 어슬렁거리며 사라진다.

‘너무 과민 반응 한 건가?’

감각이 상승함에 따라 한층 예민해지긴 했다. 성장과 동시에 차차 익숙해져야 하는데, 지금의 나는 성장 속도가 너무 빠르니 보니 적응 기간이 무의미했다.

‘아니, 이번에는 느낌이 좀 이상했는데.’

뒤늦게 [기감]을 끌어 올려 봤지만 인적 없는 골목길에는 아무것도 존재하지 않았다.

삑.



- [기감]으로 탐색할 수 있는 대상이 없습니다.



시스템이 그렇다면 그런 거겠지. 확실히 요즘 피곤하긴 한 모양이다.

“아, 갑자기 삼계탕 확 땡기네.”

생각난 김에 가족들이랑 다 같이 외식이나 할까?

야들야들한 살코기와 뜨끈한 국물을 생각하니 발걸음이 가벼워진다.



* * *



어두운 골방, 명상에 잠겨 있던 청년이 번쩍 눈을 떴다.

“헙!”

아무렇게나 뻗친 머리는 땀에 젖었고 숨은 거칠다. 허겁지겁 생수를 들이켠 그가 안도의 한숨을 내쉬었다.

“어우, 씨발. 깜짝 놀랐네.”

모든 게 순탄했다. 아니, 지루할 정도였다.

조사 대상은 마침 휴가 중이었고 이동 동선은 뻔했다. 집, 편의점, 집. 오늘은 그나마 한 시간 거리나 이동했지만 추적에는 무리가 없었다.

그런데…….

“저 새끼 뭐야? 왜 거기서 갑자기 뒤를 돌아보고 지랄이야 지랄이.”

날카로운 눈초리를 본 순간 심장이 덜컥 내려앉았다. 황급히 고양이와 링크(Link)를 끊지 않았다면 정말 들켰을지도 모르는 일이다.

“알고 그런 건 아니겠지?”

조사 대상은 C급 헌터에 불과하다. 지금까지 조사해 왔던 놈들에 비하면 한참 급이 떨어진다.

‘그럴 리가 없지. 내가 누군데.’

B급 마법사이자 정보 상인인 홍우진은 고개를 저었다.

그는 추적, 감시 마법의 달인이다. 화려한 공격 마법은 쓰지 못해도 이 분야에서만큼은 최고라는 자부심이 있었다.

“맞아. 그럴 리 없어. 그냥 우연이야, 우연.”

주문처럼 중얼거리는 홍우진. 그의 목소리에는 불안함이 깃들어 있었다.
```

## Final English reading copy

```markdown
# Chapter 91

“Do you know me?”

I asked the approaching man a question in return.

“Who are you?”

*At least introduce yourself before asking something like that, shouldn’t you?*

Maybe my bewilderment had shown clearly on my face, because the man slid his dark sunglasses down. A handsome face with a lightly tanned complexion appeared beneath them.

“Park Jihoon.”

Park Jihoon? Well, it wasn’t as if I had only met one or two people over the years.

More importantly, I didn’t recognize him at all.

“I’m sorry, but I think you have me confused with someone else.”

“I don’t. It’s definitely you. Didn’t you attend Garam Middle School?”

“Huh?”

That was the name of the school I had attended. I had moved away before graduating and lost touch with everyone there, but my memories of it were still vivid.

“Right? Garam Middle School. You’re twenty-seven this year.”

“Yes, that’s true, but…”

“Then it is you! Jin Taekyung from Class 6, Third Year!”

He even remembered my name, grade, and class—details I barely remembered myself.

At that point, I couldn’t deny it. I asked the sunglasses-wearing man, who was grinning from ear to ear,

“…Do you really know me?”

“I’m Jihoon. Park Jihoon! We played soccer together all the time in middle school! We were always getting called to the homeroom teacher’s office because we were bad at studying, and then the two of us would get smacked around. You don’t remember?”

Soccer? Getting beaten by our homeroom teacher?

I opened my mouth, wondering if it could really be him.

“Park Jihwang?”

“That’s right, you punk. I’m Park Jihwang! Ah, right. You wouldn’t know that I changed my name.”

“Of course I wouldn’t.”

I didn’t know Park Jihoon, but I knew Park Jihwang.

I never expected to meet one of my middle school classmates here. A smile naturally spread across my face.

“Wow, meeting you here. Some guy I’d never seen before came up and acted like he knew me, so I was wondering what was going on.”

“Shouldn’t you have recognized me anyway? It’s not like we were in kindergarten together. It was only ten years ago.”

“Even if it had only been five years, I wouldn’t have recognized you. Your face has changed too much.”

“Has it? Ha-ha.”

It was an undeniable fact. The scrawny kid with the dark complexion had turned into someone who could probably be called handsome wherever he went.

“You didn’t just get better-looking. You got a better body, too?”

“Oh, you have a good eye.”

“It’s basic observation.”

As far as I remembered, he had been about a head shorter than me. Now, our eye levels were roughly the same.

“Damn, you really made it big.”

An unrecognizably changed face, a solid build, a pretty girlfriend, and a foreign car that looked like it would easily cost a hundred million won.

Jihwang—or Jihoon—had changed a great deal in the ten years since we had last met. And I knew why.

*This guy is a Hunter, too.*

Now that my Qi Sense had reached a higher realm, I could assess people even without using the System.

*Is it that I can feel his qi?*

There was no doubt about it. He was a Hunter. He seemed about as strong as Im Changsoo—or perhaps even stronger.

*A friend I haven’t seen in ten years turns out to be a Hunter. How strange.*

I could even use Qi Sense to read his Level, but I didn’t feel like going that far.

I had met an old friend in a place filled with memories. Right now, I was neither a Hunter nor a martial artist.

I was just an ordinary Jin Taekyung.

“Anyway, it’s really good to see you. You know I was really upset when we lost touch right after you transferred, right?”

“Was I? Things were so chaotic back then.”

I had been sixteen at the time. I was right in the middle of adolescence, and my head had been a mess because my father had just died.

After entering high school, I focused entirely on training with the goal of attending a college of physical education. I naturally lost touch with the friends I had known before.

“Ah, right. Things were like that back then. I’m sorry.”

Maybe he thought he had made a mistake, because Jihwang’s—or Jihoon’s—smile turned awkward.

“What are you apologizing for? It was my fault for not getting in touch sooner. But do you still live around here?”

“My whole family lives in Seoul now. I stopped by because I remembered this place while returning from a trip with my girlfriend.”

“Wow. What a triumphant return.”

“Don’t make it sound so embarrassing. I still have a long way to go before I can call myself successful.”

“You’ve already succeeded plenty. What more could you want?”

We continued talking with smiles on our faces. Most of what we discussed were memories from middle school, but that alone was enough to make the time enjoyable.

A considerable amount of time passed before Jihoon’s girlfriend subtly hinted that her legs were hurting.

“Oppa, my legs hurt.”

“Hm? Then do you want to wait in the car? I’ll talk a little longer and be right there.”

“…Is that really something you should say?”

I had no intention whatsoever of interfering with my friend’s love life, so I took the hint and waved my hand.

“No, let’s talk about the rest next time.”

“Next time? Didn’t you say something like that ten years ago, too? You said you’d contact me next time, then left and never contacted me once.”

I had nothing to say to that. As I stood there smacking my lips, Jihoon held out a business card.

“Forget it. Call this number right now.”

> Myeongdong Guild, Team 1  
> Hunter Park Jihoon

Myeongdong Guild might not have been one of Korea’s top ten Guilds, but it was easily one of the top twenty—a major Guild.

And being part of Team 1 meant he was an elite recognized even within Myeongdong Guild. He could probably transfer to any respectable mid-sized Guild and become a Team Leader without breaking a sweat.

*I expected him to be doing well, but this is more than I imagined.*

I hid my surprise and called the number on the card.

Bzzzz.

Jihoon checked his smartphone and grinned.

“I’ll call you. We have to grab a drink sometime.”

“We’ll see. If I’m busy, I won’t be able to make it. If I have time, I’ll go.”

“What kind of answer is that? Your name came up at the last class reunion. People were asking what you were doing these days.”

“My name came up?”

“Why do you sound so surprised? You were popular with the other kids.”

“Was I? I spent all day on the field, so I guess I was friendly with the boys, at least.”

“You were popular with the girls, too. There were a few girls who had crushes on you back then. You never noticed?”

“…Really?”

“Everyone in the class knew. Why were you the only one who didn’t?”

*Damn. They should’ve told me sooner…*

No, that didn’t matter now that I had Ms. Songi. I was devoted. Now that I had met my destined partner, none of that mattered.

“We’re planning to get together soon, so come if I call you. You can meet your fan club, too. Okay?”

“O-Okay.”

*Yeah, I’m only going to see their faces. They’re just old classmates.*

Jihoon gave me a quiet laugh, then opened the driver’s-side door before suddenly stopping.

“It was good seeing you.”

“Huh? Oh, yeah.”

“See you again.”

Vroom.

As I watched the car disappear with the roar of its large engine, a thought suddenly occurred to me.

“Were we really that close?”

* * *

“They really seemed like childhood best friends.”

“Who? Oh, Taekyung?”

“Who else would I be talking about?”

“Why are you talking like that? Did you not like him?”

“Yeah. I didn’t want to say it because he’s your friend, Oppa, but honestly, he was kind of off.”

“That’s strange. He was really popular when he was young.”

“Why?”

“There were plenty of reasons. He was tall, had a good build, and was great at sports. He wasn’t exactly bad-looking, either. His only problem was that he was completely oblivious when it came to romance.”

“Hmm. I didn’t care for him. Doesn’t he look too much like a complete unemployed bum? What does he do for a living?”

“Hmm. I forgot to ask. He dreamed of becoming a physical education teacher when he was young, so maybe he went into that field.”

“He’s twenty-seven, though, and a man… Is he still in college? Studying for some exam?”

“I don’t know. Neither do I.”

“Maybe it’s because I’m with you, but other men don’t catch my eye. You’re handsome, kind, and incredibly capable.”

“Even if it’s just lip service, that’s nice to hear.”

“I’m not saying it just to flatter you. You’re a hundred times better than that friend of yours who only looks presentable.”

“Don’t say that. He’s a good guy.”

“You said it was the first time you’d met in ten years. He was even the one who stopped contacting you first. Were you really that close that you still speak well of him?”

Park Jihoon smiled gently.

“No. Not at all.”

* * *

“What do you think?”

The real estate agent asked in a phlegmy voice. He had chain-smoked for an hour while waiting for me, and his complexion looked terrible.

“It’s nice.”

I wasn’t just being polite. The two-story detached house with a broad lawn was better than any house I had seen so far.

*Four bedrooms and two bathrooms. The living room is spacious, too.*

It looked like something out of a fairy tale. I toured the house while listening to the real estate agent explain every detail, then stepped out through the front gate.

“Listings like this are hard to find. The current owner has several buildings, but he’s putting this one up as a quick sale because he’s planning to put up another building in Incheon.”

“So what’s the market price?”

“Exactly what you saw online. 3.38 billion won.”

It was still an amount that made me want to swear, but the house was worth every bit of it.

For my family’s safety, and because this place held special meaning for us.

“Please contact me.”

“Then…?”

“I’ll buy it.”

“Oh, you’ve made a wonderful decision, Boss!”

I firmly shook the hand the man held out.

“Since we’re on the subject, would it be all right if I took another look around the neighborhood?”

“…”

“I’m joking.”

Just because I had said one thing, look at how tightly his hand clenched.

* * *

“Have a safe trip home.”

“Yes. Take care.”

I left the real estate office after putting down the ten-percent deposit. I had agreed with the owner to set a date soon and proceed with the formal purchase. Since he needed cash quickly, the negotiations had moved along fast.

*I’ll have to put off moving for a while.*

The house was about an hour away from where my family lived now. Even though I had purchased it, moving immediately would be difficult.

More importantly, Hayeon had her college entrance exam this year.

I would surprise them with the news immediately afterward.

*I’ll have to remodel it, too.*

I intended to make it as similar as possible to our old home. It had happened a very long time ago, but perhaps because we had lived there for sixteen years, I remembered the layout perfectly.

*I’ll sign the formal contract and find an interior contractor… What else is there?*

I knew how to wield a spear in a Gate, but I was a complete novice when it came to this sort of thing. I had no idea where to start.

I was turning into a dark alley while thinking about this and that when—

*Hm?*

The back of my neck began to tingle. The fine hairs on my body stood up, and it felt as if the air had shifted.

I sensed someone secretly watching me from behind.

*Open Inventory. Summon.*

I spun around like lightning, a dagger already in my hand. But then…

Meow.

“What the hell? A cat?”

Meow.

A mottled cat jumped down from the wall.

It glanced at me, then slowly wandered away.

*Was I overreacting?*

As my senses improved, I had become more sensitive. I was supposed to gradually grow accustomed to it alongside my growth, but my growth had been too fast for any adjustment period to have meaning.

*No. It felt strange this time.*

I belatedly raised my Qi Sense, but there was nothing in the deserted alley.

Beep.

> **System**
>
> There are no targets for **Qi Sense** to detect.

If the System said that was the case, then it must be true. I must have been especially tired lately.

“Ah, now I suddenly have a craving for samgyetang.[^1]”

Since I had thought of it, should I go out to eat with my family?

Thinking about tender meat and hot broth made my steps feel lighter.

[^1]: Samgyetang is Korean ginseng chicken soup, traditionally served hot.

* * *

In a dark little room, a young man who had been meditating suddenly opened his eyes.

“Gasp!”

His hair stuck out in every direction, soaked with sweat, and his breathing was ragged. He hurriedly drank bottled water, then let out a relieved sigh.

“Fuck, that scared the hell out of me.”

Everything had gone smoothly. No, it had been boring enough to be tedious.

The investigation target happened to be on vacation, and his movements were predictable. Home, convenience store, home. Today, he had traveled as far as an hour away, but tracking him had still been no trouble.

But then…

“What the fuck was that? Why did that bastard suddenly turn around and start pulling that shit?”

The moment he saw that sharp gaze, his heart had dropped. If he had not hurriedly severed the Link with the cat, he might really have been discovered.

“He didn’t know, did he?”

The target was only a C-rank Hunter. Compared to the people he had investigated until now, he was far below them.

*There’s no way. Who do you think I am?*

Hong Woojin, a B-rank mage and information broker, shook his head.

He was a master of tracking and surveillance magic. He could not use flashy attack magic, but when it came to this field, he took pride in being the best.

“That’s right. There’s no way. It was just a coincidence. A coincidence.”

Hong Woojin muttered the words like a mantra. Anxiety lingered in his voice.
```
