<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0181.txt",
      "sha256": "38a77a067f9a7846f2ac7f6b9b3022238213b9b606615fc272de32db17cc379d",
      "bytes": 15361
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "43c2b327e11e39ac42bdf83b8bfc9bb28353d961ea2f97baf9095b16cf664442",
      "bytes": 1772
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "07f727ce9637d25bace9edcae3161d49624c5ad6f6f4778b69f30b67f6b79945",
      "bytes": 45286
    },
    {
      "path": "characters/Baek Museong.md",
      "sha256": "ad153d50d8cd5ee1f28d3fbcd525521cae34e48b302db354bc0e6c879d2e5833",
      "bytes": 668
    },
    {
      "path": "characters/Cheongpung.md",
      "sha256": "6bbf3c5526220f3e1ffb211294b6fe2cbc7685288735ea0dc1cfa096e209f8a9",
      "bytes": 1755
    },
    {
      "path": "characters/Chulwoo.md",
      "sha256": "dd3486e727707b8d484051214ac3e9a48806bab9ff19408c941be09b21075ede",
      "bytes": 643
    },
    {
      "path": "characters/Eunhyang.md",
      "sha256": "972d941bb643365893d119978c61fb071e243e963f8aa27ec80311886f10d5eb",
      "bytes": 690
    },
    {
      "path": "characters/Hyuk Mujin.md",
      "sha256": "219ee4755097db618cb1b7692a8a92b6832ee272bdc54462a3efe4a27aa4a6c4",
      "bytes": 5558
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "f87e18f13b5ff7a4873a9a3480c2d4d63db869030f097e26630b8e93ae02e1f8",
      "bytes": 2055
    },
    {
      "path": "characters/Jin Wikyung.md",
      "sha256": "49df4636a28fd701c5c75202dbae947d67d595558c7d8a4afffea39bb4507acf",
      "bytes": 8199
    },
    {
      "path": "characters/Woo Hwangtae.md",
      "sha256": "50d5f97246a1d36969de9a096357e8ea70b086b65255e5834e85d087fa805213",
      "bytes": 657
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "096e2c481d9b9ae56498bb30f14947b3ed145f9037bbafa0ff3b1b505861f5f5",
      "bytes": 35987
    }
  ],
  "estimated_tokens": 32105
}
-->

# Durable State Update — Chapter 181

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 181. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 20 concise items, `open_questions` to at most 8
items, and `temporary_decisions` to at most 8 items. Keep the serialized context
under 16384 UTF-8 bytes. Use only chapter
numbers through 181. `profile_updates` may replace one exact, uniquely occurring
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
  "chapter": 181,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 181,
    "continuity_sources": [181],
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
    "The Heavenly Wind Band was annihilated near Datong by an unknown Supreme Peak master; Jin Wikyung privately suspects Mae Jonghak.",
    "Jin Taekyung is absent while having a weapon forged and has stopped sending news; Jin Mukyung is undergoing seclusion training after enlightenment.",
    "Woo Hwangtae is seeking an audience and apology regarding Woo Jintae after the Jin Family rejected his requests for five days.",
    "Baek Museong and the Huashan group are present at the Jin Family's gates.",
    "The Treasured Jade remains missing.",
    "Jang Taebo is forging Taekyung's commissioned weapon."
  ],
  "continuity_sources": [
    180
  ],
  "open_questions": [
    "Who annihilated the Heavenly Wind Band near Datong?",
    "What consequences will follow Taekyung's absence from the Jin Family's grand banquet?",
    "When will Jang Taebo complete Taekyung's weapon?",
    "Who has the Treasured Jade, or was it lost by Jopil?"
  ],
  "safe_through": 180,
  "temporary_decisions": [
    "Render 원단 as “New Year's Day.”",
    "Retain 천풍단 as “Heavenly Wind Band.”",
    "Retain 천검진인 as “Heavenly Sword True Person.”",
    "Retain 매화삼절 as “Three Plum Blossom Elites.”",
    "Render 수문각 as “Gate Guard Pavilion.”",
    "Render 장주 as “Lord.”"
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

## Exact glossary matches

| 무림     | **Murim**          |
| 진위경    | **Jin Wikyung**    |
| 혁무진    | **Hyuk Mujin**     |
| 적천강    | **Jeok Cheongang** |
| 백무성    | **Baek Museong**   |
| 철우     | **Chulwoo**        |
| 은향     | **Eunhyang**       |
| 청풍     | **Cheongpung**     |
| 산서잠룡   | **Sleeping Dragon of Shanxi** | Jin Taekyung   |
| 진천검    | **Heaven Shaking Sword**      | Jin Mukyung    |
| 화왕     | **Fire King**                 | Jeok Cheongang |
| 태원진가   | **Jin Family of Taiyuan**        |
| 열화문    | **Fire Gate Clan**               |
| 화산파    | **Huashan**                      |
| 소림     | **Shaolin**                      |
| 산서오문   | **Five Gates of Shanxi**         |
| 십봉룡    | **Ten Dragons and Phoenixes**    |
| 일류     | **First Rate**    |
| 절정     | **Peak**          |
| 무인     | **martial artist**                               | Default term                                          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 비급     | **martial arts manual**                          | “martial scroll” where object/context warrants        |
| 전음     | **Sound Transmission**                           | Fixed skill terminology; preserve the internal-energy mechanism when the source explains it, but do not add an explanation where it does not |
| 문주     | **Sect Leader**                              |
| 표국     | **Escort Bureau**                            |
| 사부     | **Master**                                   |
| 제자     | **Disciple**                                 |
| 사형     | **Senior Brother**                           |
| 사제     | **Junior Brother**                           |
| 은인     | **Benefactor**                               |
| 산서     | **Shanxi**             |
| 태원     | **Taiyuan**            |
| 화산     | **Huashan**            |
| 귀가      | **your family**                                                 |
| 대사      | **Master** for a senior Buddhist monk                           |
| 우황태 | **Woo Hwangtae** | Chief of the Seongun Escort Bureau and Woo Jintae's father. |
| 화염신장 | **Flame Divine Palm** | Jopil's deadly palm technique, noted when Taekyung compares Jopil with Mukyung. |
| 사마외도 | **demonic, heterodox arts** | Suspected martial-arts origin of Pung Yang's insidious forms. |
| 열화신단 | **Blazing Flame Divine Pill** | Dangerous elixir that grants half a jiazi of internal energy while risking death from its fire qi. |
| 산서성 | **Shanxi Province** | Province containing the Lower District Sect branches. |
| 조장 | **Captain** | Hyuk Mujin's address for Taekyung as squad leader. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 시진 | **shichen** | Traditional time unit of approximately two hours. |
| 매화삼절 | **Three Plum Blossom Elites** | Collective title for the current Sect Leader’s three exceptional disciples. |

## Listed compact profiles

### Baek Museong.md

# Baek Museong (백무성)

- **Safe through:** Chapter 180
- **Aliases:** Huashan’s Lone Crane
- **Role:** First-generation disciple of Huashan, first of the Three Plum Blossom Elites, and leader of the journey to meet Cheongpung.
- **Personality:** Calm, responsible, principled, and patient, though visibly weary of his junior disciples’ antics.
- **Voice:** Gentle and polite with strangers; measured and stern when correcting junior disciples.
- **Relationships:** The current Huashan Sect Leader is his Master; Chulwoo and Eunhyang are his junior disciples; he met Cheongpung ten years ago.

### Cheongpung.md

# Cheongpung (청풍)

- **Safe through:** Chapter 180
- **Aliases:** None
- **Role:** Mysterious young man encountered at Honghwa Inn; an exceptionally young Peak master whose Level Jin Taekyung cannot determine through Qi Sense; the grandson and disciple of Sword Saint Mae Jonghak, who secretly descended from Huashan to seek out and defeat the Ten Dragons and Phoenixes, beginning with Jin Mukyung; he has no martial title yet, naturally opened his Governor Vessel through enlightenment two years ago, has begun teaching Jin Taekyung and Hyuk Mujin using Mae Jonghak's training method, has now used Sword Energy and the Zaha Divine Technique during his spar with Taekyung, defended Taekyung from Jeok Cheongang with Huashan martial arts, and Prince Shangshan will only accept his autograph after he gains one
- **Personality:** Affable, dreamy, hazy, and childlike in manner, with innocent curiosity, delight in novel public attention, a deep love of martial arts, and a martial artist's competitive pride; he becomes unsettled when someone copies his martial arts
- **Voice:** Dreamy and hazy, with innocent, polite phrasing
- **Relationships:** Mae Jonghak, the Sword Saint, is his grandfather and martial instructor; Cheongpung came to Huashan at about age three or four rather than being born there, lived with Mae Jonghak at a hidden residence, and secretly left Huashan without his grandfather's knowledge to challenge the Ten Dragons and Phoenixes; Baek Museong met him ten years ago and is now traveling with the Three Plum Blossom Elites to meet him; Li Feng is his Martial Nephew within Huashan's hierarchy; calls Jin Taekyung and Hyuk Mujin Benefactors after they feed him

### Chulwoo.md

# Chulwoo (철우)

- **Safe through:** Chapter 149
- **Aliases:** None
- **Role:** Enormous Huashan martial artist, junior disciple of Baek Museong, and member of the Three Plum Blossom Elites.
- **Personality:** Blunt, defensive, physically intimidating, short-sighted, and unconcerned with personal cleanliness.
- **Voice:** Hearty, casual, and blunt, with indignant protests when accused of wrongdoing.
- **Relationships:** Baek Museong is his Senior Brother; Eunhyang is his fellow junior disciple and frequent bickering partner; he serves under Huashan’s Sect Leader.

### Eunhyang.md

# Eunhyang (은향)

- **Safe through:** Chapter 149
- **Aliases:** None
- **Role:** Young female Huashan martial artist, junior disciple of Baek Museong, and member of the Three Plum Blossom Elites.
- **Personality:** Bright, mischievous, playful, sharp-tongued, and willing to justify questionable actions with confident moral reasoning.
- **Voice:** Lively and teasing, with familiar phrasing and a sweet laugh; she prefers calling Baek Museong Big Brother.
- **Relationships:** Baek Museong is her Senior Brother; Chulwoo is her fellow junior disciple and bickering companion; she serves under Huashan’s Sect Leader.

### Hyuk Mujin.md

# Hyuk Mujin (혁무진)

- **Safe through:** Chapter 179
- **Aliases:** None revealed
- **Role:** Level 50 First Rate martial artist from a wealthy Taiyuan textile-merchant family; Captain of the Gatekeepers at the Jin Family of Taiyuan; deputy squad leader of White Tiger Hall’s reconnaissance squad; candidate to become the next Master of the Gatekeeper Pavilion; has accepted Jin Taekyung’s invitation to train alongside Taekyung and Cheongpung in Taekyung’s private training ground
- **Personality:** Young, disciplined, persistent, and possessed of clear martial talent; suspicious of Jin Taekyung, and openly contemptuous of the family’s disgraced third son; believes loyalty and respectable conduct matter, but is also proud, hungry for glory, and an avid wuxia-novel reader who sometimes mistakes fictional Murim conventions for reality
- **Voice:** Formal and clipped when performing his duties; blunt and moralizing when addressing Taekyung
- **Relationships:** Gatekeeper under the Jin Family; deputy subordinate to Jin Taekyung in the reconnaissance squad; son of the Hyuk Family Textile Shop’s owners, with a younger sibling who removed the need for him to inherit the family business

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 179
- **Aliases:** Fire King
- **Role:** Nearly one-hundred-year-old wandering martial master and the Fire King; he visits Jang Taebo’s home, can detect Qi Sense, can cross more than ten jang in an instant, plans to reach Taiyuan and visit the Lower District Sect while concealing his identity, and once fought Sword Saint Mae Jonghak for seven days and seven nights to a draw at Mount Jiuhua before emerging from seclusion and annihilating one thousand Demonic Cultists there; after striking Jin Taekyung with the Flame Divine Palm, he deduces that Taekyung took the Blazing Flame Divine Pill and confronts him when he tries to flee the inn.
- **Personality:** Secretive, cryptic, sharp-eyed, amused by unusual young martial artists, and casually violent when dissatisfied with an answer.
- **Voice:** Sharp and ringing when calling out, then gruff, dryly teasing, and threatening during interrogation.
- **Relationships:** Visits Jang Taebo and tells him to check on the worried child living nearby; regards Jin Taekyung as an interesting fellow after detecting Qi Sense and interrogates him about the System; fought Mae Jonghak more than forty years ago and was close enough to be considered his kindred spirit; recognizes Cheongpung as Mae’s grandson and calls him a dependable grandson and Mae’s successor; rescued an orphan named Jangcheon during an Anhui epidemic, eventually accepted him as his Disciple, and later learned that Jangcheon became Jopil; regards Jangcheon as an only son and grandson despite their lack of blood relation, secretly followed him for four months after learning of his murders, confronted him in a red-light district, and could not bring himself to kill him before Jangcheon held a vial of Bone-Melting Powder between his lips and declared his departure; after learning that Taekyung killed Jopil, acknowledges a debt to Taekyung and apologizes to him and the others for his rash actions.

### Jin Wikyung.md

# Jin Wikyung (진위경)

- **Safe through:** Chapter 180
- **Aliases:** Junzi Sword
- **Role:** Thirty-five-year-old Lesser Family Head and future Family Head of the Jin Family of Taiyuan; has led the family in place of the absent Family Head for two years and established it as Shanxi Murim's hegemon
- **Personality:** Calm and authoritative in public; affectionate and protective toward Taekyung beneath a stern mask; accepts responsibility from his subordinates and shows immediate concern for family
- **Voice:** Restrained, formal, and commanding with subordinates; openly affectionate with Taekyung
- **Relationships:** Taekyung’s eldest brother and future Family Head; head of Wipeng; member of the Jin Family

### Woo Hwangtae.md

# Woo Hwangtae (우황태)

- **Safe through:** Chapter 180
- **Aliases:** None
- **Role:** Chief of the Seongun Escort Bureau and father of Woo Jintae; arrives at the Jin Family of Taiyuan seeking an audience and apology for his son's humiliation.
- **Personality:** Proud, status-conscious, volatile, and deeply angered by perceived disrespect toward his family.
- **Voice:** Blunt and sharp under pressure, becoming explosive when his wounded pride is provoked.
- **Relationships:** Father of Woo Jintae; chief of the Seongun Escort Bureau; one of the heads of the Five Gates of Shanxi.

## Korean source

```text
＃181화



“너는 잠시라도 눈을 뗐다 하면 사고를 치는구나.”

가볍게 사제를 꾸짖은 백무성이 우황태를 향해 고개를 숙여 보였다.

“서로 간에 사소한 오해가 있었던 것 같습니다. 넓은 아량으로 용서하시지요.”

인상만큼이나 부드러운 목소리였다.

우황태는 무인이라기보다는 장사치에 가까웠다. 무공은 일류지만 표국을 운영해 오며 길러 낸 눈썰미만큼은 절정이라고 자부할 수 있을 만큼.

아마 평소였다면 백무성을 본 순간 이런 생각을 했을지도 모른다.

‘평범 속의 비범.’

그러나 불행히도 지금의 우황태는 제정신이 아니었다.

난데없이 끼어든 백무성의 멀끔한 인상은 만만해 보였고 공손하면서도 강자의 여유가 묻어 나오는 목소리는 건방지게만 들렸다.

“뭐라, 넓은 아량으로 용서?”

부글거리는 목소리로 뇌까린 그가 눈썹을 치켜떴다.

“감히 누구한테 이래라저래라 하는 것이냐?”

“그런 의도로 드린 말씀은 아닙니다만, 마음이 상하셨다면 사과드리지요.”

“사과? 허, 이 하룻강아지 같은 놈이 그래도.”

까드득.

본래 한 번 분노에 사로잡히면 사고가 흐려지기 마련.

주먹을 말아 쥐며 나서는 우황태를 다른 문주들이 황급히 만류했다.

“우 국주, 이쯤에서 그만하는 것이 좋겠소.”

“송 문주의 말이 옳소이다. 괜히 소란 일으켜 봤자 좋을 게 뭐가 있겠소?”

“어디서 굴러먹다 왔는지 모를 놈들이 건방을 떠는데 참아라? 당신들도 나를 우습게 여기는 거요?”

“아니, 그 말이 아니라.”

“그럼 무슨 말이 하고 싶은 건가?”

이제는 반쯤 하대나 다름없는 말투. 산서오문의 문주들은 내심 눈살을 찌푸렸지만 괜한 분란은 막아야 했다.

“그저 시기와 장소가 틀렸다는 말이오. 우리 처지를 잊은 거요?”

“굳이 하겠다면 더 이상 말리지는 않겠소만…… 태원진가에 미운털이 박힌 이때 소란을 일으킬 필요는 없지.”

“화난 건 이해하지만 우리 입장도 생각해 주시구려. 다 같이 좀 살아 봅시다.”

또, 또. 그놈의 태원진가!

우황태는 순간 터져 나오려는 욕설을 가까스로 참았다. 주위에 수많은 눈과 귀가 없었다면 온갖 욕설을 퍼부으며 눈에 보이는 것들을 전부 때려 부쉈을 것이다.

하지만 마지막 한 줄기 이성이 그를 붙잡았다.

“끄으으응.”

간신히 마음을 진정시킨 우황태가 백무성을 노려보았다. 그는 여전히 침착한 표정으로 그 자리에 서 있었다.

“마음 같아서는 당장 단매에 때려죽여도 시원치 않지만…… 촌무지렁이의 실수라 생각하고 넘어가 주마. 꺼져라, 마음이 바뀌기 전에.”

물끄러미 그를 바라보던 백무성이 고개를 숙였다.

“사정을 봐주셔서 감사드립니다.”

“흥, 운 좋은 놈들.”

그러나 운이 좋은 것은 우황태였다.

백무성이 한발 앞서 전음을 날리지 않았더라면 그는 지금쯤 사경을 헤매고 있었을 테니까.

- 둘째, 멈춰라.

막 몸을 날리려던 매화삼절의 둘째, 패화권(敗華拳) 철우의 신형이 우뚝 멈췄다.

그의 잇새 사이로 다른 이에게 들리지 않는 음성이 새어 나왔다.

- 저로 모자라서 대사형까지 건드린 놈입니다.

- 상관없다.

- 전 상관있습니다. 한 대만, 딱 한 대만 때리면 안 됩니까?

- 때려죽이고 싶다는 말로 들리는구나.

- ……살살 때리겠습니다. 진짜 딱 한 대만요.

- 그건 살살 때려죽이겠다는 말이고. 괜한 시선을 끌지 말라는 사부님의 엄명을 잊었느냐?

갈등하던 철우가 꽉 움켜쥐고 있던 주먹을 늘어뜨렸다.

“후우, 미치겠네.”

백무성이 대견하다는 듯 어깨를 두드려 주었다.

“잘 참았다. 이 또한 수련이다.”

“이게 뭐가 수련입니까? 기껏 배워 놓은 무공도 제때 못 쓰는구먼.”

“무분별한 살생(殺生)은 너를 망칠 뿐이다. 무공은 정기신을 갈고 닦는 것이지, 누군가를 죽이기 위한 게 아니야.”

“사형을 볼 때마다 헷갈립니다. 제가 화산파 제자인지, 소림사 승려인지.”

“네 녀석 성격에 승려가 가당키나 하겠느냐? 앞으로 부숴 먹을 목탁만 불쌍하지.”

피식 웃는 백무성의 모습에 철우가 한숨을 내쉬었다.

마음 깊이 존경하는 사형이지만 너무 사람이 좋아서 문제다.

“저런 놈들은 아구창을 박살 내야 하는 건데…….”

“어허, 그 입!”

“알겠습니다. 알겠어요.”

철우는 어느새 훌쩍 멀어진 우황태의 뒷모습을 바라보며 입맛을 다셨다.

‘얼굴 기억해 뒀다. 한 번만 걸려라.’

그런 사제의 생각을 모를 리 없는 백무성이다. 그는 고개를 절레절레 내저었다.

“허튼 생각은 그만하고 막내부터 찾거라.”

“은향이 그 녀석 또 없어졌습니까?”

“그래, 너처럼 말이지.”

철우가 움찔했다.

“저, 저는 소피보러 간 겁니다.”

“그랬지. 그런데 소피보러 간다는 놈이 왜 사람 많은 곳에서 시비가 붙었느냐?”

“시원하게 비우고 오는 길에 그만. 아니 사형, 지금 저 못 믿으시는 겁니까? 아직 손 안 닦았는데 냄새 맡아 보실래요?”

“……됐다.”

백무성은 관자놀이를 문질렀다. 누구보다 아끼는 사제들이지만 다루기가 여간 까다로운 것이 아니었다.

그나마 철우는 덩치라도 커서 금방 찾지, 막내 사제인 은향은 이런 인파 속에서 보이지도 않는다.

“보이는 것 없느냐?”

남들보다 머리 두 개는 더 큰 철우가 주위를 쓱 훑었다.

“글쎄요. 사람이 워낙 많아서.”

끝도 없이 늘어선 북적이는 인파 속에서 자그마한 체구의 소녀를 찾는 건 절정 고수의 눈으로도 어렵다.

오죽 사람이 많으면 곳곳에 좌판을 깐 장사치들마저 보일 정도였다.

“그나저나 태원진가가 이 정도였습니까? 오기 전까지는 들어 본 적도 없는데.”

“아는 사람은 알지. 현 문주인 산서기협(山西奇俠)도 그렇고, 진천검(振天劍)도 제법 알려져 있지 않느냐?”

“산서기협은 잘 모르겠고 진천검이라면 십봉룡이니 뭐니 하는 그놈 말입니까?”

“그놈이라니. 입조심하거라.”

“학관이나 다니는 샌님인데요, 뭘. 제 생각엔 아마 대사형이 훨씬…….”

“어허. 보기도 전에 사람을 판단하는 고약한 버릇은 어디서 배웠느냐? 그는 분명 뛰어난 인재다.”

“뭐, 산서성에서 그 정도면 개천에서 용 난 것이나 다름없긴 합니다만.”

시큰둥하게 대꾸하던 철우가 문득 눈살을 찌푸렸다.

“그 왜, 진천검 말고도 무슨 용인지 미꾸라지인지, 한 명 더 있지 않습니까?”

“용? 산서잠룡을 말하는 것이냐?”

“아, 맞습니다. 산서잠룡.”

“진천검만큼은 아니지만 제법 뛰어난 기재라고 들었지.”

“용인지 미꾸라진지, 오는 길에 지긋지긋하게 들어서 얼굴이나 한번 봐야겠습니다.”

주먹을 불끈 움켜쥐는 철우를 본 백무성의 입꼬리가 슬쩍 올라갔다.

“겨뤄 보고 싶으냐?”

철우가 뒤통수를 긁적이며 대답했다.

“뭐, 꼭 그런 건 아닙니다. 어차피 제가 이길 건데.”

“호승심은 좋다만 분란은 가급적 피해야 한다.”

“분란 일으킬 거리나 있겠습니까? 기왕 나온 김에 실력이나 보자는 거지.”

백무성은 둘째 사제를 지그시 응시했다.

말과는 달리 제법 궁금한 기색이 역력하다.

철우의 성격에 몇 년째 화산에 틀어박혀 매일 같은 이들만 상대하다 보니 들뜬 모양이었다.

“금방 볼 수 있을 게다. 물론 그전에 막내를 찾아야겠지만.”

뒤에 덧붙인 말은 한숨에 가까웠다.

이미 태원진가의 문은 열렸고 초대받은 이들이 구름처럼 몰려간 상황이다.

그가 나무에라도 올라가야 하나 고민하던 그때였다.

“사형, 조금 시끄러운 건 괜찮지 않습니까?”

“뭐?”

씩 웃어 보인 철우가 크게 숨을 들이켰다.

그리고 다음 순간, 천둥 같은 외침이 터져 나왔다.

“은-향-아!!!”

미처 말릴 새도 없었다. 철우의 목청은 체구만큼이나 대단했다.

그들의 주위에 있던 사람들은 귀를 막으며 주저앉았고, 웃고 떠들던 수많은 사람이 입을 닫았다.

찬물이라도 끼얹은 듯 모두가 침묵한 그때였다.

“오라버니들! 나 여기!”

저 멀리, 제자리에서 열심히 깡충깡충 뛰고 있는 한 소녀를 발견한 철우가 의기양양하게 말했다.

“으하하! 사형, 찾았습니다!”

“……그래, 잘했다. 아주 잘했어.”

백무성이 머리를 짚은 그때였다.

쏴아아아.

마치 바람에 갈대밭이 갈라지듯 수백 명의 사람들이 웅성거리며 길을 텄다.

그리고 그 끝에 철탑처럼 서 있는 한 사내를 본 철우가 자신도 모르게 중얼거렸다.

“저게 사람이야, 곰이야.”

“사람이다. 그가 아니었다면 오늘의 태원진가도 없었겠지.”

곰 같은 사내, 진위경을 향해 백무성은 공손히 포권을 취했다.



* * *



두두두두!

풍경이 휙휙 스쳐 지나간다. 바로 옆에서 말을 몰고 있던 혁무진이 소리치듯 외쳤다.

“분명히 갈 때는 느렸는데, 돌아올 때는 엄청 빠르네요. 이틀 전에는 좀 느긋하게 가서 그런가?”

“모든 일에는 다 이유가 있지.”

“무슨 이유요?”

“누군가가 말을 타면서 뭔가를 처먹으려고 시도하지 않으면 돼. 그럼 빨라져.”

“아.”

청풍은 시종일관 우울한 표정이었다. 출발 전, 음식을 잔뜩 포장하려는 녀석을 내가 제지했기 때문이었다.

“배고파요.”

나는 냉정하게 대꾸했다.

“참으세요.”

절정 고수는 소화력도 절정이더라. 청풍은 먹는 만큼 많이 쌌고, 싼 만큼 도로 처먹었다.

거기에 더해 자주 먹으니 자주 쌀 수밖에…… 젠장, 더러워서 여기까지 해야겠다.

“어디까지 왔냐?”

“방금 지나친 게 아홉 번째 마을이니까…… 짧으면 반 시진, 길면 한 시진 안에 도착할 것 같은데요.”

쏟아지는 햇살에 눈이 따갑다. 나는 중천을 향해 슬금슬금 올라가는 태양을 바라봤다.

“도착하면 정오 쯤 되려나.”

“아마도요.”

“늦었겠지?”

“그야 당연히 늦었죠. 조금 덜 늦으려고 불나게 뛰는 것 아니겠습니까.”

그건 그래.

나는 대답 대신 말에 박차를 가했다. 달릴 때마다 등에 메어 놓은 길쭉한 보퉁이가 말 등을 때린다.

‘어우, 성가셔 죽겠네.’

보퉁이에 든 것은 [이름 없는 검]이다.

본래 적천강에게 돌려줘야 했을 물건이지만 어쩔 수 없이 내가 도로 떠맡게 됐다.

법은 오지게 멀고 주먹은 지리도록 가까운 무림에 사는 이상, 내게 선택권 따위는 없었다.

‘그렇다고 인벤토리에 넣어 놓을 수도 없고.’

화염신장의 비급은 품에 넣어 놨다고 변명이라도 할 수 있지, 주머니에서 검 한 자루가 튀어나왔다가는 빼도 박도 못 한다.

혼자 있다면 모를까, 다른 사람의 눈이 있을 때는 사마외도로 몰리기에 딱 좋은 상황인 거다.

‘그나저나 이거 진짜 잘못 걸렸네.’

귀찮게 애물단지를 맡았다는 불평이 아니다. 화왕 적천강, 그 무시무시한 노인네를 또 만나야 한다는 것이 싫은 거다.



‘조만간 다시 보자꾸나.’



보긴 뭘 또 봐.

몇 시진 전 들었던 말을 떠올릴 때마다 속이 울렁거린다.

틈틈이 나를 힐끔대던 혁무진이 물었다.

“표정이 왜 그러세요?”

“화왕 생각나서.”

“으. 행복한 생각만 해도 부족한데 무슨 그런 끔찍한 상상을 하십니까?”

“너 같으면 생각 안 나겠냐? 조만간 또 온다잖아.”

“그래서 말인데, 저 휴가 좀 주시면 안 됩니까? 갑자기 가족이 보고 싶습니다.”

“이 새끼가 혼자 살려고.”

“사람 일 어떻게 될지 모르는 건데, 죽기 전에 부모님 얼굴이라도 한 번 뵈어야죠.”

“몇 년 동안이나 얼굴 한 번 안 비춘 불효자식이 할 말은 아닌 것 같은데.”

“이번 기회에 효자가 되고 싶습니다.”

“응. 안 돼.”

혁무진의 개소리를 깔끔하게 무시한 나는 하늘을 보며 한탄했다.

“하늘도 무심하지, 그 노인네는 왜 굳이 이런 물건을 나한테 줬을까.”

“들고 다니기 귀찮다잖아요.”

“고작 그런 이유로?”

“그분이면 충분히 그럴 수 있을 것 같은데요.”

“…….”

상당히 설득력 있는데?

“그사이에 물건을 잃어버리거나, 아니면 내가 쓱싹할 수도 있잖아.”

“조장님께서요?”

혁무진이 대단한 농담이라도 들은 것처럼 웃었다.

“그런 분이 여태까지 뭐 했습니까? 죽을 위기가 아니었으면 열화신단도 갖고만 계셨을걸요?”

“그건…… 그렇지.”

“그냥 누구 눈에 안 띄게 꽁꽁 숨겨 두십쇼. 혹시 압니까, 그 대단한 화왕이 그 답례로 한 수 가르쳐 줄지도.”

“가르쳐 주긴 개뿔. 제자를 죽인 놈한테 잘도 그러겠다.”

턱도 없는 소리에 피식 웃음이 나왔다.

열화문은 일인전승 비인부전의 문파라고 했다. 개인적인 감정을 떠나 외인(外人)인 내게 무공을 전수해 준다니.

“헛소리도 적당히 해야 웃기는 거야, 인마.”

“뭐, 듣고 보니 그렇긴 하네요.”

그때, 시체처럼 축 늘어진 채 배고프다를 연발하던 청풍이 입을 열었다.

“은인을 제자로 삼으려는 것 아니에요?”

“……?”

“……?”

“아닌가? 전 그런 것 같은데. 적 할아버지가 은인을 유심히 보는 것 같더라고요.”

“저를요?”

“조장님을요?”

나와 혁무진의 시선이 허공에서 부딪쳤다. 녀석은 황당하다는 표정이었다. 아마 나도 비슷한 얼굴일 거다.

우리는 동시에 실소를 흘렸다.

“잘됐네요. 조장님, 미리 축하드립니다.”

“어, 그래. 고맙다.”

만난 지 고작 하루 이틀밖에 안 된 나를?

워낙 황당무계한 소리라 농담 수준에도 못 들어간다.

“아닌가? 맞나?”

엉뚱한 말을 내뱉은 청풍이 고개를 갸웃거릴 때, 혁무진이 손가락을 들어 저 너머를 가리켰다.

“보이십니까?”

보인다. 닦여진 길을 걸어가는 사람들이. 그리고 저 멀리 보이는 너른 대지와 그 주위를 둘러싼 인파가.

‘태원진가.’

사흘 만의 귀환이었다.
```

## Final English reading copy

```markdown
# Chapter 181

“You cause trouble whenever I take my eyes off you, even for a moment.”

After lightly scolding his Junior Brother, Baek Museong bowed his head toward Woo Hwangtae.

“It seems there was a minor misunderstanding between you. I hope you’ll forgive him with your broad magnanimity.”

His voice was as gentle as his appearance.

Woo Hwangtae was closer to a merchant than a martial artist. His martial arts were First Rate, but he could pride himself on having a Peak-level eye for people and situations, honed through years of running an Escort Bureau.

Under normal circumstances, he might have thought this upon seeing Baek Museong:

*The extraordinary within the ordinary.*

Unfortunately, Woo Hwangtae was not in his right mind at the moment.

Baek Museong had stepped in out of nowhere, and his clean-cut appearance made him seem like an easy mark. His polite voice carried a strong man’s composure, but to Woo Hwangtae, it sounded merely insolent.

“What did you say? Forgive him with my broad magnanimity?”

His voice bubbled with rage as he raised his eyebrows.

“How dare you order me around?”

“That was not my intention, but if I’ve offended you, I apologize.”

“An apology? Hah. You little pup.”

Crack.

Once anger took hold, a person’s judgment naturally grew clouded.

As Woo Hwangtae stepped forward with his fists clenched, the other Sect Leaders hurriedly tried to restrain him.

“Chief Woo, it would be best to stop here.”

“Sect Leader Song is right. Nothing good will come of making a scene.”

“Some bastards who God knows where they rolled in from are acting arrogant, and you’re telling me to put up with it? Do you all think lightly of me too?”

“No, that’s not what we meant.”

“Then what are you trying to say?”

His tone was now nearly that of someone speaking down to them. The Sect Leaders of the Five Gates of Shanxi frowned inwardly, but they had to prevent an unnecessary conflict.

“We only mean that this is the wrong time and place. Have you forgotten our situation?”

“If you insist, I won’t stop you anymore, but… there’s no need to cause trouble when the Jin Family of Taiyuan already has us in its bad books.”

“We understand that you’re angry, but please think of our situation as well. Let’s all try to survive.”

Again. Again with the Jin Family of Taiyuan!

Woo Hwangtae barely managed to swallow the curses that were about to burst from his mouth. If not for the countless eyes and ears around him, he would have hurled every curse he knew and smashed everything in sight.

But the last shred of reason held him back.

“Nggh.”

After barely calming himself, Woo Hwangtae glared at Baek Museong. He was still standing there with a calm expression.

“I’d like nothing more than to beat you to death with a single blow right now, but… I’ll let it pass as a country bumpkin’s mistake. Get lost before I change my mind.”

Baek Museong looked at him for a moment before bowing his head.

“Thank you for showing consideration.”

“Hmph. Lucky bastards.”

But the lucky one was Woo Hwangtae.

If Baek Museong hadn’t sent a Sound Transmission a moment earlier, he would have been hovering between life and death by now.

“Second, stop.”

The second of the Three Plum Blossom Elites, Chulwoo of the Defeated Flower Fist, stopped dead just as he was about to launch himself forward.

A voice that no one else could hear leaked between his teeth.

“He wasn’t satisfied with going after me—he even went after you, Senior Brother.”

“It doesn’t matter.”

“It matters to me. Can’t I hit him once? Just once?”

“That sounds like you want to beat him to death.”

“…I’ll hit him gently. Just once. Really.”

“That sounds like you want to gently beat him to death. Have you forgotten Master’s strict order not to attract unnecessary attention?”

After wrestling with himself, Chulwoo lowered the fist he had been gripping tightly.

“Whew. This is driving me crazy.”

Baek Museong patted him on the shoulder as if he were proud of him.

“You held back well. This too is training.”

“How is this training? I can’t even use the martial arts I worked so hard to learn when the time comes.”

“Mindless killing will only ruin you. Martial arts are meant to hone your essence, qi, and spirit, not to kill someone.”

“Every time I look at you, I get confused. Am I a disciple of Huashan or a Shaolin monk?”

“Could a monk possibly suit your personality? I only feel sorry for all the wooden fish you’ll break in the future.”

Baek Museong let out a quiet laugh, and Chulwoo sighed.

He deeply respected his Senior Brother, but the man was simply too kindhearted. That was the problem.

“Those bastards should have their mouths smashed in…”

“Hey, watch that mouth!”

“All right, all right.”

Chulwoo watched Woo Hwangtae’s back as he grew smaller in the distance and smacked his lips.

*I’ve memorized his face. Let him cross my path once.*

Baek Museong naturally knew what his Junior Brother was thinking. He shook his head from side to side.

“Stop thinking nonsense and find the youngest.”

“Did Eunhyang disappear again?”

“Yes, just like you.”

Chulwoo flinched.

“I went to take a leak.”

“That’s right. But why did someone who went to take a leak end up picking a fight in a crowded place?”

“I was on my way back after relieving myself. Seriously, Senior Brother, you don’t believe me? I haven’t washed my hands yet. Want to smell them?”

“…Never mind.”

Baek Museong rubbed his temple. He cherished his Junior Brothers more than anyone, but they were exceptionally difficult to handle.

At least Chulwoo was large enough to find quickly. The youngest Junior Disciple, Eunhyang, was practically invisible in a crowd like this.

“Do you see anything?”

Chulwoo, who was at least two heads taller than everyone else, swept his gaze around.

“Not really. There are too many people.”

Even the eyes of a Peak master would have difficulty finding a small girl in the endless, bustling crowd.

There were so many people that peddlers had even set up stalls all over the place.

“By the way, was the Jin Family of Taiyuan always this big? I’d never even heard of it before we came.”

“Those in the know do. The current Sect Leader, the Shanxi Extraordinary Hero, is fairly well known, and so is the Heaven Shaking Sword, isn’t he?”

“I don’t know the Shanxi Extraordinary Hero, but the Heaven Shaking Sword… Is that the guy who’s supposedly one of the Ten Dragons and Phoenixes?”

“Don’t call him that. Watch your mouth.”

“He’s just a milquetoast scholar who attends an academy. In my opinion, Senior Brother is much more…”

“Hey. Where did you learn that bad habit of judging people before you’ve even seen them? He’s clearly a gifted talent.”

“Well, for someone from Shanxi Province, being that good is practically the same as a dragon rising from a ditch.”

Chulwoo answered indifferently, then suddenly frowned.

“Wasn’t there someone else besides the Heaven Shaking Sword? Some kind of dragon or loach?”

“A dragon? Do you mean the Sleeping Dragon of Shanxi?”

“Ah, right. The Sleeping Dragon of Shanxi.”

“I heard he’s a fairly impressive talent, though not as much as the Heaven Shaking Sword.”

“Whether he’s a dragon or a loach, I’ve heard about him nonstop on the way here. I should at least see his face once.”

Baek Museong’s lips curled slightly upward when he saw Chulwoo clench his fists.

“Do you want to spar with him?”

Chulwoo scratched the back of his head.

“Not necessarily. I’d win anyway.”

“Competitive pride is a good thing, but you should avoid causing trouble whenever possible.”

“Would there even be anything to cause trouble over? Since we came all this way, I just want to see what he’s made of.”

Baek Museong stared intently at his Second Junior Brother.

Despite his words, Chulwoo was obviously quite curious.

After spending years cooped up on Huashan and facing the same people every day, he seemed excited.

“You’ll see him soon enough. Of course, we have to find the youngest first.”

The words he added at the end sounded more like a sigh.

The gates of the Jin Family of Taiyuan were already open, and the invited guests were streaming inside like a gathering cloud.

Baek Museong was wondering if he would have to climb a tree when—

“Senior Brother, it’s all right to be a little noisy, isn’t it?”

“What?”

Chulwoo grinned and drew in a deep breath.

The next moment, a thunderous shout burst forth.

“Eun—hyang!”

There was no time to stop him. Chulwoo’s voice was as tremendous as his body.

The people around them covered their ears and dropped to the ground, while the countless people who had been laughing and chatting abruptly fell silent.

Just as everyone stood in silence as if cold water had been thrown over them—

“Big Brothers! I’m over here!”

Far away, Chulwoo spotted a young girl jumping up and down enthusiastically in place. He spoke triumphantly.

“Ha-ha! Senior Brother, I found her!”

“…Yes, good job. Very good.”

Baek Museong put a hand to his head.

That was when hundreds of people began murmuring and parted like reeds splitting in the wind.

At the end of the opened path stood a man as tall as an iron tower. Chulwoo unconsciously muttered,

“Is that a man or a bear?”

“He’s a man. If not for him, the Jin Family of Taiyuan wouldn’t be what it is today.”

Baek Museong respectfully performed a cupped-fist salute toward the bear-like man, Jin Wikyung.

* * *

Thud-thud-thud-thud!

The scenery whipped past us. Hyuk Mujin, riding right beside me, shouted over the pounding hooves.

“It was definitely slow when we were going there, but it’s incredibly fast on the way back. Is it because we took it easy two days ago?”

“Everything has a reason.”

“What reason?”

“It gets faster when no one tries to eat something while riding a horse.”

“Ah.”

Cheongpung had worn a gloomy expression the entire time. Before we left, I had stopped him from packing a huge amount of food.

“I’m hungry.”

I answered coldly.

“Endure it.”

A Peak master’s digestive power was Peak-level too. Cheongpung crapped as much as he ate, then ate as much as he crapped.

On top of that, he ate often, so he had no choice but to crap often…

Damn it. This is too disgusting. I’ll stop there.

“How far have we come?”

“We just passed the ninth village, so… We should arrive in half a shichen at the earliest, or a full shichen at the latest.”

The sunlight pouring down made my eyes sting. I looked up at the sun, which was slowly climbing toward the middle of the sky.

“We’ll arrive around noon, then?”

“Probably.”

“We’re late, aren’t we?”

“Of course we’re late. Isn’t that why we’re riding like hell, trying to be a little less late?”

He was right.

Instead of answering, I dug my heels into the horse. Every time it ran, the long bundle strapped across my back thumped against its body.

*Ugh, what a pain.*

The bundle held the Unnamed Sword.

It was something I had originally been supposed to return to Jeok Cheongang, but I had ended up taking it back again.

As long as I lived in a Murim where the law was damn far away and fists were painfully close, I had no choice.

*I can’t put it in my inventory either.*

I could at least claim that I had tucked the Flame Divine Palm martial arts manual inside my clothes. But if a sword suddenly came flying out of my pocket, there would be no way to explain it.

If I were alone, it might be different. But with other people watching, it was the perfect situation to be accused of practicing demonic, heterodox arts.

*This really turned into a nasty bind.*

It wasn’t that I was complaining about being saddled with a troublesome object. I simply hated the thought of having to meet Fire King Jeok Cheongang—that terrifying old man—again.

*I’ll see you again soon.*

*Who wants to see him again?*

Every time I remembered the words I’d heard a few shichen ago, my stomach churned.

Hyuk Mujin, who had been sneaking glances at me from time to time, asked,

“Why do you look like that?”

“I was thinking about the Fire King.”

“Ugh. We don’t have enough time for happy thoughts, so why are you imagining something so horrible?”

“If you were me, wouldn’t you think about him? He said he’d come again soon.”

“Speaking of which, could you give me a vacation? I suddenly miss my family.”

“This bastard is trying to save his own skin.”

“You never know what might happen. Before I die, I should at least see my parents’ faces one more time.”

“That doesn’t sound like something an unfilial son who hasn’t shown his face in years should be saying.”

“I want to become a good son while I have the chance.”

“No. You can’t.”

I completely ignored Hyuk Mujin’s bullshit and looked up at the sky with a sigh.

“What an unfeeling heaven. Why did that old man have to give me this thing?”

“He said it was a pain to carry around.”

“For such a petty reason?”

“With him, I can completely believe it.”

“…”

That was actually pretty convincing.

“I could lose it in the meantime. Or I could quietly swipe it.”

“You, Captain?”

Hyuk Mujin laughed as if he had just heard a brilliant joke.

“What have you done all this time? If you hadn’t been in mortal danger, you would have just kept the Blazing Flame Divine Pill too, wouldn’t you?”

“That’s…”

He had a point.

“Just hide it somewhere no one will notice. Who knows? Maybe that great Fire King will teach you a move in return.”

“Teach me, my ass. As if he’d do that for someone who killed his Disciple.”

I let out a quiet laugh at the absurdity of it.

The Fire Gate Clan was said to be a sect whose arts were passed down to a single successor and never taught to outsiders. Setting personal feelings aside, the idea that he would teach martial arts to an outsider like me was ridiculous.

“Your nonsense is only funny when you keep it in moderation, you idiot.”

“Well, now that you mention it, that’s true.”

At that moment, Cheongpung, who had been hanging limp like a corpse and repeating that he was hungry, spoke up.

“Isn’t he trying to take you as his Disciple, Benefactor?”

“…”

“…”

“Maybe not? I think he is. Grandpa Jeok seemed to be watching you closely, Benefactor.”

“Me?” I asked.

“Captain?” Hyuk Mujin asked.

Our gazes collided in midair. He looked utterly baffled. I was probably wearing much the same expression.

We both let out a quiet laugh.

“That’s great. Congratulations in advance, Captain.”

“Yeah. Thanks.”

*Me? Someone he’d known for barely a day or two?*

It was such an absurd idea that it did not even qualify as a joke.

“Or not? Is that right?”

As Cheongpung tilted his head after saying something so bizarre, Hyuk Mujin raised a finger and pointed into the distance.

“Can you see it?”

I could.

People were walking along a well-kept road. Farther ahead was a broad expanse of land surrounded by a crowd.

*The Jin Family of Taiyuan.*

It was my return after three days away.
```
