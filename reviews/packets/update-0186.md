<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0186.txt",
      "sha256": "ecb79a33b43a04336a661c0af85e909a414825b53b480b97ddaed173d7673d85",
      "bytes": 16497
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "a7ada1ee6585d9076e3dc971bd86aef7a8697407b313fa12f4c0e83cf8d99d7e",
      "bytes": 4429
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "c3704c23e3351ab81ccdfcdd37a07ab67655d0e06e25b4ff29f968fc3722abec",
      "bytes": 46481
    },
    {
      "path": "characters/Baek Museong.md",
      "sha256": "0a7bad42d7c3b4a87ae5c649efcf015c6b1ec61a0fb6b25657f673030d97cdda",
      "bytes": 781
    },
    {
      "path": "characters/Cheongpung.md",
      "sha256": "4528b9433f493e7fdc295e154b3d2dba2d7ab86ad4be5fb8c8292da40f0655a2",
      "bytes": 2091
    },
    {
      "path": "characters/Chulwoo.md",
      "sha256": "3c7694c8f4cdc986c3db6ec3f3fec6463e3b9035a2a4bd6945cb5ff92f5cd575",
      "bytes": 845
    },
    {
      "path": "characters/Eunhyang.md",
      "sha256": "d3c2256ab9d542410bb52d4bd05edab09e671dbfef68897cc9cdc91bc9cd87e0",
      "bytes": 743
    },
    {
      "path": "characters/Gong Yacheong.md",
      "sha256": "19ac5040549fe4decaabd093d5d6227c89928bb71bf75be3c952255b8d0e6877",
      "bytes": 2150
    },
    {
      "path": "characters/Hyuk Mujin.md",
      "sha256": "1627260d68c82240669cf69168c32d001cdb5a6be4c5abc7200235e5ff02d16c",
      "bytes": 5558
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "517fd3ee9d6824ada97dcf7a6ef4950d44bee596ed7821cafb8520ff632e213b",
      "bytes": 24938
    },
    {
      "path": "characters/Jin Wikyung.md",
      "sha256": "6188f2cac5747ccbcb28c7ad9677cbca48fb9cad74c723f7f5c801d91d74f2af",
      "bytes": 8199
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "e619f4272cd8181d515c691e9cdf7a9488ba98ea320c098a142f1b063aedde0c",
      "bytes": 622
    },
    {
      "path": "characters/Socheon.md",
      "sha256": "dbdb0d09cddd26e65a33d82dab59d67bd766b9697378ad8831e7fe4726c44091",
      "bytes": 1704
    },
    {
      "path": "characters/Soyul.md",
      "sha256": "e24e5f11970d4ff15222434835d67443345919f1a00061b4b5142b1286e4c032",
      "bytes": 1610
    },
    {
      "path": "characters/Wipeng.md",
      "sha256": "abd51bb62bb25c4580634ca7381a33695a12665a00c68f462dcf2d4cb3877458",
      "bytes": 4701
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "b12f1d7ddb9eacf7db873687affd2ffd18b09278d30306a349140bf991a73d6a",
      "bytes": 38474
    }
  ],
  "estimated_tokens": 35087
}
-->

# Durable State Update — Chapter 186

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 186. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 20 concise items, `open_questions` to at most 8
items, and `temporary_decisions` to at most 8 items. Keep the serialized context
under 16384 UTF-8 bytes. Use only chapter
numbers through 186. `profile_updates` may replace one exact, uniquely occurring
complete line in a listed profile, and only an Aliases, Role, Personality, Voice, or
Relationships line. Use `profile_creations` only for a newly introduced named
character without a listed profile. Filenames must be plain `.md` basenames.
`names` contains only newly required Korean-to-English rows; Korean keys must occur
in the source. `address_pairs` contains only newly required speaker→addressee rows;
each Korean key must occur in the source or already appear in the address ledger,
and at least one endpoint must occur in the source (first-person narrators may be
ledger-only). Speaker and addressee must be Hangul source spellings (Arabic digits
allowed in titles such as 1팀장; do not romanize). Do not invent risk-register rows. Beat
plot paragraphs are plain strings; continuity and translation decisions are concise
list items.
Return this exact shape:

{
  "chapter": 186,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 186,
    "continuity_sources": [186],
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
    "Jin Wikyung has led the Jin Family in place of the absent Family Head for two years and established it as Shanxi Murim's hegemon.",
    "The Jin Family is holding a three-day grand banquet beginning on New Year's Day, with support from Huashan, the imperial family, and Shanxi Murim.",
    "Jin Wikyung and Wolhwa finalized a cooperative alliance between the Jin Family and the Lower District Sect.",
    "The Heavenly Wind Band was annihilated near Datong by an unknown Supreme Peak master; Jin Taekyung privately suspects Mae Jonghak.",
    "Jin Taekyung is absent while having a weapon forged and has stopped sending news; Jin Mukyung is undergoing seclusion training after enlightenment.",
    "Woo Hwangtae sought an audience and apology regarding Woo Jintae, became enraged at the Jin Family's representatives, and was prevented from escalating the conflict.",
    "Baek Museong and the Huashan group are present at the Jin Family; Baek has formally greeted Cheongpung as his Martial Uncle and is leading the effort to return him to Huashan.",
    "The Treasured Jade remains missing.",
    "Jang Taebo is forging Taekyung's commissioned weapon.",
    "Chulwoo is the second of the Three Plum Blossom Elites, bears the epithet Defeated Flower Fist, is a Level 95 early-Peak martial artist, fought Taekyung, and has now apologized after failing to recognize Cheongpung as his Martial Uncle.",
    "Eunhyang is the youngest junior disciple in Baek Museong's group, bears the epithet Flower Sword Phoenix, and was found after becoming separated in the crowd.",
    "Taekyung, Hyuk Mujin, and Cheongpung returned to Taiyuan after three days away.",
    "Taekyung is temporarily carrying Jeok Cheongang's Unnamed Sword outside his inventory; Cheongpung has speculated that Jeok may want Taekyung as his Disciple.",
    "The Heavenly Sword True Person is Cheongpung's eldest Senior Brother by generation and ordered him to return to Huashan; Cheongpung refused and chose to remain with Taekyung.",
    "Cheongpung is Mae Jonghak's grandson and Disciple; Baek Museong is his Martial Nephew through the current Huashan Sect Leader.",
    "Cheongpung never underwent Huashan's initiation ceremony and is technically an outsider despite possessing Huashan's treasured arts.",
    "At the Jin Family gathering, Taekyung was mobbed by Shanxi power players, including Jang Se-pal, leader of the small Hequ Sect, and received multiple marriage proposals.",
    "Gong Ilhyuk has told the Roaring Fury Swordsman that Cheongpung is the Sword Saint's Disciple and is leading the elder toward the Jin Family's gathering.",
    "The Roaring Fury Swordsman is a fiery-tempered elder of the Zhongnan Sect who has decided to verify Cheongpung's identity and confront the Jin Family's gathering.",
    "Jeok Cheongang, the Fire King, entrusted Taekyung with a sword and a martial arts manual."
  ],
  "continuity_sources": [
    185
  ],
  "open_questions": [
    "Who annihilated the Heavenly Wind Band near Datong?",
    "What consequences will follow Taekyung's absence from the Jin Family's grand banquet?",
    "When will Jang Taebo complete Taekyung's weapon?",
    "Who has the Treasured Jade, or was it lost by Jopil?",
    "Does Jeok Cheongang actually intend to take Taekyung as his Disciple?",
    "What consequences will follow Woo Hwangtae's conflict with Chulwoo and the Jin Family?",
    "Will Taekyung help Baek Museong return Cheongpung to Huashan?",
    "What will the Roaring Fury Swordsman do when he reaches the Jin Family's gathering?"
  ],
  "safe_through": 185,
  "temporary_decisions": [
    "Render 원단 as “New Year's Day” and 천풍단 as “Heavenly Wind Band.”",
    "Render 천검진인 as “Heavenly Sword True Person,” 매화삼절 as “Three Plum Blossom Elites,” 화산파 일대 제자 as “First-generation Disciple of Huashan,” and 사숙 as “Martial Uncle.”",
    "Render 수문각 as “Gate Guard Pavilion” and 장주 as “Lord.”",
    "Render 패화권 as “Defeated Flower Fist” and 산서기협 as “Shanxi Extraordinary Hero.”",
    "Render 절정 초입 as “early Peak” and 권기 as “fist qi.”",
    "Render 노호검객 as “Roaring Fury Swordsman,” 하곡문 as “Hequ Sect,” and 양천 as “Yangcheon.”",
    "Render 청성파 as “Qingcheng Sect” and 집법원 as “Disciplinary Hall.”"
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
| 박지훈 | **Park Jihoon** | Current name of Taekyung's former middle-school classmate; Hunter in Myeongdong Guild Team 1. |
| 박지황 | **Park Jihwang** | Jihoon's former name, revealed when Taekyung recognizes him. |
| 가람중 | **Garam Middle School** | Middle school attended by Taekyung and Jihoon. |
| 명동 길드 | **Myeongdong Guild** | Large Guild in which Jihoon belongs to Team 1. |
| 1팀장 | **Team 1 Leader** | Sangdong Guild's Team 1 leader and its only A-rank Hunter besides Im Chunsoo. |
| 희망 고시원 | **Hope Goshiwon** | The goshiwon listed as Taekyung's residence in the target report. |
| 기감 | **Qi Sense** | Taekyung's sensory technique; its range reaches seventy meters in this chapter. |
| 집파리 | **Housefly** | System label for a Level 1 fly familiar. |
| 검정파리 | **Black Blow Fly** | System label for a Level 1 fly familiar. |
| 금파리 | **Green Bottle Fly** | System label for a Level 1 fly familiar. |
| 패밀리어 | **Familiar** | System classification for the flies detected in Taekyung's home. |
| 김선희 | **Kim Seonhee** | Assistant Manager at the Ilsan Store |
| 대리 | **Assistant Manager** | Corporate title used by Kim Seonhee |
| 일산 | **Ilsan** | Location of the Store and Lafesta |
| 라페스타 | **Lafesta** | Shopping and entertainment district in Ilsan |
| 스토어 | **Store** | Restricted luxury retailer for magical goods and Hunter equipment |
| 쌀벌레 | **Rice Weevil** | Creature used by Hong Woojin as a Familiar |
| 링크 | **Link** | Mental connection between a mage and Familiar |
| 김희선 | **Kim Seonhee** | Source spelling variant for the established Assistant Manager Kim Seonhee at the Ilsan Store. |
| 여름이 | **Yeoreum** | Name Hayeon gives to the Level 2 kitten. |
| 김준수 | **Kim Junsu** | C-rank mental mage and Sangdong Guild Security Team’s sole Familiar mage. |
| 김권동 | **Kim Gwondong** | C-rank Sangdong Guild Security Team Hunter assigned to surveillance and disguise work. |
| 나비 | **Nabi** | Name used for the black kitten Familiar. |
| 고양시 | **Goyang** | City where the target previously visited a real-estate office. |
| 보안팀 | **Security Team** | Sangdong Guild’s surveillance and protection unit. |
| 보안팀장 | **Security Team Leader** | Unnamed leader coordinating the operation. |
| 최병일 | **Choi Byungil** | B-rank Security Team leader; his Level is in the mid-sixties. |
| 박형진 | **Park Hyungjin** | One of the C-rank Sangdong Guild watchers. |
| 오규현 | **Oh Gyuhyeon** | One of the C-rank Sangdong Guild watchers. |
| 이민철 | **Lee Mincheol** | One of the C-rank Sangdong Guild watchers. |
| 교관 | **Instructor** | Kim Hwajong's former Hunter Training Center role and address. |
| 헌터 훈련소 | **Hunter Training Center** | Training institution where Kim Hwajong served as an instructor. |
| 1번 훈련생 | **Trainee Number One** | Im Chunsoo's training call sign during his forced military identification. |
| 28연대 1대대 2중대 | **28th Regiment, First Battalion, Second Company** | Military unit designation shouted during Im Chunsoo's identification. |
| 사도세자 | **Crown Prince Sado** | Joseon crown prince used in the comparison for Jinho's haggard appearance; footnoted. |
| 박혁거세 | **Park Hyeokgeose** | Legendary founder of Silla, used in the comparison to Jinho emerging from the capsule; footnoted. |
| 열양공 | **heat-yang technique** | Mukyung's heat-based internal-energy technique. |
| 옥황상제 | **Jade Emperor** | Daoist deity invoked in Hyuk Mujin's prayer. |
| 원시천존 | **Primordial Heavenly Venerable** | Daoist deity invoked alongside the Jade Emperor. |
| 항산검문주 | **Sect Leader of the Mount Heng Sword Sect** | Title for Lee Seowol, the sect's current leader. |
| 산서제일미 | **Shanxi's foremost beauty** | Former reputation of Taekyung's mother. |
| 봉황객잔 | **Phoenix Inn** | Famous Shanxi inn with luxurious lodging, imperial-court cuisine, and a beautiful proprietress. |
| 계용옥미갱 | **chicken-and-corn soup** | Egg-thickened corn soup. |
| 계용옥미앵 | **chicken-and-corn soup** | Source spelling variant of 계용옥미갱 for the same dish. |
| 광수 | **Gwangsu** | First attacker at the Phoenix Inn; identified by the others after Taekyung punches him. |
| 적풍단 | **Red Wind Band** | Rising mounted-bandit power from the northern plateau. |
| 적풍단주 | **Red Wind Band Leader** | Unnamed leader of the Red Wind Band; commands two hundred followers. |
| 관제묘 | **Guandi Temple** | Shrine type mentioned in martial-arts novels. |
| 흑도 | **dark-path figures** | Generic category of underworld martial forces. |
| 오색귀 | **Five-Colored Ghosts** | Nickname for the five former subordinates of Jang Sam. |
| 이삼 | **Lee Sam** | Leader of the ten-man human-trafficking group; his Level window identifies him by this name. |
| 추종향 | **tracking scent** | Scent used to guide the messenger hawk. |
| 대동 | **Datong** | Shanxi location containing the Mount Heng Sword Sect branch destroyed by the Red Wind Band. |
| 토호단 | **Earth Tiger Band** | Mounted-bandit group formerly led by Pung Yang's subordinate. |
| 풍양 | **Pung Yang** | Personal name of the Red Wind Band Leader. |
| 춘삼 | **Chunsam** | Lower District Sect martial artist serving as the carriage driver. |
| 철검대주 | **Iron Sword Squad Leader** | Title of the Mount Heng Sword Sect's Iron Sword Squad leader. |
| 대항산검문 | **great Mount Heng Sword Sect** | Expanded organizational form used for the Mount Heng Sword Sect. |
| 대동지부 | **Datong Branch** | Mount Heng Sword Sect branch in Datong. |
| 소월 | **Seowol** | Short form of Lee Seowol used by Cheol Mubaek. |
| 철 숙부 | **Uncle Cheol** | Lee Seowol's familial address for Cheol Mubaek. |
| 철 대협 | **Great Hero Cheol** | Respectful address for Cheol Mubaek. |
| 아가씨 | **Young Lady** | Former address used for Lee Seowol before she demands the title Sect Leader. |
| 문주님 | **Sect Leader** | Honorific title Lee Seowol orders the senior figures to use. |
| 산서괴협 | **Strange Hero of Shanxi** | Epithet referenced for the absent martial artist. |
| 녹림맹주 | **Green Forest Alliance Leader** | Leader title for the Green Forest Alliance. |
| 장강수로맹주 | **Alliance Leader of the Yangtze River Channel League** | Leader title for the Yangtze River Channel League. |
| 사마외도 | **demonic, heterodox arts** | Suspected martial-arts origin of Pung Yang's insidious forms. |
| 전서구 | **messenger pigeon** | Pigeon delivering the Lower District Sect's Jeongyang Branch report. |
| 절정 초입 | **early Peak** | Pung Yang's specific stage within the Peak realm. |
| 광칠이 | **Gwangchil** | Former mounted-bandit boss who took in Pung Yang and was later killed by a First Rate master. |
| 일류 초입 | **early First Rate** | Early stage of the First Rate realm. |
| 수라멸권 | **Shura Annihilating Fist** | Cheol Mubaek's single-successor martial art. |
| 항산권문 | **Mount Heng Fist Sect** | Alternate fist-sect designation used by Pung Yang for the Mount Heng defenders. |
| 화시 | **fire arrow** | Flaming arrow Lee Seowol fires to signal Cheol Mubaek. |
| 벽곡단 | **fasting pills** | Food-substitute pills found in the hidden cave where Cheol trained. |
| 잠력단 | **Temporary Strength Pill** | Rare pill that temporarily enhances strength; Pung Yang has only three and uses one against Cheol Mubaek and another during the battle. |
| 적혈십이검 | **Crimson Blood Twelve Swords** | Peak-level martial arts manual discovered by Pung Yang. |
| 적혈심법 | **Crimson Blood Cultivation Technique** | Cultivation technique discovered by Pung Yang. |
| 검강 | **Sword Force** | Higher manifestation than Sword Energy; Pung Yang's is explicitly imperfect because of insufficient enlightenment. |
| 태산압정 | **Mount Tai Presses Down on the Crown** | First move of the Three Calamities Sword Technique. |
| 나려타곤 | **Narye tagon** | Humiliating idiom comparing a fighter's evasive roll to a lazy donkey rolling on the ground. |
| 호신강기 | **Body-Protecting Qi** | Powerful defensive qi barrier that shields Pung Yang. |
| 격산타우 | **Striking the Ox Across the Mountain** | Palm technique that transmits force through an intervening defense. |
| 북망산 | **Mount Beimang** | Mountain associated with burial grounds; used as a threat to send someone to their death. |
| 열화신단 | **Blazing Flame Divine Pill** | Dangerous elixir that grants half a jiazi of internal energy while risking death from its fire qi. |
| 적혈십이도 | **Crimson Blood Twelve Sabers** | Pung Yang's domineering saber art; he has reached approximately seventy percent mastery. |
| 영단 흡수 | **Divine Pill Absorption** | System Quest created after Jin Taekyung takes the Blazing Flame Divine Pill. |
| 내상 | **Internal Injury** | System condition label for internal injury. |
| 중상 | **Severe Injury** | System condition label causing a major drop in all stats. |
| 이름 없는 검 | **Unnamed Sword** | Oldest inventory item summoned when no item named 아무거나 can be found. |
| 만년한철 | **Ten-Thousand-Year Cold Iron** | Material that destroys Pung Yang's Body-Protecting Qi when the Unnamed Sword satisfies a specific condition. |
| 완전 회복 | **Full Recovery** | Immediate Quest success reward that heals Taekyung's injuries. |
| 뛰어난 금창약 | **Superior Wound Medicine** | Quest reward used to treat external injuries. |
| 십년하수오 | **Ten-Year He Shouwu** | Quest reward used to treat internal injuries. |
| 어제의 적, 오늘의 동지 | **Yesterday's Enemy, Today's Ally** | Quest completed when Taekyung delivers Wikyung's invitation. |
| 회광반조 | **final rally** | Terminal burst of apparent vitality before death. |
| 운칠기삼 | **seven parts luck and three parts skill** | Established Korean saying used in Taekyung's reflection. |
| 운구기일 | **nine parts luck and one part qi** | Taekyung's playful variation on 운칠기삼. |
| 혈랑검법 | **Blood Wolf Sword Technique** | Peak sword technique personally created by Lee Cheonbaek. |
| 혈랑보법 | **Blood Wolf Footwork** | Peak footwork technique personally created by Lee Cheonbaek. |
| 산서성 | **Shanxi Province** | Province containing the Lower District Sect branches. |
| 정양지부장 | **Jeongyang Branch Leader** | Leader of the Lower District Sect's Jeongyang Branch. |
| 혼주지부장 | **Honju Branch Leader** | Leader of the Lower District Sect's Honju Branch. |
| 총지부장 | **Chief Branch Leader** | Title Wolhwa holds within the Lower District Sect. |
| 송이 | **Song-i** | Short form used for Song Song; Taekyung's love interest. |
| 진무보법 | **Jin Family's Manoeuvre Technique** | Named Jin Family footwork technique mastered by Taekyung. |
| 조장 | **Captain** | Hyuk Mujin's address for Taekyung as squad leader. |
| 숙부 | **Uncle** | Lee Seowol's shortened address for Cheol Mubaek. |
| 은원 | **gratitude and grudges** | Moral debts that must be repaid. |
| 원단 | **New Year's Day** | The day the Mount Heng Sword Sect will visit Taiyuan. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 시진 | **shichen** | Traditional time unit of approximately two hours. |
| 아이템창 | **Item Window** | System window displaying an item's details. |
| 전서응 | **messenger eagle** | Emergency courier used by the Lower District Sect. |
| 폭혈단 | **Blood-Exploding Pill** | Demonic Cult pill said to kill the user after its time limit. |
| 구주 | **Nine Provinces** | Traditional geographic expression used in a threat. |
| 고원 | **Gaoyuan** | Plateau region in northern Shanxi. |
| 산서제일인 | **Shanxi's Number One** | Jin Wikyung's reputation for physical strength. |
| 금잔디 | **Geum Jandi** | Heroine of Boys Over Flowers, referenced in a sarcastic comparison. |
| 사술 | **dark arts** | Unorthodox means of obtaining power. |
| 마기 | **demonic qi** | Demonic energy discussed as a possible effect of the pill. |
| 선천지기 | **innate qi** | Vital energy said to be damaged by the pill's aftereffects. |
| 소음인 | **Soeumin** | One of the constitutional types in Sasang medicine. |
| 태양인 | **Taeyangin** | One of the constitutional types in Sasang medicine. |
| 주신 | **God of Drinking** | Wipeng's drinking epithet. |
| 야왕 | **Night King** | Rumored epithet for Jin Taekyung in Taiyuan's red-light district. |
| 화북 | **North China** | Regional designation used when discussing Shanxi drinking culture. |
| 산서제일가 | **foremost family in Shanxi** | Description of the Jin Family of Taiyuan's standing. |
| 장 노인 | **Old Man Jang** | Elderly villager who witnesses the Jin Family's arrival. |
| 현령 | **county magistrate** | County official who greets Jin Taekyung and delivers the City Lord's invitation. |
| 성주 | **City Lord** | Official who sends the invitation for a gathering with young prodigies. |
| 적토마 | **Red Hare** | Famous horse used in Hyuk Mujin's exaggerated comparison. |
| 여포 | **Lü Bu** | Historical warrior used in Hyuk Mujin's exaggerated comparison. |
| 성주의 초청 | **The City Lord's Invitation** | System Quest title. |
| 구파일방 | **Nine Sects and One Gang** | Major Murim grouping. |
| 오대세가 | **Five Great Families** | Major Murim grouping. |
| 주씨 | **Zhu** | Surname of the imperial ruling house. |
| 친왕 | **Prince** | Imperial title held by the Shanxi City Lord. |
| 천자 | **Son of Heaven** | Honorific title for the Emperor. |
| 황상 | **Emperor** | Address or reference to the reigning Emperor. |
| 태자 | **Crown Prince** | Title of the Emperor's older brother who was reportedly assassinated. |
| 석칠 | **Seokchil** | Middle-aged porter with nearly twenty years of experience. |
| 성운표국 | **Seongun Escort Bureau** | Escort Bureau in southern Shanxi Province. |
| 송 표두 | **Escort Chief Song** | Unnamed person responsible for the escort run. |
| 연화봉 | **Lotus Peak** | Peak on Huashan from which Cheongpung recently fled. |
| 빙당호로 | **candied hawthorn skewers** | Traditional fruit skewers coated in hardened sugar; explained in a footnote. |
| 하북 | **Hebei** | Province where Hyuk Family Textile Shop has a branch. |
| 혁가 포목점 | **Hyuk Family Textile Shop** | Taiyuan textile shop owned by Hyuk Mujin's parents; the largest in Taiyuan, with branches in Henan and Hebei. |
| 홍화객잔 | **Honghwa Inn** | Inn where Taekyung, Mujin, and Cheongpung dine. |
| 메구미 | **Megumi** | Japanese name used in Taekyung's joke about the abbreviated dish name. |
| 산니백육 | **Garlic Pork** | Boiled pork sliced thin and served with garlic sauce. |
| 어향육사 | **Fish-Fragrant Shredded Pork** | Shredded pork dish. |
| 경장육사 | **Beijing Sauce Shredded Pork** | Shredded pork dish. |
| 규화계 | **Beggar's Chicken** | Named inn dish. |
| 매구 | **Maegu** | Waiter's shortened name for Maechae Guyuk. |
| 매채구육 | **Maechae Guyuk** | Pork belly with preserved mustard greens; the abbreviation is explained in a footnote. |
| 개방 | **Beggars' Sect** | Murim organization counted among the Nine Sects and One Gang. |
| 우진태 | **Woo Jintae** | Heir of the Seongun Escort Bureau and host of the Five Gates scions. |
| 우 소협 | **Young Hero Woo** | Honorific address for Woo Jintae. |
| 황 소저 | **Young Lady Hwang** | Honorific address for an unidentified young woman who is the only daughter of a martial sect. |
| 혁 아우 | **Little Brother Hyuk** | Familiar address for an otherwise unnamed male scion who calls Woo Jintae hyung. |
| 국주님 | **Chief** | Honorific title for the head of an Escort Bureau. |
| 촉금 | **Shu brocade** | Fine brocade brought from Sichuan. |
| 삼도문 | **Samdo Sect** | One of the five former Five Gates sects annihilated at Eight Spring Gorge. |
| 궁귀문 | **Gunggui Sect** | One of the five former Five Gates sects annihilated at Eight Spring Gorge. |
| 성룡이 | **Seongryong** | Name shown in a Level Window; one of the five current Five Gates scions. |
| 천우 | **Cheonwoo** | Name shown in a Level Window; one of the five current Five Gates scions. |
| 명화 | **Myeonghwa** | Name shown in a Level Window; one of the five current Five Gates scions. |
| 소혜 | **Sohye** | Name shown in a Level Window; one of the five current Five Gates scions. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 도동파 | **Dodong Sect** | Fabricated sect claimed by Taekyung when Woo Jintae demands his affiliation. |
| 천진반 | **Tien Shinhan** | Fabricated personal identity claimed by Taekyung. |
| 왕가장 | **Wang Family Estate** | Family estate whose heir is one of the Five Gates scions; he uses sabers rather than sword arts. |
| 왕 공자 | **Young Master Wang** | Heir of the Wang Family Estate. |
| 신 소저 | **Young Lady Shin** | Young woman described as the only daughter of a martial sect. |
| 정 소협 | **Young Hero Jeong** | Address for one injured Five Gates heir; his given name is not stated. |
| 갈 소협 | **Young Hero Gal** | Address for one injured Five Gates heir; his given name is not stated. |
| 석 모 | **Seok** | Self-identification by Honghwa Inn's chief steward; his given name is not stated. |
| 석 총관 | **Chief Steward Seok** | Title and surname form used for Honghwa Inn's chief steward. |
| 칠매검 | **Seven Plum Sword** | Sword art practiced by the unnamed martial official at eight-tenths mastery. |
| 상산왕 | **Prince Shangshan** | The City Lord and a member of the imperial family who orders the luncheon. |
| 정삼품 | **Third-Rank** | Official rank of the unnamed Assistant Military Commissioner. |
| 도지휘첨사 | **Assistant Military Commissioner** | Military office held by the unnamed official responsible for training soldiers. |
| 산서성부 | **Shanxi Provincial Office** | Government office where the City Lord resides west of Taiyuan. |
| 점소이 검신 되다 | **The Shop Assistant Becomes a Sword God** | Wuxia novel title read by Hyuk Mujin. |
| 아파야 무인이다 | **You Must Hurt to Become a Martial Artist** | Wuxia novel title read by Hyuk Mujin. |
| 무림의 아들 걸어서 구주팔황 세 바퀴 반 | **The Son of Murim Walks Three and a Half Rounds Around the Nine Provinces and Eight Wastes** | Wuxia novel title read by Hyuk Mujin. |
| 구주팔황 | **Nine Provinces and Eight Wastes** | Literary geographic phrase appearing in a wuxia novel title. |
| 이풍 | **Li Feng** | Shanxi Province's Assistant Military Commissioner; former Huashan lay disciple |
| 이 첨사 | **Assistant Commissioner Li** | Address form for Li Feng |
| 홍 내관 | **Eunuch Hong** | Eunuch and Deputy Military Commissioner of Shanxi Province |
| 도지휘동지 | **Deputy Military Commissioner** | Second-rank military office held by Eunuch Hong |
| 도지휘사 | **Military Commissioner** | Provincial military commander's office |
| 종남삼수 | **Three Hands of Zhongnan** | Three renowned Zhongnan Sect martial artists invited to the gathering |
| 홍진 | **Hong Jin** | Level 22 man at the City Lord's luncheon; delicate in appearance and voice. |
| 전하 | **His Highness** | Formal royal address for the resident prince; the official insists on this form instead of king. |
| 풍운검군 | **Wind-and-Cloud Sword Lord** | Epithet of Gong Iljung, the Zhongnan Sect's Sect Leader. |
| 철혈문 | **Iron Blood Sect** | Henan sect mentioned by Gong Ilhyuk. |
| 오호검문 | **Five Tigers Sword Sect** | Henan sect mentioned by Gong Ilhyuk. |
| 태을미리장 | **Taeeul Miri Palm** | Palm technique taught to Cheongpung by Mae Jonghak. |
| 육합검 | **Six Harmonies Sword** | Huashan sword technique known by Cheongpung. |
| 매화검법 | **Plum Blossom Sword Technique** | Huashan sword technique Cheongpung performed at age ten. |
| 상청검 | **Supreme Clarity Sword** | Huashan sword technique listed among Cheongpung's knowledge. |
| 낙화추영장 | **Falling Flower Chasing Shadow Palm** | Huashan palm technique listed among Cheongpung's knowledge. |
| 산화무영수 | **Scattering Flowers Shadowless Hand** | Huashan hand technique listed among Cheongpung's knowledge. |
| 자하신공 | **Zaha Divine Technique** | Huashan internal-energy technique used by Cheongpung. |
| 태사부 | **Grandmaster** | Huashan title referring to Mae Jonghak. |
| 군림 | **The Reign** | Opening fragment of an incomplete wuxia novel title that Taekyung read through volume thirty-four. |
| 주표 | **Zhu Bao** | Personal name of Prince Shangshan. |
| 근위대 | **royal guard** | Guard unit protecting Prince Shangshan. |
| 근위대 갑옷 세트 | **Royal Guard Armor Set** | Armor set Li Feng offers Cheongpung. |
| 황태자 | **Crown Prince** | The Emperor's older brother in Taekyung's recollection. |
| 고평문 | **Gopyeong Sect** | Minor sect whose young sect leader is pressured by Taekyung. |
| 고평지부 | **Gopyeong Branch** | Proposed branch designation under the Jin Family of Taiyuan. |
| 상산왕의 증표 | **Prince Shangshan's Token** | Golden medallion awarded by Zhu Bao as the Quest Reward. |
| 선황 | **the late Emperor** | The former Emperor whom Hong Jin served. |
| 내관 | **palace attendant** | Hong Jin's former palace role; context identifies him as a eunuch. |
| 고자 | **eunuch** | Castrated man; Hong Jin openly identifies himself by this term. |
| 사서삼경 | **Four Books and Three Classics** | Confucian texts used to describe conventional scholarly learning. |
| 금성전장 | **Golden Star Exchange** | Financial institution that issued the thousand-nyang bank draft. |
| 전표 | **bank draft** | Negotiable draft used for the thousand-silver-nyang payment. |
| 은자 | **silver nyang** | Silver currency unit. |
| 철전 | **iron coins** | Lower-value coin currency used to compare the payment's value. |
| 은원보 | **silver yuanbao** | Small silver ingot given to Taekyung as pocket money. |
| 대국 | **Great Nation** | Political wording on the Jin Family's welcome banner. |
| 성군 | **sage king** | Desired form of rulership proclaimed for Prince Shangshan. |
| 대태원진가 | **great Jin Family of Taiyuan** | Formal exalted reference to the Jin Family of Taiyuan. |
| 평양 | **Pyongyang** | City invoked in Taekyung's communist-atmosphere joke. |
| 천하제일인 | **greatest under heaven** | Superlative martial distinction used in Hong Jin and Jin Wikyung's banter. |
| 고금제일인 | **greatest of all time** | Superlative martial distinction used in Hong Jin's exaggerated praise. |
| 비무행 | **dueling tour** | Cheongpung's planned journey to challenge the Ten Dragons and Phoenixes. |
| 청강검 | **blue-steel sword** | Cheongpung's sword. |
| 광염 | **light-flames** | Violet manifestation surrounding Cheongpung when he uses the Zaha Divine Technique. |
| 서안 | **Xi’an** | Historic city near Huashan. |
| 서악 | **Western Peak** | Name for Huashan among the Five Great Mountains. |
| 흑사파 | **Black Serpent Sect** | Dark-path gambling-den gang in Xi’an. |
| 화산일학 | **Huashan’s Lone Crane** | Epithet of Baek Museong. |
| 매화삼절 | **Three Plum Blossom Elites** | Collective title for the current Sect Leader’s three exceptional disciples. |
| 매화검수 | **Plum Blossom Swordsmen** | Huashan appointment held by its three elite disciples. |
| 검신 | **Sword God** | Alternate title used for Mae Jonghak; kept distinct from 검성, rendered Sword Saint. |
| 기해 | **qi sea** | Name for the dantian, the place where internal energy begins and gathers. |
| 임독양맥 | **Conception and Governor Vessels** | The paired vessels Taekyung attempts to open. |
| 근맥 | **Sinews and Meridians** | System attribute reduced by one after Taekyung's failed qi circulation. |
| 사해오호 | **Four Seas and Five Lakes** | Traditional geographic phrase used with the Nine Provinces and Eight Wastes. |
| 환골탈태 | **Bone Transformation** | Advanced transformation described as optional in martial-arts novels. |
| 연무장 | **training ground** | Private martial-arts practice area at Taekyung's newly rebuilt pavilion. |
| 청석 | **bluestone** | Extremely hard stone used for the training-ground floor. |
| 십팔반병기 | **eighteen traditional weapons** | Training weapons displayed on a rack. |
| 수련동 | **training hall** | Building located roughly two hundred jang from the training ground. |
| 찍고 땡 | **touch-and-go method** | Repeatedly reaching a destination and returning as an endurance exercise. |
| 홍가 | **Hong** | Unnamed middle-aged Jin Family martial artist who identifies himself by surname. |
| 진무량 | **Jin Muryang** | Founder of the Jin Family; legendary martial artist from roughly three hundred years earlier. |
| 천응 | **Heavenly Eagle** | Huge bird regarded as a spirit creature, said to have a wingspan exceeding one jang. |
| 혈교 | **Blood Cult** | Demonic organization named as a possible source of the intruder. |
| 강시 | **jiangshi** | Reanimated corpse from folklore; Childeuk and Hong mistakenly identify Taekyung as one. |
| 태초 마을 | **Taecho Village** | Place named by Taekyung immediately after surviving the fall. |
| 벽호공 | **Wall Lizard Technique** | Climbing martial art used to scale walls and cliffs. |
| 낙안봉 | **Falling Goose Peak** | Huashan peak exceeding five hundred jang; Cheongpung climbed it as a child. |
| 인피면구 | **human-skin mask** | Disguise made from peeled human facial skin. |
| 무재 | **martial talent** | Innate aptitude for learning martial arts. |
| 검성 수련 간접 체험기 | **Sword Saint Training: A Secondhand Experience** | Cheongpung's Peak-grade cliff-training Quest. |
| 검성 수련 간접 체험기-2 | **Sword Saint Training: A Secondhand Experience—2** | Linked Quest generated after the first training Quest succeeds. |
| 초보 수련자 | **Beginner Trainee** | System Title upgraded after the tenth cliff climb. |
| 중급 수련자 | **Intermediate Trainee** | System Title received after Beginner Trainee is upgraded. |
| 황하방 | **Yellow River Gang** | Organization involved in a dispute with the Sogong Sect. |
| 소공문 | **Sogong Sect** | Sect involved in a dispute with the Yellow River Gang. |
| 남부상회 | **Southern Merchant Guild** | Merchant organization whose matter is reported to Jin Wikyung. |
| 내당주 | **Inner Hall Master** | Title for the head of the Jin Family's Inner Hall. |
| 내외당 | **Inner and Outer Halls** | The Jin Family's two internal administrative divisions. |
| 세가 | **great family** | Murim category Jin Wikyung hopes the Jin Family will attain. |
| 복호권 | **Crouching Tiger Fist** | Huashan martial art Cheongpung uses during the spar. |
| 암향표 | **Dark Fragrance Drift** | Movement technique Cheongpung uses to evade Taekyung's attacks. |
| 천근추 | **Thousand-Catty Drop** | Technique Cheongpung identifies when Taekyung lifts the spear shaft beneath his foot. |
| 일권복호 | **One Fist Subdues the Tiger** | Named form of the Crouching Tiger Fist. |
| 매화권 | **Plum Blossom Fist** | Huashan fist technique Cheongpung uses in sparring. |
| 천응조 | **Heavenly Eagle Claw** | Huashan claw technique used by Cheongpung. |
| 봉미혈 | **Fengwei acupoint** | Acupoint around the ribs targeted by Cheongpung. |
| 태권도 | **Taekwondo** | Martial art Taekyung practiced as a child. |
| 태극 1장부터 8장까지 | **Taegeuk Forms 1 through 8** | Standard taekwondo pattern sequence Taekyung copied as a child. |
| 공수납백인 | **Empty-Hand Seizes the Blade** | Technique for catching an opponent's weapon between bare fingers. |
| 오행매화보 | **Five-Element Plum Blossom Steps** | Footwork technique Cheongpung combines with Dark Fragrance Drift. |
| 백전백패 | **Hundred Battles, Hundred Losses** | Taekyung's proposed teasing nickname for Mujin. |
| 너구리 | **Neoguri** | Instant-noodle brand used in Taekyung's flavor joke. |
| 진라면 | **Jin Ramen** | Instant-noodle brand used in Taekyung's flavor joke. |
| 푸라면 | **Puramyeon** | Instant-noodle brand used in Taekyung's flavor joke. |
| 매화오품지 | **Plum Blossom Five-Point Finger** | Five-finger technique Cheongpung uses during the duel. |
| 벽을 넘어서 | **Beyond the Wall** | System Quest generated during Taekyung's breakthrough. |
| 절정 고수 | **Peak Master** | System class awarded after Taekyung completes Beyond the Wall. |
| 테무르 | **Temur** | Northern Gaoyuan chieftain commanding one hundred tribespeople; claims descent from the khans. |
| 칭겐 | **Chinggen** | Northern Gaoyuan chieftain commanding one hundred tribespeople; restrains Temur. |
| 인도 | **Human Butcher** | Epithet of a mysterious Han Chinese mounted-bandit power commanding fifty subordinates. |
| 텡게르 | **Tengger** | Sky deity invoked by Temur. |
| 대칸 | **Great Khan** | Title of the former ruler whose descendants Temur and Chinggen claim to be. |
| 대초원 | **Great Steppe** | The steppe region from which Temur and Chinggen come. |
| 마유주 | **mare's-milk wine** | Fermented alcoholic drink offered at the gathering. |
| 게르 | **ger** | Traditional nomadic dwelling contrasted with Central Plains wooden buildings. |
| 한족 | **Han Chinese** | Ethnic designation used by the steppe chieftains. |
| 흑사 | **Black Sand** | Eyepatched middle-aged leader of the Black Sand Band; a newly introduced identity. |
| 흑사대 | **Black Sand Band** | Han-Chinese mounted-bandit force of one hundred. |
| 천풍단 | **Heavenly Wind Band** | Five-hundred-member northern plateau mounted-bandit force subordinate to Black Sand. |
| 천풍단주 | **Heavenly Wind Band Leader** | Leader operating under Black Sand's orders near Datong. |
| 하곡 | **Hequ** | Route and Jin Family branch targeted as the alliance's entry point into Shanxi. |
| 참마검 | **horse-chopping sword** | Heavy saber used by the Human Butcher; rendered descriptively. |
| 삼매진화 | **Samadhi True Fire** | Internal-energy flame demonstrated by the unnamed old man. |
| 귀환자 | **Returnee** | System Title |
| 명가의 자제 | **Scion of a Prestigious Family** | System Title |
| 승부사 | **Gambler** | System Title |
| 명장 | **Master Artisan** | Master craftsman capable of handling Ten-Thousand-Year Cold Iron |
| 가공되지 않은 만년한철 | **Unprocessed Ten-Thousand-Year Cold Iron** | System Item |
| 장인을 찾아라 | **Find the Master Artisan** | System Quest |
| 장태보 | **Jang Taebo** | Former Guild Leader of the Ironcraft Guild; now lives near Jeongyang and is sought as a Master Artisan. |
| 철기방 | **Ironcraft Guild** | Hubei guild composed mainly of skilled craftsmen and closely associated with the Nine Sects and One Gang. |
| 철기방주 | **Guild Leader of the Ironcraft Guild** | Title of the Ironcraft Guild’s leader; the current leader is Jang Taebo’s disciple. |
| 오향장육 | **five-spice pork** | Dish Cheongpung packed for the journey. |
| 항아 | **Hanga** | Local village boy who lives near Jang Taebo. |
| 구방표국 | **Nine-Room Escort Bureau** | Escort Bureau that supplies Jang Taebo with a fifty-year-old He Shou Wu every four months. |
| 하수오 | **He Shou Wu** | Traditional medicinal herb; a thirty-year-old specimen is offered to Jang Taebo. |
| 오십 년 묵은 하수오 | **Fifty-Year-Old He Shou Wu** | First Rate Spirit Herb shown in the System Item Window; can provide up to about two years of internal energy. |
| 불로초 | **Herb of Eternal Youth** | Spirit herb said to grant eternal youth and immortality. |
| 불로초를 찾아서 | **In Search of the Herb of Eternal Youth** | System Quest generated after Jang Taebo names the Herb of Eternal Youth. |
| 천검진인 | **Heavenly Sword True Person** | Taoist-style title of the current Sect Leader of Huashan, who once commissioned a sword from Jang Taebo. |
| 여의주 | **dragon pearl** | Legendary treasure requested by Jang Taebo. |
| 공청석유, 용의 발톱, 여의주 구하기 | **Get Gongcheong Seokyu, a Dragon’s Claw, and a Dragon Pearl** | Quest generated after Jang Taebo makes additional demands; Taekyung rejects it. |
| 천풍 | **Heavenly Wind** | Short form displayed on the Heavenly Wind Band's flag. |
| 장팔 | **Jang-pal** | Woodcutter who meets and helps the unnamed old man. |
| 장 씨 | **Jang** | Surname form used for the woodcutter Jang-pal. |
| 장가촌 | **Jang Family Village** | Clan village where Jang-pal lives. |
| 홍가촌 | **Hong Family Village** | Clan village said to be three hundred li from Jang Family Village. |
| 신령님 | **Mountain Spirit** | Jang-pal's mistaken address for the unnamed old man. |
| 장씨 | **Jang** | Unspaced source variant of 장 씨; surname form for Jang-pal. |
| 반박귀진 | **Returning to Simplicity** | Supreme Peak technique or phenomenon used by Jeok Cheongang. |
| 이형환위 | **Shifting Form and Position** | Supreme Peak movement or evasion technique used by Jeok Cheongang. |
| 허공섭물 | **Seizing an Object Through Empty Space** | Technique Jeok Cheongang uses to lift Jang Taebo remotely. |
| 백련정강 | **Baekryeon Jeonggang** | Extremely hard steel used to forge Hyuk Mujin's sword. |
| 강자지존 | **Might Makes Right** | Murim principle invoked as the basis for Mae Jonghak's challenge. |
| 꼰대 | **boomer** | Modern slang for a hidebound older person; used by Cheongpung. |
| 꼰머 | **boomer-brain** | Related slang term Cheongpung says has a similar meaning. |
| 국밥 | **gukbap** | Korean dish of rice served in hot soup; footnoted in the reading copy. |
| 부마도위 | **Imperial Son-in-Law** | Imperial title mentioned by Jang Taebo. |
| 천하오대세가 | **Five Great Families** | Expanded source form of 오대세가. |
| 열화신공 | **Fire Gate Divine Technique** | Secret internal cultivation technique of the Fire Gate Clan, preserved through one-person succession without leakage. |
| 장천 | **Jangcheon** | Name Jeok Cheongang gave to the orphan who later became Jopil; means “Vast Sky.” |
| 벌모세수 | **cleansing the sinews and washing the marrow** | Jeok Cheongang’s constitution-improving technique. |
| 상단전 | **upper dantian** | Advanced dantian whose opening signifies entry into the Martial Extremity realm. |
| 무극 | **Martial Extremity realm** | Realm associated with opening the upper dantian. |
| 창천검왕 | **Azure Sky Sword King** | One of the Ten Kings and the Grand Family Head of the Nangong Family. |
| 태상가주 | **Grand Family Head** | Title held by the Azure Sky Sword King as head of the Nangong Family. |
| 왕팔 | **Wangpal** | One of the youths who tried to take Jangcheon's dumpling. |
| 홍소칠 | **Hong Sochil** | One of the youths who tried to take Jangcheon's dumpling. |
| 소우평 | **So U-pyeong** | One of the youths who tried to take Jangcheon's dumpling. |
| 보옥 | **Treasured Jade** | Missing Fire Gate Clan treasure sought by Jeok Cheongang. |
| 우황태 | **Woo Hwangtae** | Chief of the Seongun Escort Bureau and Woo Jintae's father. |
| 수문각 | **Gate Guard Pavilion** | Jin Family gate complex at the main entrance. |
| 수문위사 | **gate guard** | Jin Family guard stationed at the gate. |
| 장주 | **Lord** | Title used for one of the Five Gates heads, as in 태 장주. |
| 패화권 | **Defeated Flower Fist** | Chulwoo’s epithet. |
| 산서기협 | **Shanxi Extraordinary Hero** | Epithet mentioned among the Jin Family’s known figures; distinct source spelling from 산서괴협. |
| 소림사 | **Shaolin Temple** | Temple invoked in Chulwoo’s comparison of Baek Museong’s conduct. |
| 화검봉 | **Flower Sword Phoenix** | Eunhyang’s epithet and one of the Three Plum Blossom Elites. |
| 화산말학 | **Huashan’s Last Crane** | Taekyung’s mistaken hearing of 화산일학; not a genuine epithet. |
| 매화손절 | **Plum Blossom Cutoff** | Taekyung’s mistaken hearing of 매화삼절; not a genuine title. |
| 하곡문 | **Hequ Sect** | Small sect led by Jang Se-pal. |
| 장세팔 | **Jang Se-pal** | Leader of the small Hequ Sect. |
| 양천 | **Yangcheon** | Shanxi-area location near which a small martial arts academy operates. |
| 노호검객 | **Roaring Fury Swordsman** | Fiery-tempered elder and top-five master of the Zhongnan Sect. |
| 청성파 | **Qingcheng Sect** | Sect named in Baek Museong's comparison about disciplinary rules. |
| 집법원 | **Disciplinary Hall** | Huashan body that handles violations of sect rules. |

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
| 여자 친구 | 박지훈 | girlfriend_to_boyfriend | Oppa | casual-familiar | Jihoon's girlfriend addresses him as 오빠 while asking him to return to the car. |
| 임춘수 | 1팀장 | guild_master_to_team_leader | Team 1 Leader | blunt-commanding | Chunsoo addresses him with a rough 야 while issuing orders and demanding his candid assessment. |
| 1팀장 | 임춘수 | guild_team_leader_to_guild_master | Guild Master | formal-deferential | The Team 1 Leader consistently addresses Chunsoo as 길드장님 while reporting and accepting orders. |
| 진태경 | 하연 | older_brother_to_younger_sister | Sis | casual-familiar | Taekyung addresses Hayeon as 동생아 during their fly investigation. |
| 동료 | 김준수 | Security Team colleague | Junsu | casual-collegial | Uses 준수야 while checking whether Junsu pulled an all-nighter. |
| 보안팀장 | 김준수 | team_leader_to_subordinate | Kim Junsu | blunt-commanding | Shouts 김준수 when the target begins moving. |
| 김권동 | 보안팀장 | subordinate_to_team_leader | Team Leader | deferential | Uses 팀장님 over the radio while reporting on the disguised approach. |
| 보안팀장 | 1번 | supervisor_to_surveillance_agent | Number One | command-radio | Uses the operative’s radio call sign while directing the real-estate-office surveillance. |
| 보안팀장 | 2번 | supervisor_to_surveillance_agent | Number Two | command-radio | Uses the operative’s radio call sign while ordering continued observation. |
| 부동산 아줌마 | 진태경 | real_estate_agent_to_customer | Boss; young bachelor | chatty-polite and flirtatious | The agent calls Taekyung 사장님 and 총각 while offering listings and commenting on his appearance. |
| 김권동 | 진태경 | surveillance_hunter_to_target | young man | friendly and polite | Gwondong maintains his ordinary-neighbor disguise and addresses Taekyung as a younger local acquaintance. |
| 진하연 | 여름이 | caretaker_to_kitten | Yeoreum | affectionate-casual | Hayeon repeatedly calls the kitten by name and refers to herself as Sis. |
| 김권동 | 김준수 | Security Team colleagues | Junsu | casual-collegial | Gwondong uses 진수야 while questioning Junsu’s interpretation of the item. |
| 보안팀장 | 김권동 | team_leader_to_subordinate | Gwondong | blunt-commanding | Uses 권동아 while directing the operation. |
| 진태경 | 최병일 | target_to_attacking_team_leader | Mr. Choi Byungil | mock-polite and taunting | Uses 최병일 씨 while baiting and confronting him. |
| 진태경 | 김준수 | target_to_surveillance mage | Junsu | casual and taunting | Uses 준수야 while questioning him. |
| 임춘수 | 진태경 | guild_master_to_younger_rival | you | blunt-but-familiar | Repeatedly uses 자네 while challenging and testing Taekyung. |
| 김화종 | 임춘수 | familiar_mage_to_guild_master | Chunsoo | gentle-and-familiar | Addresses Im Chunsoo as 춘수 on arriving at the hiking-trail entrance. |
| 임춘수 | 김화종 | former_trainee_to_former_instructor | Instructor | deferential and fearful | Im Chunsoo addresses Hwajong as 교관님 after recognizing his former instructor. |
| 김화종 | 진태경 | senior_Hunter_to_younger_Hunter | Mr. Jin | formal-polite | Hwajong addresses Taekyung as 진태경 씨 while proposing an exchange of stories. |
| 1팀장 | 보안팀장 | guild_team_leader_to_security_team_leader | Security Team Leader | formal-commanding | Team Leader 1 directly addresses the Security Team Leader while warning him about discipline. |
| 보안팀장 | 1팀장 | security_team_leader_to_guild_team_leader | Team Leader 1 | formal-deferential | The Security Team Leader addresses Team Leader 1 as 팀장님 while reporting what he heard. |
| 진태경 | 기사님 | customer_to_moving_driver | Driver | polite | Taekyung addresses the private moving-truck driver by his occupational title on the phone. |
| 이삿짐 아저씨 | 진태경 | moving_driver_to_customer | Mr. Jin Taekyung; Boss | friendly-polite | The driver uses 진태경 씨 on the phone and 사장님 while insisting on moving the capsule. |
| 진무경 | 혁무진 | senior martial artist to subordinate | Hyung Mujin | blunt-senior | Mukyung deliberately misnames Hyuk Mujin as 형무진 before ordering him to stop the carriage. |
| 혁무진 | 진무경 | subordinate to Second Young Master | Second Young Master | deferential | Uses 이공자님 while correcting Mukyung's deliberate misnaming and accepting his orders. |
| 월화 | 진태경 | Lower District Sect branch leader to Jin Family young master | Young Master Jin; our Young Master | polite and lightly playful | Uses 우리 공자님, 진 공자, and the teasing 잠룡 공자 while greeting and teasing Taekyung. |
| 월화 | 혁무진 | inn proprietress and branch leader to visiting martial artist | Young Martial Artist; Martial Artist | polite and teasing | Uses 젊은 무사님 and 무사님 while discussing her profession and correcting Mujin's conduct. |
| 혁무진 | 월화 | Jin Family retainer to Lower District Sect Branch Leader | Young Lady; Branch Leader | formal-polite, then deferential | Initially addresses Wolhwa as 소저, then corrects himself to 지부장님 after learning her identity. |
| 월화 | 진무경 | Lower District Sect Branch Leader and inn proprietress to Jin Family Second Young Master | Young Hero Jin | polite and lightly playful | At departure, Wolhwa addresses Mukyung as 진 소협 after agreeing to accompany the group. |
| 오색귀 | 진태경 | former_bandit_associates_to_prior_benefactor | Boss | pleading and deferential | The Five-Colored Ghosts repeatedly call Taekyung 대형 while begging him to rescue them. |
| 월화 | 춘삼 | Lower District Sect branch leader to subordinate | Chunsam | commanding-familiar | Uses 춘삼아 while directing him to execute the interrogation order. |
| 마적 | 풍양 | mounted-bandit subordinate to bandit leader | Leader | deferential | Uses 단주 when reporting to Pung Yang. |
| 소월 | 철무백 | niece_to_paternal_uncle | Uncle Cheol | familiar-polite | Lee Seowol asks Cheol Mubaek to suppress his heat because she cannot breathe. |
| 철무백 | 소월 | paternal_uncle_to_niece | Seowol | affectionate-familiar | Cheol Mubaek speaks gently to Seowol and says protecting her is his duty. |
| 소월 | 철검대주 | sect_leader_to_subordinate | Iron Sword Squad Leader | formal-commanding | Lee Seowol addresses him while issuing her final instruction about her title. |
| 소월 | 수문각주 | sect_leader_to_subordinate | Master of the Gatekeeper Pavilion | formal-commanding | Lee Seowol addresses him while asserting her authority as Sect Leader. |
| 사자 | 이소월 | enemy_envoy_to_sect_leader | Sect Leader | mock-formal | The Red Wind Band envoy addresses Lee Seowol as 문주님 while delivering the coercive marriage-or-destruction ultimatum. |
| 풍양 | 철무백 | junior_to_older_martial_peer | Senior Cheol | polite and taunting | Pung Yang repeatedly addresses Cheol as 철 선배 while provoking him. |
| 진태경 | 철무백 | junior_to_respected_Peak_master | Sir | apologetic-polite | Taekyung first calls Cheol Grandpa, then corrects himself to the respectful 대협. |
| 월화 | 철무백 | ally_to_injured_master | Sir Cheol | polite and reassuring | Wolhwa addresses the critically wounded Cheol while administering temporary medicine and asking about his attacker. |
| 진무경 | 풍양 | challenger_to_bandit_leader | Pung Yang | challenge-shout | Mukyung calls out Pung Yang by name to begin the confrontation. |
| 풍양 | 이소월 | captor_to_coerced_bride | Young Lady | polite and coercive | Pung Yang addresses Seowol as 소저 while threatening her subordinates and demanding marriage. |
| 풍양 | 진무경 | enemy_to_enemy | you / little brat | condescending and taunting | Uses 네놈 and 어린놈 while threatening to sever Mukyung's limbs. |
| 진태경 | 풍양 | enemy_to_enemy | you pill-popping bastard | insulting-casual | Taekyung openly insults Pung Yang while announcing that he will use a pill too. |
| 풍양 | 진태경 | enemy_to_enemy | little brat; wet-behind-the-ears fledgling | condescending and taunting | Pung Yang dismisses Taekyung as an inexperienced child while challenging his ability to intervene. |
| 무인 | 이소월 | sect_subordinate_to_sect_leader | Sect Leader | formal-deferential | Surviving Mount Heng martial artists address Seowol by her title during the casualty search. |
| 이소월 | 진태경 | rescued_sect_leader_to_benefactor | Benefactor | deferential | Lee Seowol repeatedly addresses Taekyung as 은공 after acknowledging that he and Jin Mukyung saved the Mount Heng Sword Sect. |
| 월화 | 혼주지부장 | chief_branch_leader_to_subordinate_branch_leader | Honju Branch Leader | formal-commanding | Wolhwa addresses him by branch title while directing rumor operations. |
| 진무경 | 이소월 | junior_to_sect_leader | Sect Leader | formal-polite | Uses 문주 while greeting Lee Seowol. |
| 혁무진 | 이소월 | subordinate_to_sect_leader | Sect Leader | deferential and exuberant | Formally praises the Sect Leader while greeting her. |
| 혁무진 | 철무백 | junior_to_respected_Peak_master | Great Hero Cheol | deferential | Begins a formal greeting with 철무백 대협 before being stopped. |
| 철무백 | 진무경 | senior_martial_peer_to_younger_martial_artist | Heaven Shaking Sword | affectionate-teasing | Uses 우리 진천검 while warmly inviting Mukyung to return. |
| 철무백 | 진태경 | senior_martial_peer_to_benefactor | you | casual-teasing | Uses 자네 while teasing Taekyung about his greeting and injuries. |
| 진위경 | 위팽 | lord_to_personal_guard | you | formal-but-familiar | Uses 자네 while assigning Wipeng the banner-preparation task. |
| 하오문도 | 진위경 | informant_to_lesser_family_head | Lesser Family Head | deferential | Uses 소가주님 while correcting Wikyung's misunderstanding about Mukyung's condition. |
| 현령 | 진태경 | county_official_to_celebrated_martial_artist | Great Hero Jin | formal-polite and admiring | Uses 진 대협 while praising Taekyung's alleged exploits. |
| 진태경 | 현령 | martial_artist_to_county_official | County Magistrate | polite and lightly sarcastic | Uses 현령님 while explaining that the Lesser Family Head cannot receive visitors. |
| 혁무진 | 진위경 | Jin Family subordinate to Lesser Family Head | Lesser Family Head | deferential | Uses 소가주님 while confessing that he accepted Taekyung's invitation. |
| 진위경 | 혁무진 | Lesser Family Head to direct family subordinate | you | formal-but-familiar | Uses 자네 while recognizing Mujin and instructing him to keep helping Taekyung. |
| 현령 | 진위경 | county_official_to_lesser_family_head | Lesser Family Head | formal-polite and deferential | Uses 진 소가주님 when asking Taekyung to convey his regards. |
| 현령 | 진무경 | county_official_to_renowned_martial_artist | Heaven Shaking Sword | formal-polite and respectful | Uses 진천검 when asking Taekyung to convey his regards. |
| 동료 쟁자수 | 석칠 | junior_colleague_to_senior_colleague | Hyung | casual-but-respectful | Calls Seokchil 형님 while inviting him to the fire and restraining him. |
| 석칠 | 동료 쟁자수 | senior_colleague_to_junior_colleague | Brat | gruff-casual | Uses 이놈아 while bantering with his fellow porter. |
| 동료 쟁자수 | 청풍 | senior_colleague_to_newcomer | Rookie | casual | Calls Cheongpung 신참. |
| 혁무진 | 아주머니 | childhood_benefactor_to_former_child | Auntie | deferential-polite | Mujin respectfully addresses the local snack-stall vendor who secretly gave him candied hawthorn when he was a child. |
| 청풍 | 진태경 | newly met beneficiary to benefactor | Benefactor | deferential | Cheongpung repeatedly addresses Taekyung as 은인 after receiving food. |
| 청풍 | 혁무진 | newly met beneficiary to benefactor | Benefactor | deferential | Cheongpung includes Mujin among his 은인들 after receiving the skewers. |
| 혁무진 | 청풍 | martial artist to young master | Young Master | formal-deferential | Mujin uses 공자께서는 when asking why Cheongpung descended from the mountain. |
| 우진태 | 황 소저 | host_to_five_gates_scion | Young Lady Hwang | polite and flirtatious | Woo Jintae presents Shu brocade as a gift while implying personal feelings, then retreats behind a joke. |
| 우진태 | 혁 아우 | older_friendly_sc ion_to_younger_sc ion | Little Brother Hyuk | familiar and patronizing | Woo Jintae promises the male scion an especially impressive gift. |
| 혁 아우 | 우진태 | younger_sc ion_to_older_friendly_sc ion | hyung | familiar and deferential | The scion calls Woo Jintae hyung after they have become close enough to use fraternal terms. |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 진태경 | 우진태 | enemy_to_enemy | you / you bastard | insulting-casual | Taekyung repeatedly addresses Woo Jintae with hostile informal forms while demanding an apology and slapping him. |
| 우진태 | 진태경 | enemy_to_enemy | you / little bastard | condescending and enraged | Woo Jintae uses hostile forms such as 네놈, 애새끼, and 어린놈 while trying to intimidate Taekyung. |
| 갈 소협 | 정 소협 | fellow_Five_Gates_heir | Young Hero Jeong | formal-polite | The unnamed heir addresses the other injured heir by surname and honorific. |
| 정 소협 | 갈 소협 | fellow_Five_Gates_heir | Young Hero Gal | formal-polite | The unnamed heir responds using the other injured heir's surname and honorific. |
| 관리 | 진태경 | official_to_young_martial_artist | Young Master | formal-polite | The official addresses Taekyung as 공자 while explaining the consequences of Prince Shangshan's displeasure. |
| 홍 내관 | 이풍 | political_rivals | Assistant Commissioner Li | mock-friendly and probing | Uses 우리 이 첨사 and a superficially familiar tone while testing and provoking Li Feng. |
| 이풍 | 홍 내관 | political_rivals | Eunuch Hong / Deputy Military Commissioner | formal but sarcastic | Alternates between the official title and Eunuch Hong to mock his demand for familiarity. |
| 공일혁 | 이풍 | martial_rivals | Li Feng of Huashan | casual and taunting | Mocks Li Feng's office and recalls his defeat at Huashan ten years earlier. |
| 이풍 | 공일혁 | martial_rivals | you bastard | hostile and furious | Responds to Gong Ilhyuk's insult toward Huashan with an openly aggressive form. |
| 진태경 | 청풍 | companion_to_young_martial_artist | Young Master Cheongpung | formal-polite | Taekyung uses 청 공자 while correcting Cheongpung's royal-etiquette mistake. |
| 공일혁 | 진태경 | senior_martial_artist_to_junior_martial_artist | Junior | condescending and dismissive | Uses 후배님 while ordering Taekyung to move aside. |
| 진태경 | 공일혁 | junior_martial_artist_to_senior_martial_artist | Senior | polite but firm | Uses 선배님 while intervening on Cheongpung's behalf. |
| 공일혁 | 청풍 | senior_martial_artist_to_junior_martial_artist | Junior | impatient and condescending | Treats Cheongpung as a junior while demanding his introduction. |
| 청풍 | 공일혁 | junior_martial_artist_to_senior_martial_artist | Senior | deferential and apologetic | Uses 선배님 while apologizing for catching Ilhyuk's wrist. |
| 이풍 | 진태경 | senior_official_to_respected_young_martial_artist | Young Hero Jin | formal and respectful | Addresses Taekyung as 진 소협 after praising his reputation. |
| 공일혁 | 홍진 | junior_official_guest_to_senior_official | Deputy Military Commissioner | formal and deferential | Appeals to Hong Jin for his view on the impending disturbance. |
| 이풍 | 청풍 | Huashan lay disciple to martial uncle | Young Hero; Martial Uncle Cheongpung | formal and reverent | Li Feng initially addresses Cheongpung as 소협 while testing his knowledge, then recognizes him as 사숙 after witnessing his Huashan sword technique. |
| 홍진 | 공일혁 | political_host_to_guest | Great Hero Gong | polite but cutting | Hong Jin uses the respectful title while dismissing Gong Ilhyuk and exposing his poor judgment. |
| 청풍 | 이풍 | Martial Uncle to Martial Nephew | Martial Nephew Li Feng | exuberant and deferential | Cheongpung adopts the address to obtain royal-guard armor and weapons. |
| 홍진 | 주표 | servant and political aide to prince | His Highness | formal-deferential | Uses the elongated royal call 전하 while summoning Zhu Bao. |
| 진태경 | 주표 | visitor to prince | His Highness, Prince Shangshan | formal-deferential | Addresses Zhu Bao as 상산왕 전하 after kneeling to meet his gaze. |
| 주표 | 진태경 | prince to visiting young hero | Jin Taekyung | formal and inquisitive | Uses the formal second-person address before asking Taekyung's name and requesting an autograph. |
| 홍진 | 진태경 | political_host_to_young_martial_artist | Young Hero Jin; Young Master Jin; Sleeping Dragon of Shanxi | polite, coaxing, and probing | Uses respectful forms while steering Taekyung toward relaying the Escort Bureau proposal and teasing him with the Seongun Escort Bureau. |
| 진태경 | 홍진 | young_martial_artist_to_political_official | Comrade Chairman—no, Deputy Military Commissioner | casual and teasing, then formally corrective | Deliberately jokes with an inappropriate title before correcting himself to Hong Jin's official office. |
| 진태경 | 이풍 | junior_to_respected_official_and_martial_ally | Great Hero Li | polite and respectful | Agrees with Li Feng's proposal that Zhu Bao visit the Jin Family's banquet. |
| 이풍 | 주표 | official_to_prince | Your Highness | formal-deferential | Suggests that Zhu Bao visit the Jin Family's grand banquet in fifteen days. |
| 주표 | 청풍 | prince_to_young_martial_artist | you | formal and gatekeeping | Refuses Cheongpung's autograph until he acquires a martial title. |
| 홍진 | 청풍 | political_official_to_young_martial_artist | Young Master | formal and curious | Uses 공자께서는 while asking whether Cheongpung has always lived on Huashan. |
| 전령 | 진위경 | military messenger to Lesser Family Head | Lesser Family Head | formal-polite and deferential | Uses 소가주님 when confirming Wikyung's identity. |
| 위팽 | 진무경 | Jin Family retainer to Second Young Master | Second Young Master | deferential and blunt | Uses 이공자 while directing Mukyung to wash before the guest's arrival. |
| 진위경 | 홍진 | political_host_to_deputy_military_commissioner | Comrade Hong | formal-polite and playful | Jin Wikyung adopts Hong Jin's requested casual address, 홍 동지. |
| 홍진 | 진위경 | deputy_military_commissioner_to_lesser_family_head | Lesser Family Head Jin | formal and teasing | Hong Jin addresses Jin Wikyung as 진 소가주님 while flattering and joking with him. |
| 청풍 | 진무경 | young_martial_artist_to_renowned_senior_martial_artist | Young Hero Jin Mukyung | deferential and excited | Cheongpung calls him 진천검 진무경 소협 and later 진 소협 while seeking his duel. |
| 진무경 | 청풍 | senior_martial_artist_to_newly_met_young_martial_artist | Young Hero | deferential and expectant | Mukyung addresses Cheongpung as 소협 while asking whether Great Hero Mae descended from Huashan. |
| 철우 | 백무성 | junior_disciple_to_senior_brother | Senior Brother | deferential | Uses 대사형 while answering Baek Museong. |
| 은향 | 백무성 | junior_disciple_to_senior_brother | Big Brother; Senior Brother | familiar and casual-polite | Repeatedly calls him 큰 오라버니 even after he insists on 대사형. |
| 홍가 | 장칠득 | older_martial_artist_to_junior_martial_artist | Little Brother Jang | familiar and casual | Hong calls Childeuk 장 아우 after inviting him to address Hong as hyung. |
| 장칠득 | 홍가 | junior_martial_artist_to_older_martial_artist | hyung | deferential, then familiar | Childeuk initially uses Senior and then adopts Hong's requested 형님 address. |
| 장칠득 | 진태경 | servant_to_third_young_master | Third Young Master | formal-deferential | Jang Childeuk addresses Taekyung as 삼공자님 while asking permission to report the dangerous training. |
| 유생 | 진위경 | scholar_to_lesser_family_head | Lesser Family Head | formal-deferential | The scholar reports matters to Jin Wikyung and apologizes for his inadequate proposal. |
| 진위경 | 유생 | lesser_family_head_to_scholar | you | formal-but-familiar | Jin Wikyung uses 자네 while correcting and instructing the inexperienced scholar. |
| 위팽 | 유생 | senior_retainer_to_scholar | you | familiar and probing | Wipeng uses 자네 while asking the scholar for his assessment. |
| 매종학 | 청풍 | grandfather_to_grandson | Pung | affectionate-instructional | Mae Jonghak calls young Cheongpung 풍아 while teaching him the Crouching Tiger Fist. |
| 테무르 | 칭겐 | fellow_chieftain | Chinggen | familiar and argumentative | Temur addresses his fellow chieftain by name while defending their khan lineage. |
| 칭겐 | 테무르 | fellow_chieftain | Temur | familiar and cautioning | Chinggen uses Temur's name while warning him not to act rashly. |
| 테무르 | 인도 | hostile_strangers | you Han Chinese bastard | hostile and contemptuous | Temur insults the seated Han Chinese man before attempting to draw his curved saber. |
| 인도 | 테무르 | intimidating_rival_to_chieftain | friend | cold and taunting | The Human Butcher calls Temur a slow friend after forcing him to sit. |
| 인도 | 흑사 | rival_power_to_rival_power | Black Sand | blunt and familiar | Uses 흑사 while cutting off Black Sand's joking introduction. |
| 흑사 | 인도 | rival_power_to_rival_power | you | playful and taunting | Teases the Human Butcher about being called a butcher without showing fear. |
| 흑사 | 칭겐 | alliance_recruiter_to_recruited_chieftain | Chinggen | lightly teasing and probing | Identifies Chinggen by name while commenting on his composure and perceptiveness. |
| 흑사 | 노인 | subordinate_to_overwhelming_unknown_master | Elder, then big brother; both rejected | deferential and fearful | Black Sand first uses 어르신 and then 형님 while trying to placate the old man; the old man rejects both forms. |
| 위팽 | 진태경 | retainer_to_third_young_master | Third Young Master | formal-polite and admonishing | Uses 삼공자 while warning Taekyung to return by noon and behave respectfully toward Jang Taebo. |
| 장태보 | 항아 | elder_neighbor_to_child | Hanga | familiar and instructive | Calls the neighboring boy by name while correcting his speech and sending him home after dark. |
| 항아 | 장태보 | child_to_elder_neighbor | Grandpa | childlike-familiar | Repeatedly calls Jang Taebo 할부지. |
| 진태경 | 항아 | visiting_adult_to_local_child | little one | friendly and coaxing | Questions Hanga and offers food in exchange for information. |
| 혁무진 | 항아 | visiting_adult_to_local_child | little one | coaxing and encouraging | Questions Hanga with an artificially kind smile and offers two food bundles. |
| 진태경 | 장태보 | younger_visitor_to_elder_master | Elder | polite and persistent | Taekyung repeatedly addresses Jang Taebo as 어르신 while requesting his assistance. |
| 장태보 | 진태경 | elder_master_to_younger_visitor | you | gruff and familiar | Jang Taebo uses 자네 while questioning and dismissing Taekyung. |
| 장태보 | 혁무진 | elder_smith_to_young_martial_artist | you / wet-behind-the-ears brat | gruff and insulting | Insults Mujin after Mujin whispers that Jang is senile. |
| 장태보 | 청풍 | elder_smith_to_young_martial_artist | you / lunatic | gruff and incredulous | Initially treats Cheongpung as a lunatic despite recognizing him as Mae Jonghak's disciple. |
| 장팔 | 노인 | stranger_to_elder | Mountain Spirit, then Elder | deferential and apologetic | Jang-pal initially mistakes the old man for a mountain spirit, then shifts to a respectful elder address. |
| 노인 | 장팔 | strangers | you | gruff and familiar | The old man uses 자네 while questioning Jang-pal and accepting his help. |
| 항아 | 노인 | child_to_elder_stranger | Grandpa | childlike-familiar | Hanga calls the unnamed old man 할부지 after he arrives at her family’s home; this is distinct from her address to Jang Taebo. |
| 적천강 | 장태보 | strangers; visiting elder to local smith | Old Man Jang | blunt and familiar | Uses 장 노인 while confirming Jang Taebo’s identity. |
| 적천강 | 진태경 | overwhelming stranger to interrogated young martial artist | you; you bastard | blunt, threatening, and taunting | Uses 너, 네놈, and 이놈 while demanding Taekyung explain Qi Sense and the System. |
| 진태경 | 적천강 | frightened young martial artist to overwhelming elder | elder | polite and fearful | Uses the honorific 어르신 while explaining that the System may have felt like a cheat. |
| 적천강 | 청풍 | overwhelming_elder_to_young_martial_artist | you / little punk | blunt, amused, and threatening | Jeok Cheongang uses 네, 이놈, and related blunt forms while testing Cheongpung. |
| 청풍 | 적천강 | young_martial_artist_to_overwhelming_elder | Grandpa Jeok | casual-familiar despite deference | Cheongpung uses 적 할아버지 while asking Jeok Cheongang to confirm Taekyung's condition; this is a familial form of address, not literal kinship. |
| 혁무진 | 적천강 | subordinate_to_overwhelming_elder | Great Hero Jeok | deferential and fearful | Mujin uses 적 대협 while reporting Jeok’s orders and Taekyung’s awakening. |
| 적천강 | 혁무진 | overwhelming_elder_to_junior_martial_artist | you stupid fool | blunt and mocking | Jeok calls Mujin a 멍청한 놈 after knocking him down during the attempted escape. |
| 장천 | 적천강 | disciple_to_master | Master | deferential and pleading | Jangcheon repeatedly begs Jeok Cheongang to accept him as his Disciple. |
| 적천강 | 장천 | master_to_disciple | you / fool | blunt and gruff | Jeok rejects Jangcheon’s pleas, questions his choices, and threatens to send him down the mountain. |
| 우황태 | 송 문주 | fellow_Five_Gates_head | Sect Leader Song | sharp and defensive | Uses 송 문주 while defending his need to apologize for Woo Jintae. |
| 우황태 | 태 장주 | fellow_Five_Gates_head | Lord Tae | sharp and defensive | Uses 태 장주 while arguing that retreating would damage the Seongun Escort Bureau's standing. |
| 우황태 | 거한 | insulted_stranger_to_accidental_bystander | you ox-headed bastard | aggressive and insulting | Escalates from demanding an apology to insulting the huge Huashan junior after the dropped pill. |
| 백무성 | 철우 | senior_disciple_to_second_junior_disciple | Second | calm and admonishing | Baek Museong uses 둘째 while ordering Chulwoo to stop and later directs him to find Eunhyang. |
| 진위경 | 백무성 | host_to_visiting_martial_artist | Young Hero Baek | formal-polite | Uses 백 소협 when asking whether anything is wrong. |
| 은향 | 철우 | younger_female_disciple_to_older_fellow_disciple | Senior Brother Chul | familiar and casual-polite | Uses 철 오라버니 while teasing and speaking familiarly to Chulwoo. |
| 우황태 | 철우 | insulted_stranger_to_accidental_bystander | Young Hero Chul; Great Hero Chul | apologetic and pleading | Switches from 철 소협 to 철 대협 while apologizing after Chulwoo mocks him. |
| 철우 | 우황태 | stranger_to_stranger | Brother over there | casual-polite and teasing | Uses 형장 while selecting Woo Hwangtae to guide him to a supposed scenic privy. |
| 철우 | 진태경 | stranger_to_stranger | Brother over there | casual-polite | Uses 형장 when stopping after seeing Taekyung near the mountainside. |
| 위팽 | 철우 | Jin Family retainer to visiting martial artist | Defeated Flower Fist | formal-commanding | Uses Chulwoo's epithet while stopping the fight and rebuking both men for disgracing their schools. |
| 진태경 | 철우 | rival_companions | next mountain man | casual-teasing | Taekyung responds to Chulwoo's insult with a mocking counter-insult. |
| 백무성 | 진태경 | senior_martial_artist_to_younger_martial_artist | Young Hero Jin | formal-polite | Baek Museong agrees with Taekyung while correcting Chulwoo. |
| 백무성 | 청풍 | Martial_Nephew_to_Martial_Uncle | Martial Uncle | formal-deferential | Baek formally identifies himself as Cheongpung's Martial Nephew. |
| 공일혁 | 노호검객 | junior_disciple_to_sect_elder | Elder | deferential | Gong Ilhyuk repeatedly addresses the Roaring Fury Swordsman as 장로님 while steering him toward the Jin Family. |
| 철우 | 청풍 | junior_disciple_to_Martial_Uncle | Martial Uncle | apologetic and deferential | Initially calls Cheongpung Young Hero, then recognizes him and apologizes for failing to recognize the senior sect relation. |
| 위팽 | 청풍 | Jin Family retainer to visiting Huashan martial artist | Young Hero Cheongpung | formal-polite and worried | Uses 청 소협 while warning that Cheongpung's refusal of the Sect Leader's order could strain relations between the Jin Family and Huashan. |

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 진위경    | **Jin Wikyung**    |
| 위팽     | **Wipeng**         |
| 혁무진    | **Hyuk Mujin**     |
| 백무성    | **Baek Museong**   |
| 철우     | **Chulwoo**        |
| 은향     | **Eunhyang**       |
| 청풍     | **Cheongpung**     |
| 화왕     | **Fire King**                 | Jeok Cheongang |
| 태원진가   | **Jin Family of Taiyuan**        |
| 암천     | **Dark Heaven**                  |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 무인     | **martial artist**                               | Default term                                          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 비급     | **martial arts manual**                          | “martial scroll” where object/context warrants        |
| 기세     | **aura** / **momentum**                          | Depends on scene                                      |
| 전음     | **Sound Transmission**                           | Fixed skill terminology; preserve the internal-energy mechanism when the source explains it, but do not add an explanation where it does not |
| 운기조식   | **circulate one's qi**                           | Usually better as a verb than a proper-name technique |
| 가주     | **Family Head**                              |
| 소가주    | **Lesser Family Head**                       |
| 장로     | **Elder**                                    |
| 대장로    | **Head Elder**                               |
| 사형     | **Senior Brother**                           |
| 사제     | **Junior Brother**                           |
| 사숙     | **Martial Uncle**                            |
| 사질     | **Martial Nephew**                           |
| 전각     | **pavilion**                                 | Use “hall” only when established for a specific named building |
| 은인     | **Benefactor**                               |
| 상태               | **Status**                     |
| 아이템              | **Item**                       |
| 산서     | **Shanxi**             |
| 태원     | **Taiyuan**            |
| 본가      | **our family / this family**                                    |
| 소협      | **Young Hero**                                                  |
| 공자      | **Young Master**                                                |
| 공야청 | **Gong Yacheong** |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 소천 | **Socheon** |
| 소율 | **Soyul** |
| 하연 | **Hayeon** | Jin Taekyung’s younger sister |
| 삭주 | **Sakju** | Jin Family branch location |
| 삼공자 | **Third Young Master** | Title used for Jin Taekyung. |
| 화염신장 | **Flame Divine Palm** | Jopil's deadly palm technique, noted when Taekyung compares Jopil with Mukyung. |
| 만년한철 | **Ten-Thousand-Year Cold Iron** | Material that destroys Pung Yang's Body-Protecting Qi when the Unnamed Sword satisfies a specific condition. |
| 산서성 | **Shanxi Province** | Province containing the Lower District Sect branches. |
| 매화삼절 | **Three Plum Blossom Elites** | Collective title for the current Sect Leader’s three exceptional disciples. |
| 검신 | **Sword God** | Alternate title used for Mae Jonghak; kept distinct from 검성, rendered Sword Saint. |
| 연무장 | **training ground** | Private martial-arts practice area at Taekyung's newly rebuilt pavilion. |

## Listed compact profiles

### Baek Museong.md

# Baek Museong (백무성)

- **Safe through:** Chapter 185
- **Aliases:** Huashan’s Lone Crane
- **Role:** First-generation disciple of Huashan, first of the Three Plum Blossom Elites, and leader of the effort to return Cheongpung, his Martial Uncle, to Huashan.
- **Personality:** Calm, responsible, principled, and patient, though visibly weary of his junior disciples’ antics.
- **Voice:** Gentle and polite with strangers; measured and stern when correcting junior disciples.
- **Relationships:** The current Huashan Sect Leader is his Master; Chulwoo and Eunhyang are his junior disciples; Cheongpung is his Martial Uncle through Mae Jonghak and the current Sect Leader; he met Cheongpung ten years ago.

### Cheongpung.md

# Cheongpung (청풍)

- **Safe through:** Chapter 185
- **Aliases:** None
- **Role:** Mysterious young man encountered at Honghwa Inn; an exceptionally young Peak master whose Level Jin Taekyung cannot determine through Qi Sense; the grandson and disciple of Sword Saint Mae Jonghak, who secretly descended from Huashan to seek out and defeat the Ten Dragons and Phoenixes, beginning with Jin Mukyung; he has no martial title yet, naturally opened his Governor Vessel through enlightenment two years ago, has begun teaching Jin Taekyung and Hyuk Mujin using Mae Jonghak's training method, has now used Sword Energy and the Zaha Divine Technique during his spar with Taekyung, defended Taekyung from Jeok Cheongang with Huashan martial arts, and Prince Shangshan will only accept his autograph after he gains one
- **Personality:** Affable, dreamy, hazy, and childlike in manner, with innocent curiosity, delight in novel public attention, a deep love of martial arts, and a martial artist's competitive pride; he becomes unsettled when someone copies his martial arts
- **Voice:** Dreamy and hazy, with innocent, polite phrasing
- **Relationships:** Mae Jonghak, the Sword Saint, is his grandfather and martial instructor; Cheongpung came to Huashan at about age three or four rather than being born there, lived with Mae Jonghak at a hidden residence, and secretly left Huashan without his grandfather's knowledge to challenge the Ten Dragons and Phoenixes; Baek Museong is his Martial Nephew through the current Huashan Sect Leader, met him ten years ago, and is now leading the effort to return him to Huashan; the current Huashan Sect Leader, the Heavenly Sword True Person, is his eldest Senior Brother by generation and has ordered him to return; Cheongpung never underwent Huashan's initiation ceremony and is technically an outsider; Li Feng is his Martial Nephew within Huashan's hierarchy; calls Jin Taekyung and Hyuk Mujin Benefactors after they feed him and has chosen to remain with Taekyung despite the order

### Chulwoo.md

# Chulwoo (철우)

- **Safe through:** Chapter 185
- **Aliases:** None
- **Role:** Level 95 early-Peak Huashan martial artist, second junior disciple of Baek Museong, second of the Three Plum Blossom Elites, and wielder of the Defeated Flower Fist.
- **Personality:** Blunt, defensive, physically intimidating, short-sighted, quick-tempered, coarse, and unconcerned with personal cleanliness.
- **Voice:** Hearty, casual, and blunt, with crude insults, indignant protests, and a competitive streak when provoked.
- **Relationships:** Baek Museong is his Senior Brother; Eunhyang is his fellow junior disciple and frequent bickering partner; Cheongpung is his Martial Uncle, whom he initially failed to recognize and then apologized to; he serves under Huashan’s Sect Leader.

### Eunhyang.md

# Eunhyang (은향)

- **Safe through:** Chapter 185
- **Aliases:** None
- **Role:** Young female Huashan martial artist, youngest junior disciple of Baek Museong, member of the Three Plum Blossom Elites, and bearer of the Flower Sword Phoenix epithet.
- **Personality:** Bright, mischievous, playful, sharp-tongued, and willing to justify questionable actions with confident moral reasoning.
- **Voice:** Lively and teasing, with familiar phrasing and a sweet laugh; she prefers calling Baek Museong Big Brother.
- **Relationships:** Baek Museong is her Senior Brother; Chulwoo is her fellow junior disciple and bickering companion; she serves under Huashan’s Sect Leader.

### Gong Yacheong.md

# Gong Yacheong (공야청)

- **Safe through:** Chapter 179
- **Aliases:** Uncle Gong
- **Role:** Recovering guide and protector of the Sakju Branch survivors Socheon and Soyul; appointed to oversee the rebuilt Sakju Branch
- **Personality:** Weary, responsible, and determined to keep the children alive despite the pursuit
- **Voice:** Protective and restrained
- **Relationships:** Longtime friend of Socheon’s father, the Sakju Branch Leader; guardian of Socheon and Soyul during their flight

### Hyuk Mujin.md

# Hyuk Mujin (혁무진)

- **Safe through:** Chapter 184
- **Aliases:** None revealed
- **Role:** Level 50 First Rate martial artist from a wealthy Taiyuan textile-merchant family; Captain of the Gatekeepers at the Jin Family of Taiyuan; deputy squad leader of White Tiger Hall’s reconnaissance squad; candidate to become the next Master of the Gatekeeper Pavilion; has accepted Jin Taekyung’s invitation to train alongside Taekyung and Cheongpung in Taekyung’s private training ground
- **Personality:** Young, disciplined, persistent, and possessed of clear martial talent; suspicious of Jin Taekyung, and openly contemptuous of the family’s disgraced third son; believes loyalty and respectable conduct matter, but is also proud, hungry for glory, and an avid wuxia-novel reader who sometimes mistakes fictional Murim conventions for reality
- **Voice:** Formal and clipped when performing his duties; blunt and moralizing when addressing Taekyung
- **Relationships:** Gatekeeper under the Jin Family; deputy subordinate to Jin Taekyung in the reconnaissance squad; son of the Hyuk Family Textile Shop’s owners, with a younger sibling who removed the need for him to inherit the family business

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 185
- **Aliases:** Sleeping Dragon of Shanxi
- **Role:** Modern-world protagonist; recently fired after seven years at his job; C-rank Hunter who defeated eight B-rank Minotaurs and killed a Level 70 B-rank Minotaur Warrior in one blow; Peak Master with forty-five years of internal energy and the Scorching Yang Qi attribute after fully absorbing the Blazing Flame Divine Pill; possesses Jopil’s Flame Divine Palm manual and Ten-Thousand-Year Cold Iron sword; youngest son of the Jin Family of Taiyuan; new owner of a two-story detached house in Goyang intended for his family; Qi Sense reaches a seventy-meter radius; possesses one Temporary Strength Pill in his Inventory and has reserved it for a worst-case, life-threatening contingency; Level 71 with 2,400 Fame (+250) and seventy unassigned stat points; completed the Find the Master Artisan Quest after securing Jang Taebo’s agreement to forge his Ten-Thousand-Year Cold Iron into a spear; can roughly copy observed martial forms and copied the Plum Blossom Fist after three days of sparring with Cheongpung; killed Jin Baekyang, the Blade of Flowers, and was rendered unconscious with an Internal Injury by Jeok Cheongang’s Flame Divine Palm
- **Personality:** Hungry, self-aware, dryly observant, and willing to take a questionable opportunity when desperate; treats the impossible as a game until the danger becomes undeniable
- **Voice:** First-person, conversational, dryly self-mocking; uses vivid trap-and-prey imagery, game jargon, and occasional profanity
- **Relationships:** Jin Mukyung’s younger brother and current student; son of a deceased father; supports his mother and younger sibling; loves Song Song; has a strained relationship with Lee Seowol, the current Sect Leader of the Mount Heng Sword Sect, whose marriage proposal he has decided to reject

### Jin Wikyung.md

# Jin Wikyung (진위경)

- **Safe through:** Chapter 185
- **Aliases:** Junzi Sword
- **Role:** Thirty-five-year-old Lesser Family Head and future Family Head of the Jin Family of Taiyuan; has led the family in place of the absent Family Head for two years and established it as Shanxi Murim's hegemon
- **Personality:** Calm and authoritative in public; affectionate and protective toward Taekyung beneath a stern mask; accepts responsibility from his subordinates and shows immediate concern for family
- **Voice:** Restrained, formal, and commanding with subordinates; openly affectionate with Taekyung
- **Relationships:** Taekyung’s eldest brother and future Family Head; head of Wipeng; member of the Jin Family

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 185
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Socheon.md

# Socheon (소천)

- **Safe through:** Chapter 179
- **Aliases:** None revealed
- **Role:** Fourteen-year-old survivor of the Sakju Branch; older brother and protector of Soyul
- **Personality:** Watchful, frightened, and determined to survive and protect his sister after witnessing the massacre of his home
- **Voice:** A guarded child’s voice that becomes resolute under pressure
- **Relationships:** Son of the Sakju Branch Leader; older brother of Soyul; protected by Gong Yacheong; will return with Gong Yacheong to the rebuilt Sakju Branch in six months

### Soyul.md

# Soyul (소율)

- **Safe through:** Chapter 66
- **Aliases:** None revealed
- **Role:** Young survivor of the Sakju Branch; Socheon's younger sister
- **Personality:** Exhausted, frightened, and dependent on her brother during the flight from the massacre
- **Voice:** A young child’s voice
- **Relationships:** Younger sister of Socheon; daughter of the Sakju Branch Leader; protected by Gong Yacheong; will return with Gong Yacheong and Socheon to the rebuilt Sakju Branch in six months

### Wipeng.md

# Wipeng (위팽)

- **Safe through:** Chapter 185
- **Aliases:** Ghost Sword; God of Drinking
- **Role:** Jin Wikyung’s personal guard and commander of the thirty-elite pursuit team sent south under an assassin-hunt pretext
- **Personality:** Loyal, observant, teasing, and resigned to his master’s impulsive departures
- **Voice:** Weary and knowing; jokes with Jin Wikyung and uses Sound Transmission
- **Relationships:** Trusted guard and retainer of Jin Wikyung; the Human Butcher has claimed him as his personal target in the planned attack

## Korean source

```text
＃186화



진위경과 위팽.

이야기를 이어 갈수록 두 사람의 감정이 노골적으로 느껴졌다.

경악, 불신. 그리고 다시 경악.

“그, 그게 정녕 사실이더냐?”

하도 길게 이야기를 했더니 진이 다 빠질 지경이다. 나는 피곤함을 느끼며 대답했다.

“순도 십 할의 진실이니까 믿으세요.”

아까부터 넋이 나가 있던 위팽이 득달같이 달려들었다.

“삼공자. 이게 다 거짓말이면 진짜 나 죽고 당신 죽는 겁니다.”

“십 할이라니까요. 십 할!”

“아니, 그래도…….”

“아, 거짓 한 톨 안 섞인 십 할의 진실이라고요. 이런 십 할!”

“…….”

왠지 기분이 더러운데, 하는 얼굴로 멈칫한 위팽을 향해 검과 비급을 흔들었다.

이럴 때일수록 곱씹어 볼 시간을 주면 안 된다.

“정 의심이 가시면 직접 살펴보세요. 화염신장의 비급, 만년한철로 만든 검!”

“허억! 치우십시오. 어서!”

뱀파이어한테 십자가를 들이밀어도 이 정도 반응은 안 나올 거다.

“왜 그래요?”

위팽이 기겁한 얼굴로 대답했다.

“화염신장의 비급을 확인해 보라니, 본가를 멸문시키려고 작정했습니까?”

“아, 맞다. 그랬었지.”

화왕의 독문무공을 훔쳐봤다가는 뜨거운 맛을 보게 될 거다. 온몸이 불탈 정도의 뜨거운 맛을.

“어쨌든 전부 사실입니다. 여기 증인들도 있어요. 그렇지?”

죽은 듯이 구석에 앉아 있던 혁무진이 슬그머니 손을 들어 올렸다.

“외람되지만 전부 사실입니다.”

종류가 뭔지도 모르는 다과를 쑤셔 넣던 청풍도 진지한 얼굴로 입을 열었다.

“어오와어오!”

“…….”

저 증언은 별로 효력이 없을 것 같은데. 그보다 저놈의 다과는 도대체 언제까지 처먹는 거야. 화수분인가?

“이보게 위팽, 아무래도 태경이의 말이 사실인 것 같네만.”

진위경의 말에 위팽도 복잡한 얼굴로 고개를 끄덕였다.

“예. 도저히 믿기 힘든 사실이지만…… 믿을 수밖에 없군요.”

“화왕, 바로 그 화왕이란 말이지.”

진위경이 긴 숨을 내뱉었다. 망설이던 그의 손이 탁자에 올려 둔 [이름 없는 검]을 집어 들었다.

스릉.

투박한 검갑에서 모습을 드러내는 새하얀 검신. 서릿발 같은 예기를 뿜어내는 그것을 바라보던 진위경이 중얼거렸다.

“피 냄새가 나는구나.”

잠시 잊고 있었다. 진위경이 태원진가의 소가주이기 전에 한 사람의 검객이라는 것을.

나처럼 아이템 설명창을 보지 않고도 병기의 상태를 정확히 읽어 낸 그는 검을 도로 집어넣었다.

“태경아.”

“예.”

나는 자세를 바로 했다. 진위경이 나를 ‘막내’가 아닌 이름으로 불렀다는 것은 진중한 이야기를 할 때라는 의미다.

“이것들이 어떤 물건인지 아느냐?”

“귀물(貴物) 아닌가요? 천금을 들여도 얻기 힘든.”

천하를 오시할 수 있는 초절정 무공과 만년한철로 만들어진 희대의 명검.

내가 아는 무림인이라는 족속은 이것들을 얻기 위해 목숨이라도 걸 것이다.

진위경이 고개를 가로저었다.

“틀렸다.”

“네?”

“이것은 귀물(鬼物)이다. 사람의 혼을 빼놓고 미치게 만드는.”

“아.”

“그 귀신의 이름을 아느냐?”

나는 작게 뇌까렸다.

“탐욕.”

“그래, 탐욕이다. 모든 사람의 마음에 깃들어 있는 아주 끈질기고 위험한 놈이지.”

안다. 직접 겪어 봤으니 모를 수가 없었다.

수년 전 그날, 내 마음에 탐욕이란 놈이 깃들었고 그로 인해 가까운 사람들을 잃어야 했으니까.

“화왕이 어떤 의도로 네게 이런 위험한 물건들을 맡겼는지는 모르겠지만…… 이에 관한 모든 것들을 철저히 불문에 부쳐야 한다. 알겠느냐?”

시선과 자세는 오로지 나를 향하고 있지만 이 방 안의 모든 사람에게 하는 말이나 다름없다.

나와 혁무진, 마지막으로 청풍까지. 우리는 약속이라도 한 것처럼 동시에 대답했다.

“네.”

“명심하겠습니다, 소가주님.”

“아우하해호, 마아하해오.”

……저놈의 주둥이를 확 그냥.



* * *



진위경은 두꺼운 천을 걷어 올렸다. 격자무늬 창밖으로 멀어지는 진태경의 뒷모습이 보였다.

그의 등 뒤에 매어져 있는 투박한 검갑에 부딪친 햇살이 산산이 부서졌다.

“날씨 한 번 빌어먹게 좋군.”

“아까는 끝내준다고 하지 않으셨습니까?”

“그땐 그때고. 어차피 비슷한 말이야.”

“이번엔 느낌이 좀 다릅니다만.”

“다 알면서 말꼬리 좀 잡지 말게. 그러고 보니 아까 간다던 사람이 왜 아직도 있어?”

위팽이 힘 빠진 목소리로 대꾸했다.

“주군이야말로 말꼬리 잡지 마십시오. 안 그래도 머릿속이 복잡하니까요.”

그건 두 사람 모두에게 해당하는 말이었다. 진위경이 십 년은 늙은 얼굴로 중얼거렸다.

“도대체 무슨 일이 벌어지고 있는 거지?”

“저도 그게 궁금합니다.”

일 년, 아니 반년 남짓한 시간 동안 태원진가에 벌어진 일들을 돌이켜 보면 마(魔)가 낀 건 아닌지 의심이 들 정도다.

“하다 하다 이제는 화왕까지 나오는군.”

“듣기로는 여간 괴팍한 성정이 아니던데, 본가에 화가 미치지는 않을까 걱정입니다.”

“그 위기를 기회로 만들어야겠지.”

진위경이 찻잔을 어루만졌다. 다른 사람이 보기에는 상념에 잠긴 듯했지만, 그의 입술은 미세하게 달싹이는 중이었다.

- 그 일은 어떻게 되어 가고 있나?

전음의 의미를 알아차린 위팽은 자연스럽게 행동했다.

“차가 식었군요. 다시 내오라 할까요?”

- 아직 알아낸 바가 없습니다.

“괜찮네. 아직 마실 만해.”

- 살아남은 잔당들은?

“그러다가 몸 상하십니다.”

- 심문 과정에서 대부분이 죽었습니다.

“내 몸 생각해 주는 건 자네밖에 없군.”

- 그래서, 몇 명이나 남았나?

“저라도 신경 써 드려야 하지 않겠습니까. 주모(主母)도 안 계시는 마당에.”

- 셋입니다.

진위경의 손가락이 우뚝 멈췄다. 뜻밖의 소식에 순간 말을 이어야 한다는 사실도 잊을 정도였다.

- 고작 셋?

위팽이 한숨을 내쉬며 고개를 끄덕였다.

- 생각 이상으로 강력한 금제가 걸려 있었습니다. 이런 말씀을 드리게 되어 송구합니다만…… 제 능력으로는 역부족입니다.

- 자네 잘못이 아닐세. 본가의 역량이 부족한 탓이지.

- 명을 내려 주십시오.

진위경은 목이 타는 것을 느꼈다.

- 심문은 중단하게. 무슨 수를 써서라도 명줄을 단단히 붙들어 놔. 지금은 놈들만이 유일한 물증일세.

- 존명.

그는 차갑게 식어 있는 찻잔을 움켜쥐었다.

잘게 떨리는 찻물의 표면 위, 형체를 알 수 없는 일그러진 얼굴이 비쳤다. 마치 놈들처럼.

‘암천(暗天)…….’

어디서, 어떻게, 무슨 연유로 그런 짓을 벌였는지 알 수 없다.

그 어떤 것도 알아내지 못한 채 허공만 휘젓고 있는 상황.

그러나 진위경의 뇌리에는 한 가지 추측이 점점 확신으로 변해 가고 있었다.

‘매우 위험한 놈들이다. 산서성을 노린 건 시작에 지나지 않아.’

대장로는 오랜 세월을 인내하며 때를 기다렸다. 그러나 수십 년의 대계(大計)라고 하기에는 그 결과가 너무 초라하다.

진위경은 승리의 기쁨이 가신 후에야 그 사실을 알아차렸다.

‘이건…… 너무 쉽다.’

한 성을 손에 넣을 절호의 기회. 그러나 암천은 끝까지 모습을 드러내지 않았다. 마치 이 정도면 족하다는 듯이.

‘도대체 무엇을 노리는 것이냐.’

지금으로서는 짐작할 수 없다.

다만 자신이 놈들을 과대평가했기를 바랄 뿐.

“주군?”

“아.”

“너무 오래 자리를 비우셨습니다. 객들이 기다리고 있습니다.”

“……그런가.”

위팽의 부름에 진위경은 단숨에 찻잔을 비우고 일어났다.

“이만 가세나.”

태원진가를 위한 자리다. 지금은 승자의 기쁨을 마음껏 누려도 좋으리라.



* * *



겨울의 낮은 짧다. 태원진가로 돌아온 지 얼마 되지 않았는데 벌써 석양이 지기 시작했다.

‘그러고 보니 요 며칠간 운기조식을 제외하면 제대로 수련한 적이 없네.’

몸도 풀 겸, 전각에 딸린 연무장에서 무공을 수련 중이던 내게 뜻밖의 손님이 찾아온 것도 그때 즈음이었다.

“은인!”

“은인!”

“……?”

메아리야, 뭐야. 나는 소리가 난 방향으로 고개를 돌렸다.

“저 왔어요!”

입가에 뭔지 모를 양념을 잔뜩 묻힌 채 활짝 웃고 있는 청풍. 그리고…….

“은인! 저 소천입니다!”

“오랜만이오. 진 소협.”

“어?”

삭주지부의 생존자들, 공야청과 소천이다. 오랜만에 보는 얼굴들에 불쑥 반가움이 솟구쳤다.

‘그런데 뭐가 하나 빠진 것 같은데?’

고개를 갸웃거리던 그때, 그들 앞을 가로막은 돌담 아래서 칭얼거리는 소리가 들려왔다.

“나도! 소율이도 아저씨 볼래!”

“기다려 보거라.”

공야청이 뭔가를 집고 번쩍 들어 올려 목말을 태웠다. 자그마한 여자아이, 소율이가 방긋방긋 웃으며 손을 흔든다.

“아저씨!”

“오, 많이 컸는데.”

“아저씨도 많이 컸어!”

“그거 고맙네. 근데 나 아저씨 아냐.”

“누가 봐도 아저씨야!”

“……어, 그래.”

아저씨면 어떻고 아니면 어때. 실소를 흘린 나는 사람들에게 다가갔다.

“다들 잘 지냈어요?”

공야청이 희미하게 웃는 얼굴로 대답했다.

“물론이오.”

아직 핼쑥해 보이긴 해도 혈색이 좋다. 중독되어 사경을 헤매던 과거와는 확연히 나아진 모습이다.

‘애들도 잘 지내는 것 같고.’

한창 성장기인 소천은 못 본 사이 신장이 반 뼘은 더 커졌고, 소율은 볼이 통통하다.

그리고 청풍은 잘 먹었는지 배가 빵빵하게 부풀어 올라 있었다.

“…….”

그래. 잘 먹고 잘 커라.

스무 살이면 한창 클 때지.

“그런데 다들 어쩐 일로 왔어요?”

소천이 기다렸다는 듯 입을 열었다.

“혁 무사님께서 부탁하셨습니다. 곧 연회가 시작되는데 근무를 서러 가야 하니 은인께 대신 좀 말씀을 전해 달라고.”

“아, 연회.”

아까 얼핏 들었던 것도 같다. 저녁에 성대한 연회가 있을 예정이라고.

그때 입가에 묻은 양념을 핥아 먹고 있던 청풍이 깜짝 놀랐다.

“헛, 진짜요?”

“……뭐야, 알고 온 거 아닙니까?”

“네. 알면 좀 적게 먹었을 텐데!”

소율이도 충격받은 듯 눈을 동그랗게 떴다. 손에 들고 있던 당과가 툭 떨어진다.

“안 대! 소율이도 배부른데!”

“…….”

반응을 보아하니 두 사람이 어디서 만났는지 대충 짐작이 간다.

“뭐, 그래서 언제 시작한대요?”

“한 식경도 남지 않았습니다, 은인.”

“은인, 빨리 가요. 저 연회 처음이에요!”

“장소는?”

“이번에 새로 마련된 대연무장 앞입니다. 은인.”

“대연무장 앞이래요, 은인!”

“아, 거기.”

나는 들고 있던 수련용 창을 내려놓고 옆에 풀어 둔 보퉁이를 단단히 등에 고정시켰다.

물론 보퉁이에 든 물건은 화왕이 맡긴 검이었다.

“다들 가시죠.”

발걸음을 떼려다 멈칫했다. 아까부터 하고 싶은 말이 생각났기 때문이었다.

“아, 그리고 말인데…….”

“말씀하십시오, 은인.”

“왜요, 은인?”

나는 한숨을 푹 내쉬며 말을 이었다.

“한 사람만 은인이라고 해. 헷갈려.”

두 마리의 앵무새가 따로 없다. 두 은인무새들은 생각할 것도 없다는 듯 고개를 끄덕였다.

“명심하겠습니다. 은인.”

“알았어요, 은인.”

“…….”

아니, 생각 좀 하고 대답하라고.



* * *



대연무장. 말 그대로 가문 내에서 가장 큰 연무장인 그곳은 사람들로 인산인해였다.

“뭐야, 왜 이렇게 많아?”

초청받은 손님만 들어오는 게 아니었나? 의문을 해결해 준 건 청풍이었다.

“아까 숙수 아저씨한테 들었는데요, 소가주님께서 이런 좋은 날에는 다 같이 함께해야 한다고 밖에 있는 사람들까지 모두 받아들이라고 하셨대요.”

“그 사람들을 전부 다?”

“네. 그래서 숙수 아저씨가 굉장히 화냈어요. 소가주님이 생각이 없다고, 요리 도와줄 것도 아니면서 말 함부로 뱉는다고요.”

야무지게 당과를 빨아먹고 있던 소율이도 동조했다.

“맞아! 어디 가서 말하지 말라고 소율이한테 당과도 줬어!”

“……근데 그걸 왜 말하니?”

“합!”

나는 고개를 절레절레 저으며 발걸음을 옮겼다. 몇 걸음 걷기도 전에 태원진가의 무인이 다가왔다.

“두 공자님만 따로 모시겠습니다.”

“저는 아무 데서나 봐도 상관없는데. 아마 안 되겠죠?”

“예. 소가주님의 명입니다.”

자리가 자리인 만큼 어쩔 수 없다. 나는 공야청 일행과 가벼운 작별 인사를 나누고 마련된 자리로 이동했다.

극소수의 귀빈들만이 앉을 수 있는 상석(上席) 중 하나가 내 자리였다.

물론 그 말인즉슨…….

“청풍 사숙, 진 공자. 금방 다시 뵙는군요.”

매화삼절도 그중 하나라는 뜻이지.

제법 친근하게 알은척을 하는 백무성의 양 옆자리에는 그의 사제들이 앉아 있었다.

“아까는 제대로 인사 못 했죠? 은향이라고 해요.”



[Lv.75 은향]



기껏해야 동생인 하연이랑 비슷한 나이려나? 그녀와 인사를 마치자마자 불퉁한 음성이 튀어나왔다.

“젠장. 네놈이 내 옆자리냐?”

자리가 좁아 보일 정도의 거구. 철우였다.

“왜, 싫어?”

“너 같으면 좋겠냐?”

“나도 싫어서 하는 소리지. 마음이 통했네.”

“끔찍한 소리 하지 마라!”

“그럼 자리 바꾸든가.”

“어디로?”

“너 말고 거기 앉고 싶은 사람 많아. 저 아래에 서 있는 사람들 중에 아무하고나 바꿔.”

“이 개자식이!”

“지금 내 부모님 욕 한 거냐? 태원진가에서 진룰라 한 거야?”

몸을 부르르 떠는 철우를 백무성이 질책했다.

“이 녀석! 이게 무슨 망발이냐!”

“아니, 사형. 그게…….”

“시끄럽다. 진 소협, 사제를 대신해 사과드리겠소. 청풍 사숙께도 사죄드립니다.”

아까부터 내 뒤에 숨어 있던 청풍이 빼꼼 얼굴을 내밀었다.

“전 괜찮아요. 사질.”

나도 부드럽게 웃었다.

“저도 괜찮습니다. 한창 피가 끓을 나이 아닙니까. 이해해야죠.”

“나보다 다섯 살이나 어린놈이 뭐가 어째?”

“백 소협. 실례지만 자리 좀 바꿔 주실 수 있으십니까? 무서워서 옆에 앉기가 좀…….”

“둘째야!”

“후우, 후우우.”

나는 콧김을 뿜어내는 녀석의 옆자리에 털썩 앉았다. 우철우 좌청풍.

위치 한 번 기가 막히는군.

‘그런데 진위경은 어디 있지?’

아무리 둘러봐도 진위경과 위팽의 모습이 보이지 않던 그때.

쿵!

대연무장을 둘러싼 태원진가의 무인들이 병장기를 두드리기 시작했다. 무려 삼백이 넘어가는 그들에게서 칼 같은 기세와 파도 같은 기백이 휘몰아쳤다.

쿵! 쿵! 쿵!

흡사 전장의 북소리를 닮은 그것은 점점 커지며 모든 소음을 집어삼켰다. 그리고 이내…….

쿵!!

그 어느 때보다 큰 굉음과 함께 인(人)의 장막이 갈라졌다.
```

## Final English reading copy

```markdown
# Chapter 186

Jin Wikyung and Wipeng.

As the conversation continued, the emotions of the two men became increasingly obvious.

Shock. Disbelief. And then shock all over again.

“Th-That’s really true?”

I had talked for so long that I felt completely drained. Tired, I answered,

“It’s a hundred percent pure truth, so believe me.”

Wipeng, who had been staring blankly into space, suddenly lunged at me.

“Third Young Master. If all of this is a lie, then I’m really going to die—and so are you.”

“I said it’s a hundred percent. A hundred percent!”

“No, but still…”

“Ah, I mean a hundred percent truth with not a speck of lies mixed in. What the hell!”

“……”

Wipeng paused with an expression that seemed to say, *Why do I suddenly feel so disgusted?*

I waved the sword and martial arts manual at him.

Now more than ever, I couldn’t give him time to mull it over.

“If you’re really suspicious, inspect them yourself. The Flame Divine Palm manual, and a sword made of Ten-Thousand-Year Cold Iron!”

“Gasp! Put them away. Quickly!”

Even if someone shoved a cross in a vampire’s face, they probably wouldn’t react this strongly.

“What’s wrong?”

Wipeng answered with a horrified expression.

“You’re telling me to inspect the Flame Divine Palm manual? Have you decided to destroy our entire family?”

“Oh, right. That’s how it was.”

Anyone who stole a look at the Fire King’s signature martial art would get a taste of the heat—enough heat to burn their whole body.

“Regardless, everything is true. We have witnesses here, too. Right?”

Hyuk Mujin, who had been sitting in the corner like a corpse, cautiously raised his hand.

“Pardon me for interrupting, but everything is true.”

Cheongpung, who had been stuffing his mouth with snacks of unknown variety, spoke with a serious expression.

“Uh-oh-wa-uh-oh!”

“……”

That testimony probably wouldn’t carry much weight. More importantly, how long was that guy planning to keep eating those snacks? Was he some kind of inexhaustible jar?

“Wipeng, I believe Taekyung’s story really is true.”

At Jin Wikyung’s words, Wipeng nodded with a complicated expression.

“Yes. It’s a truth that’s nearly impossible to believe, but there’s no choice except to believe it.”

“The Fire King. The Fire King himself.”

Jin Wikyung let out a long breath. After hesitating, he reached for the Unnamed Sword resting on the table.

*Shing.*

The pure-white blade emerged from its rough scabbard.

As Jin Wikyung gazed at the sword, which radiated a frost-like sharpness, he murmured,

“It smells of blood.”

I had momentarily forgotten.

Before he was the Lesser Family Head of the Jin Family of Taiyuan, Jin Wikyung was a swordsman.

Unlike me, he didn’t need to look at an Item description window to accurately read the weapon’s condition. He slid the sword back into its scabbard.

“Taekyung.”

“Yes.”

I straightened my posture.

The fact that Jin Wikyung had called me by my name instead of *youngest* meant that he was about to say something serious.

“Do you know what these things are?”

“A precious treasure, aren’t they? The kind that would be difficult to obtain even if you spent a thousand nyang of gold.”

A Supreme Peak martial art that could let its wielder look down on the entire world, and a peerless sword forged from Ten-Thousand-Year Cold Iron.

The Murim martial artists I knew would risk their lives to obtain these things.

Jin Wikyung shook his head.

“Wrong.”

“Pardon?”

“These are ghostly objects. They take away a person’s soul and drive them mad.”

“Oh.”

“Do you know the name of that ghost?”

I muttered softly,

“Greed.”

“That’s right. Greed. A tenacious and dangerous creature dwelling in everyone’s heart.”

I knew.

I had experienced it firsthand, so there was no way I couldn’t.

On that day several years ago, greed had taken root in my heart, and because of it, I had lost people close to me.

“I don’t know what intentions the Fire King had when he entrusted these dangerous objects to you, but… everything related to this must be kept completely secret. Do you understand?”

His gaze and posture were directed solely at me, but his words were meant for everyone in the room.

Me, Hyuk Mujin, and finally Cheongpung.

As though we had made a promise, we answered at the same time.

“Yes.”

“I’ll keep it in mind, Lesser Family Head.”

“Ah-uh-ah-hae-ho, ma-ah-hae-oh.”

……

That damn mouth of his. I ought to just…

* * *

Jin Wikyung lifted the thick curtain. Through the latticework window, he could see Jin Taekyung’s back growing more distant.

Sunlight struck the rough scabbard strapped to Taekyung’s back and shattered into fragments.

“The weather is fucking beautiful.”

“Didn’t you say it was fantastic earlier?”

“That was then. It’s basically the same thing.”

“This feels a little different.”

“Don’t nitpick when you already know what I mean. Come to think of it, why is the person who said he was leaving still here?”

Wipeng answered in a weary voice.

“You’re the one nitpicking, my lord. My head is already complicated enough.”

That applied to both of them.

Jin Wikyung murmured with a face that looked ten years older.

“What on earth is happening?”

“I’m curious about that myself.”

When he looked back over everything that had happened to the Jin Family of Taiyuan over the past year—or rather, the past six months or so—it was enough to make him wonder whether some demon had gotten involved.

“Now even the Fire King has appeared.”

“I’ve heard he has an exceptionally eccentric temperament. I’m worried he might bring calamity down on our family.”

“We have to turn this crisis into an opportunity.”

Jin Wikyung gently caressed his teacup. To anyone else, he might have appeared lost in thought, but his lips were moving almost imperceptibly.

*How is that matter progressing?*

Wipeng understood the meaning of the Sound Transmission and acted naturally.

“The tea has gone cold. Shall I have them bring out a fresh cup?”

*We haven’t learned anything yet.*

“It’s fine. It’s still drinkable.”

*What about the surviving remnants?*

“You’ll ruin your health if you keep doing that.”

*Most of them died during the interrogation.*

“You’re the only one who worries about my health.”

*So, how many are left?*

“Shouldn’t I at least look after you, with the Lady of the House not here?”

*Three.*

Jin Wikyung’s fingers stopped dead.

The news was so unexpected that, for a moment, he even forgot that he was supposed to continue speaking.

*Only three?*

Wipeng sighed and nodded.

*They had a far more powerful restriction placed on them than expected. I’m sorry to say this, but… my abilities aren’t enough.*

*It isn’t your fault. Our family’s capabilities are lacking.*

*Give me your orders.*

Jin Wikyung felt his throat grow dry.

*Stop the interrogation. Keep them clinging to life by whatever means necessary. Right now, those men are our only physical evidence.*

*Understood.*

He closed his hand around the cold teacup.

On the trembling surface of the tea, a distorted face with no discernible features was reflected.

Just like those men.

*Dark Heaven…*

He didn’t know where, how, or why they had done such a thing.

He was flailing at empty air without learning a single thing.

Yet one suspicion in Jin Wikyung’s mind was gradually hardening into certainty.

*They’re extremely dangerous. Targeting Shanxi Province was only the beginning.*

The Head Elder had endured for many years while waiting for his moment. But for a decades-long grand design, the results were far too shabby.

Jin Wikyung realized that only after the joy of victory had faded.

*This was… too easy.*

It had been a perfect opportunity to seize an entire province.

Yet Dark Heaven had never revealed themselves. It was as if this much had been enough for them.

*What on earth are they after?*

For now, he had no idea.

He could only hope that he had overestimated them.

“My lord?”

“Ah.”

“You’ve been away from your seat too long. The guests are waiting.”

“……Is that so?”

At Wipeng’s call, Jin Wikyung drained his teacup in one gulp and rose.

“Let us go.”

This was a gathering for the Jin Family.

For now, it was all right to savor the joy of victory to his heart’s content.

* * *

Winter days were short.

I had only just returned to the Jin Family of Taiyuan, but the sun was already beginning to set.

*Come to think of it, aside from circulating my qi, I haven’t had a proper training session in days.*

It was around then, while I was training in the ground attached to my pavilion to loosen up my body, that some unexpected guests came to see me.

“Benefactor!”

“Benefactor!”

“……?”

Was that an echo or something?

I turned my head toward the direction of the voices.

“I’m here!”

Cheongpung was smiling brightly, his mouth covered in a thick layer of some mysterious sauce. And then there was…

“Benefactor! It’s Socheon!”

“It’s been a while, Young Hero Jin.”

“Huh?”

They were the survivors of the Sakju Branch, Gong Yacheong and Socheon.

Seeing their familiar faces after so long, I felt a sudden rush of happiness.

*But it feels like someone’s missing.*

Just as I was tilting my head in confusion, a whining voice came from beneath the stone wall blocking my view of them.

“Me too! Soyul wants to see Uncle too!”

“Wait a moment.”

Gong Yacheong reached down, scooped something up, and hoisted it onto his shoulders.

The small girl, Soyul, smiled brightly and waved her hand.

“Uncle!”

“Oh, you’ve grown a lot.”

“You’ve grown a lot too, Uncle!”

“Thanks for that. But I’m not an uncle.”

“Anyone can see you’re an uncle!”

“……Sure.”

What did it matter whether I was an uncle or not?

I let out a quiet laugh and walked toward them.

“Has everyone been well?”

Gong Yacheong answered with a faint smile.

“Of course.”

He still looked somewhat gaunt, but his complexion was healthy. He was clearly much better than when he had been poisoned and hovering on the verge of death.

*The kids seem to be doing well, too.*

Socheon was in the middle of his growth period, and in the time since I had last seen him, he had grown another half a handspan taller. Soyul’s cheeks were plump.

And Cheongpung’s stomach had puffed up as though he had been eating well.

“……”

Right. Eat well and grow well.

Twenty was still a good age for growing.

“But what brings everyone here?”

Socheon spoke as though he had been waiting for me to ask.

“Martial Artist Hyuk asked us to come. The banquet is about to begin, but he has to go stand watch, so he asked us to deliver a message to you in his place.”

“Oh, the banquet.”

I vaguely remembered hearing something about it earlier. There was supposed to be a grand banquet in the evening.

Cheongpung, who had been licking the sauce from around his mouth, suddenly looked shocked.

“Gasp! Really?”

“……What? Didn’t you come here knowing that?”

“Yes. If I’d known, I would have eaten less!”

Soyul also opened her eyes wide in shock. The candied treat in her hand slipped to the ground.

“No! Soyul’s full too!”

“……”

Judging from their reactions, I could roughly guess where the two of them had met.

“Well, when does it start?”

“Less than half an hour remains, Benefactor.”

“Benefactor, hurry! This is my first banquet!”

“Where is it?”

“In front of the new Grand Training Ground, Benefactor.”

“They said it’s in front of the Grand Training Ground, Benefactor!”

“Ah, there.”

I set down the training spear I was holding and tightly secured the bundle I had laid out beside me to my back.

Of course, the item inside the bundle was the sword entrusted to me by the Fire King.

“Let’s all go.”

I was about to set off when I stopped.

I had thought of something I had wanted to say for a while.

“Oh, and one more thing…”

“Please speak, Benefactor.”

“What is it, Benefactor?”

I let out a deep sigh before continuing.

“Only one of you should call me Benefactor. It’s confusing.”

They were exactly like two parrots.

The two Benefactor parrots nodded as though they didn’t need to think about it.

“I’ll keep that in mind, Benefactor.”

“Okay, Benefactor.”

“……”

No, think before you answer.

* * *

The Grand Training Ground.

As its name suggested, it was the largest training ground in the family, and it was packed with people.

“What the hell? Why are there so many people?”

Weren’t only invited guests allowed inside?

Cheongpung was the one who answered my question.

“I heard it from the cook earlier. He said the Lesser Family Head told them that everyone should be together on a day this wonderful, and ordered them to let in all the people outside, too.”

“All of them?”

“Yes. So the cook got really angry. He said the Lesser Family Head had no common sense and shouldn’t run his mouth when he wasn’t going to help with the cooking.”

Soyul, who had been sucking happily on a candied treat, chimed in.

“That’s right! He even gave Soyul a candied treat and told her not to tell anyone!”

“……Then why are you telling us?”

“Gasp!”

I shook my head and continued walking.

I had only taken a few steps when a martial artist from the Jin Family approached us.

“We’ll escort the two Young Masters to their designated seats.”

“I don’t mind watching from anywhere. I’m guessing that won’t be allowed, right?”

“No, Young Master. It is the Lesser Family Head’s order.”

Given the circumstances, there was nothing I could do.

I exchanged a light farewell with Gong Yacheong and the others before moving to the seat prepared for me.

My seat was one of the places of honor reserved for the very small number of distinguished guests.

Of course, that meant…

“Martial Uncle Cheongpung, Young Master Jin. We meet again so soon.”

The Three Plum Blossom Elites were among them.

Baek Museong had his junior disciples seated on either side of him. He greeted us with a fairly friendly expression.

“We didn’t get to properly introduce ourselves earlier, did we? I’m Eunhyang.”

> **System**
> **Level:** 75  
> Eunhyang

She was probably around the same age as my younger sister, Hayeon.

The moment I finished greeting her, a sullen voice burst out.

“Damn it. You’re sitting next to me?”

Chulwoo was a massive man, large enough to make the seat look cramped.

“Why? You don’t like it?”

“Would you?”

“I don’t like it either. That’s why I said it. Guess we agree on something.”

“Don’t say disgusting things!”

“Then switch seats.”

“With whom?”

“Lots of people besides you would love to sit there. Switch with anyone standing down below.”

“You son of a bitch!”

“Did you just insult my parents? Are you trying to pull a Jin-rula in the Jin Family of Taiyuan?”

Chulwoo’s body trembled as Baek Museong scolded him.

“You! What kind of outrageous nonsense is this?”

“No, Senior Brother. It’s just…”

“Quiet. Young Hero Jin, I apologize in place of my Junior Brother. I also apologize to Martial Uncle Cheongpung.”

Cheongpung, who had been hiding behind me, cautiously peeked his head out.

“I’m fine, Martial Nephew.”

I also smiled gently.

“I’m fine too. Aren’t you at the age when your blood is running hot? We have to be understanding.”

“You’re five years younger than me, you little punk. What did you just say?”

“Young Hero Baek, if you don’t mind, could you switch seats with me? I’m a little afraid to sit next to him…”

“Second!”

“Whoo. Whoo-hoo.”

I dropped into the seat beside the snorting Chulwoo.

Chulwoo on my right, Cheongpung on my left.

What a spectacular arrangement.

*Where is Jin Wikyung?*

No matter how much I looked around, I couldn’t see Jin Wikyung or Wipeng.

Then—

*Boom!*

The martial artists of the Jin Family surrounding the Grand Training Ground began striking their weapons.

There were more than three hundred of them, and from their ranks surged an aura sharp as a blade and a spirit as powerful as a wave.

*Boom! Boom! Boom!*

The sound resembled the drums of a battlefield. It grew louder and louder until it swallowed every other noise.

And then…

*BOOM!*

With a thunderous crash louder than any before it, the human curtain split apart.
```
