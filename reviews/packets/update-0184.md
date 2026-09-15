<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0184.txt",
      "sha256": "c51dca093b7475a44f2d558ef17c00a541897595dc6837ea07825bc899498a78",
      "bytes": 14607
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "7e22a870d76038823f17139d273f5b5dd2547d48452b236ae45a8ff17a17e14a",
      "bytes": 3175
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "de851ea30db4b288cf8cc9ce4ed4b3a48c09056b3a6a1481ded35c1c467e1590",
      "bytes": 45947
    },
    {
      "path": "characters/Baek Museong.md",
      "sha256": "a4c66644eddeb77b49787ba685d54885c7169c81537fa3efffca291f6a78b204",
      "bytes": 668
    },
    {
      "path": "characters/Cheongpung.md",
      "sha256": "3f56eea38b465bb321237f5a1d1f59a76de5d306acb0f8f0f986cfcd3e399c25",
      "bytes": 1755
    },
    {
      "path": "characters/Chulwoo.md",
      "sha256": "05db62776da447aa65dc5074531fd4d6d49b8ac740ec35ef2e868883fff0aac4",
      "bytes": 750
    },
    {
      "path": "characters/Gong Ilhyuk.md",
      "sha256": "de1460c4adaad7b04c45ffe67492850e04c485ed454230ab4388be53927cde2f",
      "bytes": 614
    },
    {
      "path": "characters/Human Butcher.md",
      "sha256": "59c814147b000624e14f238b86e8fe7b0d83f982313807c7256f38a38ab9c6de",
      "bytes": 667
    },
    {
      "path": "characters/Hyuk Mujin.md",
      "sha256": "0f14548cc321958908b701c1e4cff04c40e03a10718c54abe41420b3879daba5",
      "bytes": 5558
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "0116fbec9a7133ac1395a13cf81caf3aceea41c6e533e061f2f3441aec4da2b1",
      "bytes": 24938
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "65440eae1fdf1079f695b8a5a5f05575617293f3293e867fa706a711732c0b05",
      "bytes": 622
    },
    {
      "path": "characters/Li Feng.md",
      "sha256": "6c8a99bb27297712caeeb1d457c4b858fc463b9885b7537554f804b4ddeced10",
      "bytes": 888
    },
    {
      "path": "characters/Mae Jonghak.md",
      "sha256": "c54bec8e1c6b14bc5e7052a09334d929f52fd7f792503077acada192a6513336",
      "bytes": 808
    },
    {
      "path": "characters/Wipeng.md",
      "sha256": "18665fafdbc4aadb554dcfd7ad3e271328c5d0890382ca41585a4b9a230c7057",
      "bytes": 4701
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "56b0ed6c9b1ce8d0c9dde7a3ee528b1747927448084c651bf00ef0f65f50ad7c",
      "bytes": 37292
    }
  ],
  "estimated_tokens": 33532
}
-->

# Durable State Update — Chapter 184

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 184. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 20 concise items, `open_questions` to at most 8
items, and `temporary_decisions` to at most 8 items. Keep the serialized context
under 16384 UTF-8 bytes. Use only chapter
numbers through 184. `profile_updates` may replace one exact, uniquely occurring
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
  "chapter": 184,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 184,
    "continuity_sources": [184],
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
    "Jin Wikyung has led the Jin Family in place of the absent Family Head for two years and has established it as Shanxi Murim's hegemon.",
    "The Jin Family is holding a three-day grand banquet beginning on New Year's Day, with support from Huashan, the imperial family, and Shanxi Murim.",
    "Jin Wikyung and Wolhwa finalized a cooperative alliance between the Jin Family and the Lower District Sect.",
    "The Heavenly Wind Band was annihilated near Datong by an unknown Supreme Peak master; Jin Taekyung privately suspects Mae Jonghak.",
    "Jin Taekyung is absent while having a weapon forged and has stopped sending news; Jin Mukyung is undergoing seclusion training after enlightenment.",
    "Woo Hwangtae sought an audience and apology regarding Woo Jintae, became enraged at the Jin Family's representatives, and was prevented from escalating the conflict.",
    "Baek Museong and the Huashan group are present at the Jin Family's gates; Baek Museong has now met Jin Wikyung.",
    "The Treasured Jade remains missing.",
    "Jang Taebo is forging Taekyung's commissioned weapon.",
    "Baek Museong is the first Senior Brother of the Three Plum Blossom Elites and restrains Chulwoo with Sound Transmission.",
    "Chulwoo is the second of the Three Plum Blossom Elites, bears the epithet Defeated Flower Fist, and is a Level 95 early-Peak martial artist.",
    "Eunhyang is the youngest junior disciple in Baek Museong's group, bears the epithet Flower Sword Phoenix, and was found after becoming separated in the crowd.",
    "Taekyung, Hyuk Mujin, and Cheongpung returned to Taiyuan after three days away.",
    "Taekyung is temporarily carrying Jeok Cheongang's Unnamed Sword outside his inventory.",
    "Cheongpung has speculated that Jeok Cheongang may want Taekyung as his Disciple; this is unconfirmed.",
    "Chulwoo singled out Woo Hwangtae from the crowd, fought with Taekyung, and returned with him after Wipeng intervened.",
    "Jin Taekyung and Chulwoo are publicly perceived as newly close despite their continuing private rivalry."
  ],
  "continuity_sources": [
    183
  ],
  "open_questions": [
    "Who annihilated the Heavenly Wind Band near Datong?",
    "What consequences will follow Taekyung's absence from the Jin Family's grand banquet?",
    "When will Jang Taebo complete Taekyung's weapon?",
    "Who has the Treasured Jade, or was it lost by Jopil?",
    "Does Jeok Cheongang actually intend to take Taekyung as his Disciple?",
    "What consequences will follow Woo Hwangtae's conflict with Chulwoo and the Jin Family?"
  ],
  "safe_through": 183,
  "temporary_decisions": [
    "Render 원단 as “New Year's Day,” 천풍단 as “Heavenly Wind Band,” 천검진인 as “Heavenly Sword True Person,” and 매화삼절 as “Three Plum Blossom Elites.”",
    "Render 수문각 as “Gate Guard Pavilion.”",
    "Render 장주 as “Lord.”",
    "Render 패화권 as “Defeated Flower Fist.”",
    "Render 산서기협 as “Shanxi Extraordinary Hero,” distinct from 산서괴협.",
    "Render 절정 초입 as “early Peak” and 권기 as “fist qi.”"
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

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 위팽     | **Wipeng**         |
| 혁무진    | **Hyuk Mujin**     |
| 백무성    | **Baek Museong**   |
| 철우     | **Chulwoo**        |
| 매종학    | **Mae Jonghak**    |
| 청풍     | **Cheongpung**     |
| 공일혁    | **Gong Ilhyuk**    |
| 산서잠룡   | **Sleeping Dragon of Shanxi** | Jin Taekyung   |
| 검성     | **Sword Saint**               | Mae Jonghak    |
| 태원진가   | **Jin Family of Taiyuan**        |
| 화산파    | **Huashan**                      |
| 종남파    | **Zhongnan Sect**                |
| 절정     | **Peak**          |
| 무인     | **martial artist**                               | Default term                                          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 전음     | **Sound Transmission**                           | Fixed skill terminology; preserve the internal-energy mechanism when the source explains it, but do not add an explanation where it does not |
| 후기지수   | **young prodigy** / **rising martial artist**    | Contextual, not a title                               |
| 정파     | **orthodox faction**                             |                                                       |
| 기루     | **pleasure house**                               |                                                       |
| 문주     | **Sect Leader**                              |
| 장문인    | **Sect Leader**                              |
| 장로     | **Elder**                                    |
| 제자     | **Disciple**                                 |
| 사제     | **Junior Brother**                           |
| 사숙     | **Martial Uncle**                            |
| 은인     | **Benefactor**                               |
| 명성               | **Fame**                       |
| 산서     | **Shanxi**             |
| 태원     | **Taiyuan**            |
| 청해     | **Qinghai**            |
| 화산     | **Huashan**            |
| 노부      | **this old man / I**                                            |
| 본문      | **our sect / this sect**                                        |
| 소협      | **Young Hero**                                                  |
| 공자      | **Young Master**                                                |
| 도사      | **Daoist**                                                      |
| 인도 | **Human Butcher** | Epithet of a mysterious Han Chinese mounted-bandit power commanding fifty subordinates. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 이풍 | **Li Feng** | Shanxi Province's Assistant Military Commissioner; former Huashan lay disciple |
| 삼공자 | **Third Young Master** | Title used for Jin Taekyung. |
| 산서성 | **Shanxi Province** | Province containing the Lower District Sect branches. |
| 송이 | **Song-i** | Short form used for Song Song; Taekyung's love interest. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 구파일방 | **Nine Sects and One Gang** | Major Murim grouping. |
| 오대세가 | **Five Great Families** | Major Murim grouping. |
| 종남삼수 | **Three Hands of Zhongnan** | Three renowned Zhongnan Sect martial artists invited to the gathering |
| 은자 | **silver nyang** | Silver currency unit. |
| 화산일학 | **Huashan’s Lone Crane** | Epithet of Baek Museong. |
| 매화삼절 | **Three Plum Blossom Elites** | Collective title for the current Sect Leader’s three exceptional disciples. |
| 세가 | **great family** | Murim category Jin Wikyung hopes the Jin Family will attain. |
| 하곡 | **Hequ** | Route and Jin Family branch targeted as the alliance's entry point into Shanxi. |
| 천검진인 | **Heavenly Sword True Person** | Taoist-style title of the current Sect Leader of Huashan, who once commissioned a sword from Jang Taebo. |
| 천하오대세가 | **Five Great Families** | Expanded source form of 오대세가. |
| 패화권 | **Defeated Flower Fist** | Chulwoo’s epithet. |

## Listed compact profiles

### Baek Museong.md

# Baek Museong (백무성)

- **Safe through:** Chapter 182
- **Aliases:** Huashan’s Lone Crane
- **Role:** First-generation disciple of Huashan, first of the Three Plum Blossom Elites, and leader of the journey to meet Cheongpung.
- **Personality:** Calm, responsible, principled, and patient, though visibly weary of his junior disciples’ antics.
- **Voice:** Gentle and polite with strangers; measured and stern when correcting junior disciples.
- **Relationships:** The current Huashan Sect Leader is his Master; Chulwoo and Eunhyang are his junior disciples; he met Cheongpung ten years ago.

### Cheongpung.md

# Cheongpung (청풍)

- **Safe through:** Chapter 183
- **Aliases:** None
- **Role:** Mysterious young man encountered at Honghwa Inn; an exceptionally young Peak master whose Level Jin Taekyung cannot determine through Qi Sense; the grandson and disciple of Sword Saint Mae Jonghak, who secretly descended from Huashan to seek out and defeat the Ten Dragons and Phoenixes, beginning with Jin Mukyung; he has no martial title yet, naturally opened his Governor Vessel through enlightenment two years ago, has begun teaching Jin Taekyung and Hyuk Mujin using Mae Jonghak's training method, has now used Sword Energy and the Zaha Divine Technique during his spar with Taekyung, defended Taekyung from Jeok Cheongang with Huashan martial arts, and Prince Shangshan will only accept his autograph after he gains one
- **Personality:** Affable, dreamy, hazy, and childlike in manner, with innocent curiosity, delight in novel public attention, a deep love of martial arts, and a martial artist's competitive pride; he becomes unsettled when someone copies his martial arts
- **Voice:** Dreamy and hazy, with innocent, polite phrasing
- **Relationships:** Mae Jonghak, the Sword Saint, is his grandfather and martial instructor; Cheongpung came to Huashan at about age three or four rather than being born there, lived with Mae Jonghak at a hidden residence, and secretly left Huashan without his grandfather's knowledge to challenge the Ten Dragons and Phoenixes; Baek Museong met him ten years ago and is now traveling with the Three Plum Blossom Elites to meet him; Li Feng is his Martial Nephew within Huashan's hierarchy; calls Jin Taekyung and Hyuk Mujin Benefactors after they feed him

### Chulwoo.md

# Chulwoo (철우)

- **Safe through:** Chapter 183
- **Aliases:** None
- **Role:** Level 95 early-Peak Huashan martial artist, second junior disciple of Baek Museong, second of the Three Plum Blossom Elites, and wielder of the Defeated Flower Fist.
- **Personality:** Blunt, defensive, physically intimidating, short-sighted, quick-tempered, coarse, and unconcerned with personal cleanliness.
- **Voice:** Hearty, casual, and blunt, with crude insults, indignant protests, and a competitive streak when provoked.
- **Relationships:** Baek Museong is his Senior Brother; Eunhyang is his fellow junior disciple and frequent bickering partner; he serves under Huashan’s Sect Leader.

### Gong Ilhyuk.md

# Gong Ilhyuk (공일혁)

- **Safe through:** Chapter 142
- **Aliases:** None
- **Role:** The third member of the Three Hands of Zhongnan and a Zhongnan Sect martial artist from Shaanxi
- **Personality:** Sharp-tongued, mocking, and openly antagonistic toward Li Feng
- **Voice:** Casual, taunting, and deliberately provocative
- **Relationships:** Member of the Zhongnan Sect's Three Hands; Gong Iljung, the Sect Leader and Wind-and-Cloud Sword Lord, is his father's cousin; involved in a ten-year-old humiliating martial grievance with Li Feng

### Human Butcher.md

# Human Butcher (인도)

- **Safe through:** Chapter 183
- **Aliases:** None
- **Role:** Former mysterious Han Chinese mounted-bandit power in Northern Gaoyuan commanding fifty subordinates; a Peak master killed by an unnamed old man in a single move
- **Personality:** Cold, intimidating, and murderous; he kills people as though slaughtering livestock
- **Voice:** Cold, curt, and quietly threatening
- **Relationships:** He is one of four powerful participants at the Northern Gaoyuan gathering, intimidates Temur, and has claimed Ghost Sword Wipeng as his personal target in the proposed attack

### Hyuk Mujin.md

# Hyuk Mujin (혁무진)

- **Safe through:** Chapter 183
- **Aliases:** None revealed
- **Role:** Level 50 First Rate martial artist from a wealthy Taiyuan textile-merchant family; Captain of the Gatekeepers at the Jin Family of Taiyuan; deputy squad leader of White Tiger Hall’s reconnaissance squad; candidate to become the next Master of the Gatekeeper Pavilion; has accepted Jin Taekyung’s invitation to train alongside Taekyung and Cheongpung in Taekyung’s private training ground
- **Personality:** Young, disciplined, persistent, and possessed of clear martial talent; suspicious of Jin Taekyung, and openly contemptuous of the family’s disgraced third son; believes loyalty and respectable conduct matter, but is also proud, hungry for glory, and an avid wuxia-novel reader who sometimes mistakes fictional Murim conventions for reality
- **Voice:** Formal and clipped when performing his duties; blunt and moralizing when addressing Taekyung
- **Relationships:** Gatekeeper under the Jin Family; deputy subordinate to Jin Taekyung in the reconnaissance squad; son of the Hyuk Family Textile Shop’s owners, with a younger sibling who removed the need for him to inherit the family business

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 183
- **Aliases:** Sleeping Dragon of Shanxi
- **Role:** Modern-world protagonist; recently fired after seven years at his job; C-rank Hunter who defeated eight B-rank Minotaurs and killed a Level 70 B-rank Minotaur Warrior in one blow; Peak Master with forty-five years of internal energy and the Scorching Yang Qi attribute after fully absorbing the Blazing Flame Divine Pill; possesses Jopil’s Flame Divine Palm manual and Ten-Thousand-Year Cold Iron sword; youngest son of the Jin Family of Taiyuan; new owner of a two-story detached house in Goyang intended for his family; Qi Sense reaches a seventy-meter radius; possesses one Temporary Strength Pill in his Inventory and has reserved it for a worst-case, life-threatening contingency; Level 71 with 2,400 Fame (+250) and seventy unassigned stat points; completed the Find the Master Artisan Quest after securing Jang Taebo’s agreement to forge his Ten-Thousand-Year Cold Iron into a spear; can roughly copy observed martial forms and copied the Plum Blossom Fist after three days of sparring with Cheongpung; killed Jin Baekyang, the Blade of Flowers, and was rendered unconscious with an Internal Injury by Jeok Cheongang’s Flame Divine Palm
- **Personality:** Hungry, self-aware, dryly observant, and willing to take a questionable opportunity when desperate; treats the impossible as a game until the danger becomes undeniable
- **Voice:** First-person, conversational, dryly self-mocking; uses vivid trap-and-prey imagery, game jargon, and occasional profanity
- **Relationships:** Jin Mukyung’s younger brother and current student; son of a deceased father; supports his mother and younger sibling; loves Song Song; has a strained relationship with Lee Seowol, the current Sect Leader of the Mount Heng Sword Sect, whose marriage proposal he has decided to reject

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 183
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Li Feng.md

# Li Feng (이풍)

- **Safe through:** Chapter 146
- **Aliases:** None
- **Role:** Assistant Military Commissioner of Shanxi Province; former Huashan lay disciple who left the sect nearly ten years ago
- **Personality:** Resolute, proud, blunt, and hostile toward political and martial rivals
- **Voice:** Formal and restrained in official settings; dry and cutting with opponents
- **Relationships:** Former lay disciple of Huashan; visited the hidden residence of his Grandmaster Mae Jonghak and saw ten-year-old Cheongpung there; recognizes Cheongpung as his Martial Uncle; direct subordinate and political rival of Hong Jin, the Deputy Military Commissioner; agrees to act as Hong Jin's intermediary with Huashan and send a messenger pigeon to his Master; bears a humiliating martial grievance involving Gong Ilhyuk

### Mae Jonghak.md

# Mae Jonghak (매종학)

- **Safe through:** Chapter 182
- **Aliases:** Sword Saint
- **Role:** Sword Saint and Cheongpung's grandfather; more than forty years ago he sought Jeok Cheongang's help against the Demonic Cult, fought Jeok at Mount Jiuhua for seven days and seven nights, and drew with him.
- **Personality:** Not established in this chapter.
- **Voice:** Not established in this chapter.
- **Relationships:** Cheongpung's grandfather and martial instructor; taught him the Taeeul Miri Palm; secretly entered Huashan while its Sect Leader slept, left a dagger and handwritten note, and then went into hiding, prompting Huashan's search; fought Jeok Cheongang at Mount Jiuhua more than forty years ago and left after their draw.

### Wipeng.md

# Wipeng (위팽)

- **Safe through:** Chapter 183
- **Aliases:** Ghost Sword; God of Drinking
- **Role:** Jin Wikyung’s personal guard and commander of the thirty-elite pursuit team sent south under an assassin-hunt pretext
- **Personality:** Loyal, observant, teasing, and resigned to his master’s impulsive departures
- **Voice:** Weary and knowing; jokes with Jin Wikyung and uses Sound Transmission
- **Relationships:** Trusted guard and retainer of Jin Wikyung; the Human Butcher has claimed him as his personal target in the planned attack

## Korean source

```text
＃184화



수백이 아니라 천 명도 될 것 같다. 우리는 태원진가 무인들의 경호를 받으며 엄청나게 몰려든 인파 속을 헤쳐 나갔다.

‘기분 끝내주네.’

중화권 스타가 된 기분이다. 한류 열풍 뭐 그런 거.

아니, 실제로 한국인이니까 틀린 말은 아닌가?

“산서잠룡! 여기 한 번만 봐 주시오!”

“꺄악! 진 소협!”

“응애애애!”

똥개도 자기 집에서는 반은 먹고 들어간다고 했다.

아무리 매화삼절이 유명해도 산서성의 자랑, 태원의 아들을 홈그라운드에서 이길 수는 없었다.

흐뭇하게 웃으며 손을 흔드는 내게 철우가 속삭였다.

“입꼬리 올라간 것 봐라. 좋냐?”

“입꼬리 내려간 것 봐라. 우냐?”

“이 산서성 촌놈이.”

“네, 다음 자연인.”

“이런 개…….”

“뭐, 이…….”

다시 한번 불꽃이 튀려던 그때, 한 줄기 전음이 귓가를 파고들었다.

- 삼공자!

위팽이 험악한 표정으로 나를 노려보는 중이었다. 당장 뺨이라도 한 대 갈기고 싶어 하는 얼굴이다.

철우에게도 비슷한 전음을 보냈는지 놈도 불만 섞인 얼굴로 한마디를 툭 덧붙였다.

“봐줬다.”

나는 코웃음으로 대답을 대신했다.

사람들의 환호성을 듣고 철우, 저놈이 화산파에서도 제법 잘 나가는 후기지수라는 걸 처음 알았을 때는 꽤 놀랐지만 그뿐이었다.

‘매화삼절이면 뭐, 어쩌라고?’

화산파의 무공이라면 이미 충분히 겪어 봤다. 내 옆에서 털레털레 걷고 있는 어떤 한 사람 덕분에.

“배고파. 배고파요.”

“…….”

언제 봐도 희한한 놈이지만 청풍이 화산파의 진산절학을 섭렵한 절정 고수라는 건 부정할 수 없는 사실이다.

때문에 철우가 어떤 무공을 사용하더라도 대응할 자신이 있었다. 놈이 나보다 앞서는 거라고는 화산파라는 배경뿐이다.

“…….”

아, 아니다. 방금 했던 말 취소.

다시 생각해 보니까 배경 차이가 심각하다. 태원진가의 위상이 아무리 올랐어도 구파일방은 압도적이다.

‘시벌, 졌네.’

내가 생각하는 구파일방, 천하오대세가는 무림의 기업 연합이나 다름없다. 안 그래도 힘센 대기업들이 연합체를 꾸려서 다구리를 놓으니 당할 놈들이 없는 거다.

다행히 나름 정파랍시고 골목 상권까지 침범하진 않아서 태원진가 같은 중소기업도 위로 치고 올라가는 거지.

‘그런 의미에서 화산파가 이 일에 신경을 많이 쓰고 있는 건 확실하고.’

화산일학 백무성.

혁무진이 떠들어 댄 것들이 사실이라면 그는 자타가 인정하는 화산파 차기 장문인이나 다름없다.

그나마 화산파의 후기지수 중 그에 견줄 만한 유일한 상대가 있긴 한데…….

“은인, 저 진짜 배고파요. 혹시 만두 남은 거 없어요?”

“네. 없는데요.”

“앗. 아아아…….”

청풍은 안 될 거야, 아마.

저 인간이 화산파 장문인이 되는 것보다 화산파 도사들이 이슬람교로 개종하는 게 더 빠를 거다.

제삼자인 내 눈에도 뭐 이런 놈이 있나 싶은데 화산파 사람들이 보면 오죽할까.

‘나중에 세상의 모든 일을 경험하고 나면, 그때가 돼서야 화산파 장문인도 해 보고 싶다고 할 놈이지. 음.’

내가 상당히 신빙성 있는 미래를 상상하고 있을 때, 철우가 짜증 난 얼굴로 입을 열었다.

“거, 만두 못 먹어서 죽은 귀신이라도 붙었소? 제발 입 좀 다물고 갑시다.”

“……?”

“……?”

“……?”

순간 나와 위팽, 혁무진의 시선을 한 몸에 받은 철우가 흠칫 놀랐다.

“뭐, 뭔데? 갑자기 왜 그런 눈으로 쳐다보는 거요?”

“야, 너 혹시.”

“철 소협, 모르시오?”

“에이, 설마요. 명색이 매화삼절이신데 그걸 모르실 리가.”

줄줄이 이어지는 반응에 철우가 황소 같은 눈을 뒤룩뒤룩 굴렸다.

“뭐야? 왜 이러는 건데?”

왜 이러긴, 사문의 어르신도 못 알아보니 이러지.

항렬로 따졌을 때, 청풍은 검성의 제자이자 현 화산파 장문인인 천검진인의 막내 사제가 된다.

철우에게는 스승님의 사제, 즉 사숙(師叔)인 셈이다.

‘아, 생각해 보니 모를 수도 있겠네.’

청풍은 검성 매종학이 은거 중에 키운 제자다. 문파 내부에서도 극소수만이 그의 얼굴과 정체를 알고 있을 게 분명했다.

나는 사숙을 눈앞에 두고도 못 알아보는 철우를 보며 혀를 찼다.

“쯧쯧. 등잔 밑이 어둡다더니.”

“그러니까 그게 무슨 소리냐고.”

“아냐, 잠시 후면 알게 되겠지.”

“이런 니기미, 환장하겠네.”

철우가 답답함에 가슴을 칠 때, 우리는 군중들의 환호를 뒤로하고 태원진가의 정문으로 들어섰다.

동시에 사방에서 백여 쌍의 시선과 수군거림이 날아들었다. 문밖과는 사뭇 다른 분위기다.

“저 청년이…….”

“산서잠룡이군요. 듣던 대로 영준합니다.”

“패화권도 있군. 천검진인의 둘째 제자라지?”

“그런데 옆에 있는 두 청년은 누굽니까?”

“글쎄올시다.”

남녀노소의 구분 없이 섞여 있는 백여 명의 사람들. 옷차림과 태도에서 그들이 가진 부와 여유가 묻어 나온다.

‘산서성의 실력자들.’

그들 중에는 일문(一門)의 문주들도 있고, 상계(商界)의 부호들도 있다. 이번 회합에 정식으로 초청받을 만큼의 세력과 능력이 있는 자들이었다.

‘얼핏 보면 귀족들의 무도회 같기도 하고.’

나는 묘한 기분에 휩싸여 걸음을 옮겼다.

산서성의 지배층이라 할 수 있는 저들이 이 회합의 조연에 불과하다는 사실에, 그리고 저들이 보내는 호기심과 선망 어린 시선에 마음 한구석이 간질거렸다.

그리고 다음 순간이었다.

“하곡문(河曲門)이라는 자그마한 문파를 이끌고 있는 장세팔이라고 하오.”

“아, 네. 안녕하세요.”

“다름이 아니라, 평소 태원진가와 산서잠룡의 명성을 마음 깊이 흠모하고 있었는데…….”

이렇게 만나게 되어 영광이라는 말을 장황하게 늘어놓는 중년 무인을 시작으로 사람들이 좀비 떼처럼 몰려들기 시작했다.

“안녕하십니까. 소인은 양천 근처에서 작은 무관을 운영 중인…….”

“예? 아, 예.”

“진 소협. 내 긴히 할 말이 있는데 자리를 옮기는 것이…….”

“지금이요? 그건 좀.”

“이 아이는 내 여식이오. 산서잠룡을 꼭 한번 보고 싶다기에 데려왔는데 혹시 마음에 든다면…….”

“예, 예.”

“오오, 그럼 바로 매파를 보내면 되겠소?”

“잠깐, 잠깐만요! 잘못 대답했어요!”

이게 도대체 무슨 일이래.

사방에서 쏟아지는 악수의 요청, 아니 포권 세례에 혼이 쏙 빠질 지경이다.

때마침 위팽이 나서지 않았다면 온갖 미사여구가 들어간 청탁과 혼례 요청을 죄다 수락해야 했을 것이다.

“모두 자중하시오!”

공력이 실린 절정 고수의 외침에 사람들이 움찔한 틈을 타 자리를 빠져나왔다. 철우가 질렸다는 듯이 혀를 내두른다.

“극성이군. 산서성 사람들은 죄다 저런가?”

그럴 리가 있냐. 이번 경우가 좀 특수한 거지.

일행 중 당황하지 않은 사람은 위팽뿐이었다. 그가 덤덤한 표정으로 입을 열었다.

“앞으로 자주 겪을 일이니 차차 익숙해져야 할 겁니다.”

“오늘 같은 일을 자주 겪어야 한다고요?”

“삼공자는 태원진가의 직계니까요.”

“방금 혼인만 다섯 번 치를 뻔했어요.”

“반려자가 없는 전도유망한 후기지수에게는 당연한 일이죠.”

“아까 들어 보니 저랑 태중 혼약을 맺었다는 사람도 있던데…… 그거 사실입니까?”

“사실이면 어떻고 거짓이면 어떻습니까? 좋게 생각하십시오.”

머리털이 쭈뼛 선다. 현실에서 27년간 모태 솔로로 살았는데 난데없이 중매로 결혼하는 게 아닌가 싶어서다.

그것도 만리타향인 무림에서.

‘안 돼. 나한테는 송이 씨가 있어.’

나는 목에 핏대까지 세우며 외쳤다.

“아니, 혼인이 얼마나 중요한 일인데 그걸 그렇게 넘어가면 안 되죠! 남녀 간의 사랑! 순수한 감정! 저한테는 그런 것도 없어요?”

“예. 없습니다.”

“왜! 어째서!”

위팽이 벌레를 보는 듯한 눈빛으로 나를 훑었다.

“그게 열여섯 살 때부터 기루에 들락거린 사람이 할 소립니까? 은자 뿌리면서 양심도 같이 뿌렸어요?”

“…….”

“조용히 갑시다. 주군께서 기다리고 계십니다.”

차라리 가 봤으면 억울하지나 않지.

기루는 시발, 헌팅 술집도 못 가 봤는데.

말도 못 하고 내심 피눈물만 흘리는 내게 철우가 슬쩍 물었다.

“사실이냐?”

“뭐가.”

“열여섯 살 때부터 기루 간 거.”

“알 거 없어. 그리고 갑자기 그딴 건 왜 물어봐?”

순간 흠칫한 철우가 횡설수설했다.

“그, 뭐랄까. 개인적인 호기심이랄까. 우직하게 무인의 길만을 걸어온 한 사내의…….”

“기루에 가 보고 싶다고?”

“커흐흠!”

“……무인의 길이나 마저 걸어라. 괜히 샛길로 빠지지 말고.”

한심한 감정을 가득 담아 대답한 그때였다.

“진 소협의 말씀이 백번 옳다. 본산에서 내려온 지 얼마나 되었다고 벌써부터 무인의 본분을 잊은 것이냐?”

엄하면서도 웃음기가 담긴 말투.

낯선 목소리의 주인공은 말끔한 인상의 사내였다. 흔들림 없는 걸음으로 다가온 그가 공손히 포권을 취했다.

그 대상은 나도, 위팽도 아니었다.

“화산파 일대제자 백무성이 사숙을 뵙습니다.”

잠깐 침묵하던 청풍이 대답했다.

“누구세요?”



* * *



환갑쯤 되었을까?

호리호리한 키에 쭉 째진 눈매가 인상적인 노인이었다.

거스러미가 돋아난 입술 사이에서는 잔뜩 쉰 목소리가 흘러나왔다.

“그래서 이름도 없는 무명 소졸에게 개망신을 당했다?”

“자, 장로님. 그것이 아니오라…….”

노인의 앞에 선 세 명의 사내는 땀을 뻘뻘 흘렸다.

종남삼수(終南三手)라 불리는 그들이지만 사문의 존장 앞에서는 말 한마디, 행동거지 하나하나에 주의를 기울여야 한다.

그 상대가 종남파에서 다섯 손가락 안에 꼽히는 고수이자 불같은 성격으로 유명한 노호검객(怒號劍客)이라면 더더욱.

“그럼 무엇이냐? 아무리 들어도 노부의 귀에는 네놈들이 대 종남파의 이름에 똥칠했다는 소리로 들리는데.”

날카로운 눈빛에 종남삼수가 몸을 부르르 떨었다.

노호검객의 불호령이 떨어지려던 찰나, 시종일관 입을 꾹 다물고 있던 한 사내가 불쑥 입을 열었다.

“무명 소졸이 아니었습니다.”

“뭐라?”

팔에 부목을 댄 사내, 공일혁이 말을 이었다.

“검성의 제자라고 했습니다.”

어찌나 충격적인 말이었는지, 잠시 말을 잊고 있던 노호검객이 믿기지 않는 표정으로 되물었다.

“……검성?”

“예.”

“오래전부터 은거 중이던 검성이 제자를 키웠다고?”

“처음에는 저희도 의심했습니다만…… 사실인 것 같습니다.”

“근거는?”

“화산파의 속자제자인 이풍이 산서성 군문에 몸담고 있습니다. 놈의 반응으로 보아 확실한 듯합니다.”

“이풍?”

안 그래도 주름진 미간이 찌푸려진다.

화산파의 속가제자 따위를 기억할 정도로 그의 기억력은 뛰어나지 못했다.

“그게 전부더냐?”

뜨뜻미지근한 반응에 공일혁이 황급히 입을 열었다.

“약관의 나이에 화산파의 진산절학을 절정까지 익힌 놈입니다. 본산의 적전 제자들에게만 허락된 무공들을 줄줄이 펼쳐 내는데…….”

잠시 후, 당시 상황을 전부 전해 들은 노호검객은 말없이 검갑을 문질렀다.

‘검성의 제자라, 검성의 제자.’

검성이 은거한 지 이미 수십 년이다.

살았는지, 죽었는지도 잘 알려지지 않은 그의 제자가 갑자기 무림에 나오다니?

믿기 힘든 사실이었지만 마음은 이미 기운 후였다.

‘적어도 확인 정도는 해 봐야겠지.’

한참 동안이나 침묵하던 노호검객은 자리를 박차고 일어났다. 화들짝 놀란 종남삼수에게 명령이 떨어졌다.

“안내해라.”

“어, 어디로 말입니까?”

“혹시 검성의 제자…….”

당황하는 두 사람과는 달리 공일혁의 눈이 번쩍 빛났다.

“제자가 알기로, 놈은 태원진가의 자제와 동행중입니다.”

“태원진가의 자제라면, 아까 네가 말한 그 진태경인가 하는 놈이냐?”

“예. 이곳에서 한나절 거리지요.”

노호검객이 혀를 찼다.

“영악한 놈. 네가 노부를 찾아온 이유도 그것이겠지.”

“불민한 제자들로 인해 대 종남파의 이름이 땅에 떨어졌습니다. 장로님께서는 누구보다 본문을 아끼시는 분 아니십니까? 때마침 장로님께서 용무를 보러 근방에 와 계시다는 소식을 들어서…….”

“집어치워라. 어차피 네 얘기를 들어 보니 그 진태경인가 하는 놈도 여간 오만방자한 놈이 아니더군.”

“맞습니다. 그런 놈은 호되게 혼쭐을 내 줘야지요.”

공일혁이 막 생각났다는 듯이 덧붙였다.

“마침 태원진가에서 회합이 열리고 있다 합니다.”

“회합?”

“산서성의 모든 문파들을 초청해서 위세를 과시하는 자리지요.”

“본문을 깔아뭉개고 회합을 열어?”

노호검객의 눈에 노기가 서렸다.

“더 이상 들을 것도 없다. 앞장서라.”

“장로님의 명을 받듭니다.”

고개 숙인 공일혁의 입가에 득의양양한 미소가 걸려 있었다.
```

## Final English reading copy

```markdown
# Chapter 184

It looked like there were a thousand people, not hundreds. With the martial artists of the Jin Family of Taiyuan escorting us, we made our way through the enormous crowd.

*This feels amazing.*

I felt like a star in the Chinese-speaking world. The Korean Wave and all that.

Then again, I was actually Korean, so it wasn’t entirely wrong.

“Sleeping Dragon of Shanxi! Look this way just once!”

“Eeeek! Young Hero Jin!”

“Waaah!”

They say even a mutt has home-field advantage.

No matter how famous the Three Plum Blossom Elites were, they couldn’t beat the pride of Shanxi Province—the son of Taiyuan—on his home turf.

As I smiled warmly and waved, Chulwoo whispered to me.

“Look at the corners of your mouth. Enjoying this?”

“Look at the corners of yours. Are you crying?”

“You Shanxi bumpkin.”

“Yeah, next mountain man.”

“You little—”

“What, you—”

Just as sparks were about to fly again, a thread of Sound Transmission pierced my ear.

—Third Young Master!

Wipeng was glaring at me with a fierce expression. He looked like he wanted to slap me right then and there.

He must have sent a similar Sound Transmission to Chulwoo, because the man added a single word with a dissatisfied expression.

“I let you off.”

I answered with a derisive snort.

When I first realized from the people’s cheers that Chulwoo was a fairly prominent young prodigy of Huashan, I was rather surprised.

But that was all.

*So what if he’s one of the Three Plum Blossom Elites?*

I had already experienced enough of Huashan’s martial arts, thanks to a certain person plodding along beside me.

“I’m hungry. I’m hungry.”

“……”

Cheongpung was a strange fellow no matter how many times I saw him, but there was no denying that he was a Peak master who had mastered Huashan’s foundational secret arts.

Because of that, I was confident I could respond no matter what martial arts Chulwoo used. The only thing Chulwoo had over me was his background as a member of Huashan.

“……”

Ah, no. I take that back.

The difference in our backgrounds was pretty serious when I thought about it. No matter how much the Jin Family of Taiyuan had risen in status, the Nine Sects and One Gang were overwhelmingly powerful.

*Fuck. I lose.*

The Nine Sects and One Gang and the Five Great Families, as I saw them, were no different from a corporate alliance in Murim.

Powerful conglomerates had joined forces into one coalition and were ganging up on everyone else. There was no one who could stand against them.

Fortunately, they didn’t invade the alley markets despite calling themselves the orthodox faction, which was why small and medium-sized companies like the Jin Family of Taiyuan could still climb their way upward.

*In that sense, it’s obvious that Huashan is paying close attention to this matter.*

Huashan’s Lone Crane, Baek Museong.

If everything Hyuk Mujin had told me was true, Baek Museong was practically the next Sect Leader of Huashan—recognized as such by everyone, including himself.

There was one person among Huashan’s young prodigies who could be considered his only equal, though…

“Benefactor, I’m really hungry. Do you have any dumplings left?”

“No. I don’t.”

“Oh. Aaaah…”

Cheongpung was a lost cause.

It would probably be faster for Huashan’s Daoists to convert to Islam than for that guy to become the Sect Leader of Huashan.

Even I, an outsider, couldn’t help thinking, *What kind of person is this?* How much worse must it be for the people of Huashan?

*Once he’s experienced everything in the world, he’ll probably decide that he wants to try being the Sect Leader of Huashan too. Yeah.*

Just as I was imagining a fairly believable future, Chulwoo opened his mouth with an irritated expression.

“Hey, did a ghost of someone who died because he couldn’t eat dumplings latch onto you? Please shut your mouth and walk.”

“……?”

“……?”

“……?”

Chulwoo flinched when the gazes of Wipeng, Hyuk Mujin, and me all fell on him at once.

“W-What? Why are you looking at me like that all of a sudden?”

“Hey, you don’t happen to…”

“Young Hero Chul, you don’t know?”

“Come on, no way. You’re one of the Three Plum Blossom Elites. Surely you can’t not know.”

As the reactions came one after another, Chulwoo’s ox-like eyes rolled around.

“What? Why is everyone acting like this?”

Why else? Because he couldn’t recognize the elder of his own sect.

By seniority, Cheongpung was the Disciple of the Sword Saint and the youngest Junior Brother of the Heavenly Sword True Person, the current Sect Leader of Huashan.

To Chulwoo, that made him his Master’s Junior Brother—in other words, his Martial Uncle.

*Come to think of it, he might not know.*

Cheongpung had been raised by the Sword Saint, Mae Jonghak, while Mae Jonghak was living in seclusion. There was no doubt that only a handful of people within the sect knew what he looked like or who he really was.

I clicked my tongue as I looked at Chulwoo, who stood face-to-face with his Martial Uncle without recognizing him.

“Tsk, tsk. They say it’s darkest beneath the lamp.”

“What the hell does that mean?”

“Never mind. You’ll find out soon enough.”

“Damn it, this is driving me crazy.”

As Chulwoo pounded his chest in frustration, we left the cheers of the crowd behind and entered through the main gate of the Jin Family of Taiyuan.

At the same time, more than a hundred pairs of eyes and countless whispers flew toward us from every direction. The atmosphere was completely different from outside the gate.

“That young man…”

“That’s the Sleeping Dragon of Shanxi. He’s as handsome as I’d heard.”

“The Defeated Flower Fist is here too. Isn’t he the second Disciple of the Heavenly Sword True Person?”

“Then who are the two young men beside them?”

“I couldn’t tell you.”

More than a hundred people of all ages, both men and women, were mingling together. Their wealth and leisure were evident in their clothes and manner.

*The power players of Shanxi Province.*

Some of them were Sect Leaders, while others were wealthy merchants. They had enough influence and ability to be formally invited to this gathering.

*At a glance, it almost looks like a ball for aristocrats.*

I walked on, swept up in a strange feeling.

The fact that these people, who could be considered Shanxi Province’s ruling class, were no more than supporting characters at this gathering—and the curious, admiring gazes they sent my way—made one corner of my heart itch.

And then it happened.

“My name is Jang Se-pal. I lead a small sect called the Hequ Sect.”

“Ah, yes. Hello.”

“I’ve long admired the reputation of the Jin Family of Taiyuan and the Sleeping Dragon of Shanxi from the bottom of my heart, and…”

A middle-aged martial artist began an elaborate speech about how honored he was to meet me. Then people started surging toward us like a horde of zombies.

“Greetings. I run a small martial arts academy near Yangcheon…”

“Pardon me? Oh, yes.”

“Young Hero Jin, I have something important to discuss with you. Perhaps we could move somewhere else…”

“Right now? I’d rather not.”

“This is my daughter. She wanted to meet the Sleeping Dragon of Shanxi at least once, so I brought her along. If you happen to find her appealing…”

“Yes, yes.”

“Oh! Then shall I send a matchmaker right away?”

“Wait, wait! I answered that wrong!”

What on earth was going on?

Requests for handshakes—or rather, a barrage of fist-and-palm salutes—were pouring in from every direction. I was on the verge of losing my mind.

If Wipeng hadn’t stepped forward at just the right moment, I would have ended up accepting every request and marriage proposal wrapped in flowery language.

“Everyone, restrain yourselves!”

The shout of a Peak master infused with internal energy made the people flinch, and we took the opportunity to escape. Chulwoo clicked his tongue as though he’d had enough.

“That was excessive. Are all the people of Shanxi like that?”

Of course not. This situation was a bit unusual.

Wipeng was the only member of our group who hadn’t been flustered. He opened his mouth with a calm expression.

“You’ll experience this often from now on, so you’ll have to get used to it.”

“I’m supposed to experience things like this often?”

“You’re a direct descendant of the Jin Family of Taiyuan, after all.”

“I almost got married five times just now.”

“That’s only natural for a promising young prodigy without a partner.”

“I heard someone say they were betrothed to me before I was even born… Is that true?”

“What difference does it make whether it’s true or false? Think positively.”

The hair on my body stood on end.

I had spent twenty-seven years of my life as a lifelong single in the modern world, and now I was suddenly worried that I might be forced into an arranged marriage.

In Murim, thousands of miles from home, no less.

*No. I have Song-i.*

Veins bulging in my neck, I shouted,

“Marriage is an incredibly important matter! You can’t just brush it aside like that! Love between a man and a woman! Pure feelings! Don’t I get any of that?”

“No. You don’t.”

“Why?! How come?!”

Wipeng looked me up and down as though he were looking at an insect.

“Is that something a man who’s been going in and out of pleasure houses since he was sixteen should say? Did you throw away your conscience along with your silver nyang?”

“……”

“Let’s walk quietly. Our Lord is waiting.”

If I’d actually been to one, at least I wouldn’t feel so wronged.

Fuck, I’d never even been to a pickup bar, let alone a pleasure house.

As I said nothing and shed silent tears of blood inside, Chulwoo sidled up and asked,

“Is that true?”

“What is?”

“That you’ve been going to pleasure houses since you were sixteen.”

“You don’t need to know. Why are you suddenly asking about that?”

Chulwoo flinched and began to ramble.

“Well, how should I put it? I suppose you could call it personal curiosity. About a man who has walked only the straight path of a martial artist…”

“You want to visit a pleasure house?”

“Ahem!”

“Finish walking the path of a martial artist. Don’t go wandering down side paths for no reason.”

I replied with utter disdain. That was when a voice cut in.

“Young Hero Jin is absolutely right. How long has it been since you left the main sect, and you’ve already forgotten the duty of a martial artist?”

The tone was stern, yet carried a hint of amusement.

The owner of the unfamiliar voice was a clean-cut man. He approached with an unwavering stride and respectfully made a fist-and-palm salute.

But he wasn’t addressing me or Wipeng.

“Baek Museong, First-generation Disciple of Huashan, pays his respects to his Martial Uncle.”

Cheongpung was silent for a moment before answering.

“Who are you?”

* * *

Around sixty, perhaps?

He was an old man with a slender frame and strikingly narrow eyes.

A deeply hoarse voice came through his chapped lips.

“So you were humiliated by an unknown nobody with no name?”

“E-Elder, that’s not what happened…”

The three men standing before the old man were sweating profusely.

They were known as the Three Hands of Zhongnan, but before an elder of their sect, they had to watch every word they spoke and every movement they made.

Even more so when that elder was the Roaring Fury Swordsman—a master counted among the top five in the Zhongnan Sect and a man famous for his fiery temper.

“Then what is it? No matter how I listen, it sounds to these old ears as though you idiots smeared shit all over the name of the great Zhongnan Sect.”

The Three Hands of Zhongnan trembled beneath the old man’s sharp gaze.

Just as the Roaring Fury Swordsman was about to unleash his thunderous reprimand, one of the men, who had kept his mouth tightly shut the entire time, suddenly spoke.

“He wasn’t an unknown nobody.”

“What?”

The man with a splint on his arm, Gong Ilhyuk, continued.

“He said he was the Sword Saint’s Disciple.”

The statement was so shocking that the Roaring Fury Swordsman momentarily forgot how to speak. Then he asked with an expression of disbelief,

“…The Sword Saint?”

“Yes.”

“The Sword Saint, who has been living in seclusion for so long, raised a Disciple?”

“We suspected it at first, but… it seems to be true.”

“Your evidence?”

“Li Feng, a lay Disciple of Huashan, serves in the military of Shanxi Province. Judging by his reaction, it seems certain.”

“Li Feng?”

The old man’s already furrowed brow creased further.

His memory wasn’t good enough to remember some lay Disciple of Huashan.

“Is that all?”

At the lukewarm reaction, Gong Ilhyuk hurriedly spoke again.

“He mastered Huashan’s foundational secret arts to the Peak realm despite being only twenty. He used martial arts that are permitted only to the direct Disciples of the main sect, one after another…”

After hearing the entire account of what had happened, the Roaring Fury Swordsman silently rubbed his sword scabbard.

*The Sword Saint’s Disciple. The Sword Saint’s Disciple.*

The Sword Saint had already been living in seclusion for decades.

No one even knew whether he was alive or dead, and now his Disciple had suddenly appeared in Murim?

It was difficult to believe, but his mind had already begun to lean toward accepting it.

*At the very least, I should verify it.*

After remaining silent for a long while, the Roaring Fury Swordsman abruptly rose from his seat. An order fell on the startled Three Hands of Zhongnan.

“Guide me.”

“W-Where do you mean?”

“Could you mean the Sword Saint’s Disciple…?”

While the other two men stood there flustered, Gong Ilhyuk’s eyes flashed.

“As far as I know, that bastard is traveling with a scion of the Jin Family of Taiyuan.”

“If you mean a scion of the Jin Family of Taiyuan, are you talking about that Jin Taekyung fellow you mentioned earlier?”

“Yes. He’s half a day from here.”

The Roaring Fury Swordsman clicked his tongue.

“Cunning bastard. That must be why you came looking for this old man.”

“The name of the great Zhongnan Sect has fallen into the dirt because of these inept Disciples. Elder, aren’t you the person who cares about our sect more than anyone? I happened to hear that you were in the area on business, so…”

“Cut it out. From what you’ve told me, this Jin Taekyung fellow sounds like an incredibly arrogant bastard too.”

“That’s right. A bastard like that needs to be taught a harsh lesson.”

Gong Ilhyuk added, as though he had just remembered something,

“I hear the Jin Family of Taiyuan is holding a gathering.”

“A gathering?”

“They’ve invited every sect in Shanxi Province to show off their power.”

“They’re trampling on our sect and holding a gathering?”

Anger filled the Roaring Fury Swordsman’s eyes.

“I’ve heard enough. Lead the way.”

“I obey, Elder.”

A smug smile spread across Gong Ilhyuk’s lips.
```
