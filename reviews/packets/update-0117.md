<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0117.txt",
      "sha256": "65e80b49f594f573bfe4755822ad409dcca1424ef466493b700a1491806a687e",
      "bytes": 13901
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "098d9d83e56f161f79faf645bcb55515712becf1064081fd9364224ebdf6748c",
      "bytes": 2340
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "a1e0d5aba5ab3b4205c617090d7b04d0d5b038e74ceaafd38f4b52580ab6a1aa",
      "bytes": 17559
    },
    {
      "path": "characters/Cheol Mubaek.md",
      "sha256": "583470c03fefbbffacac1e36dc504bef1050290022b62048139c7a7f167b2c8a",
      "bytes": 724
    },
    {
      "path": "characters/Jin Mukyung.md",
      "sha256": "2670d629004e3b154da31a7acd4d7e90749dfac71698108c28a4a767b7e9ff0b",
      "bytes": 1221
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "15f4db471feb0d4e24cb9bf1ff61b4160fbd534dac11d145823802c62e630326",
      "bytes": 24117
    },
    {
      "path": "characters/Jin Wikyung.md",
      "sha256": "6d1866fa5a8a6ce7a98837a0a3b85ce04f0ef7db2cf3748238299190c3db8ca6",
      "bytes": 8154
    },
    {
      "path": "characters/Jopil.md",
      "sha256": "67ccf7cc5c6715a3be436c26f60d8933d8587af7de32b14e412b93bc2ef3dd30",
      "bytes": 2804
    },
    {
      "path": "characters/Lee Seowol.md",
      "sha256": "0615950891719c9d9de0cc67589b8eee8cb69096b17df7950bedc839cd57e1ea",
      "bytes": 749
    },
    {
      "path": "characters/Pung Yang.md",
      "sha256": "91460683f5eaebdcef1727f31719efaed7838bf459335dc4cf8ffa4d0ebd2ee1",
      "bytes": 910
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "fb5958b8c27242e020a7e3bff7541c90f9646f9bf39d2db3c730ffa2b2448c85",
      "bytes": 16853
    }
  ],
  "estimated_tokens": 19427
}
-->

# Durable State Update — Chapter 117

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 117. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 20 concise items, `open_questions` to at most 8
items, and `temporary_decisions` to at most 8 items. Keep the serialized context
under 16384 UTF-8 bytes. Use only chapter
numbers through 117. `profile_updates` may replace one exact, uniquely occurring
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
  "chapter": 117,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 117,
    "continuity_sources": [117],
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
    "Cheol Mubaek personally protected Lee Seowol during the Red Wind Band's assault and was critically wounded after Pung Yang defeated him alone.",
    "Pung Yang has used the Temporary Strength Pill, a rare power-enhancing pill with substantial aftereffects.",
    "Lee Seowol agreed under coercion to marry Pung Yang in exchange for the survival of the Mount Heng Sword Sect's captured martial artists and Cheol Mubaek.",
    "Jin Mukyung and Jin Taekyung entered the Mount Heng fortress and attacked Pung Yang and the Red Wind Band.",
    "Before Pung Yang took the pill, Jin Mukyung held an overwhelming advantage; the pill shifted the battle, and Pung Yang wounded Mukyung.",
    "Pung Yang discovered the Crimson Blood martial arts and five Temporary Strength Pills in a hidden plateau tomb, then reached the Peak realm in two years.",
    "Pung Yang can temporarily manifest imperfect Sword Force after taking a Temporary Strength Pill.",
    "Pung Yang seeks the martial arts of both the Jin Family of Taiyuan and the Mount Heng Sword Sect.",
    "The battle between Jin Mukyung and Pung Yang is unresolved.",
    "Taekyung has cleared much of the surrounding Red Wind Band and is preparing to confront Pung Yang."
  ],
  "continuity_sources": [
    116
  ],
  "open_questions": [
    "What is the origin and full long-term effect of the Temporary Strength Pill?",
    "Can Jin Taekyung and Jin Mukyung defeat Pung Yang and rescue Lee Seowol and Cheol Mubaek?",
    "Will Lee Seowol's coerced agreement be carried out or overturned?",
    "Whether the Mount Heng Sword Sect will survive the continuing assault remains unresolved."
  ],
  "safe_through": 116,
  "temporary_decisions": [
    "Render 일류 초입 as early First Rate.",
    "Retain shichen and explain three shichen as six hours in context.",
    "Render 화시 as fire arrow, 쇠뇌 as crossbow, and 충차 as battering ram.",
    "Render 수라멸권 as Shura Annihilating Fist.",
    "Render 항산권문 as Mount Heng Fist Sect.",
    "Render 벽곡단 as fasting pills.",
    "Render 잠력단 as Temporary Strength Pill and explain its literal meaning in a footnote.",
    "Render 검강 as Sword Force, 적혈십이검 as Crimson Blood Twelve Swords, and 적혈심법 as Crimson Blood Cultivation Technique."
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

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 진위경    | **Jin Wikyung**    |
| 진무경    | **Jin Mukyung**    |
| 이소월    | **Lee Seowol**     |
| 철무백    | **Cheol Mubaek**   |
| 조필     | **Jopil**          |
| 산서잠룡   | **Sleeping Dragon of Shanxi** | Jin Taekyung   |
| 진천검    | **Heaven Shaking Sword**      | Jin Mukyung    |
| 항산호    | **Tiger of Mount Heng**       | Cheol Mubaek   |
| 태원진가   | **Jin Family of Taiyuan**        |
| 항산검문   | **Mount Heng Sword Sect**        |
| 화산파    | **Huashan**                      |
| 남궁세가   | **Nangong Family**               |
| 삼류     | **Third Rate**    |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 무인     | **martial artist**                               | Default term                                          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 심법     | **cultivation technique**                        | Especially internal cultivation                       |
| 검법     | **sword technique**                              |                                                       |
| 구결     | **formula**                                      | Mnemonic/oral formula for a martial art               |
| 깨달음    | **enlightenment** / **insight**                  | Martial enlightenment                                 |
| 기세     | **aura** / **momentum**                          | Depends on scene                                      |
| 검기     | **Sword Energy**                                 | When functioning as projected weapon qi               |
| 정파     | **orthodox faction**                             |                                                       |
| 문주     | **Sect Leader**                              |
| 장로     | **Elder**                                    |
| 대장로    | **Head Elder**                               |
| 일격     | **One Strike**                         |
| 상태               | **Status**                     |
| 레벨               | **Level**                      |
| 체력               | **Stamina**                    |
| 산서     | **Shanxi**             |
| 태원     | **Taiyuan**            |
| 항산     | **Mount Heng**         |
| 화산     | **Huashan**            |
| 귀가      | **your family**                                                 |
| 풍양 | **Pung Yang** | Personal name of the Red Wind Band Leader. |
| 삼재검법 | **Three Calamities Sword Technique** | Sword technique Mukyung assumes Taekyung is pretending to use. |
| 일문일살 | **One Question, One Kill** | Jopil's alias. |
| 일섬 | **One Annihilation** | Named spear technique Taekyung uses to kill the Boss Zone monster in one blow. |
| 소월 | **Seowol** | Short form of Lee Seowol used by Cheol Mubaek. |
| 잠력단 | **Temporary Strength Pill** | Rare pill that temporarily enhances strength; Pung Yang has only three and uses one against Cheol Mubaek and another during the battle. |
| 적혈심법 | **Crimson Blood Cultivation Technique** | Cultivation technique discovered by Pung Yang. |
| 검강 | **Sword Force** | Higher manifestation than Sword Energy; Pung Yang's is explicitly imperfect because of insufficient enlightenment. |

## Listed compact profiles

### Cheol Mubaek.md

# Cheol Mubaek (철무백)

- **Safe through:** Chapter 116
- **Aliases:** Tiger of Mount Heng
- **Role:** Peak master known as the Tiger of Mount Heng; longtime close friend and peer of Lee Cheonbaek; protector of Lee Seowol
- **Personality:** Fierce, short-tempered, intimidating, and fiercely protective; becomes gentle and attentive toward Seowol
- **Voice:** Roaring and confrontational when rebuking the Mount Heng senior figures; gentle and affectionate when speaking to Seowol
- **Relationships:** Close friend and peer of Lee Cheonbaek; paternal uncle and protector of Lee Seowol; feared and respected by the Mount Heng Sword Sect's senior figures

### Jin Mukyung.md

# Jin Mukyung (진무경)

- **Safe through:** Chapter 116
- **Aliases:** Heaven Shaking Sword; Jin Family Second Young Master
- **Role:** Second son of the Jin Family of Taiyuan; twenty-three-year-old cadet at Heaven’s Gate Temple; a young Peak-level genius swordsman
- **Personality:** Reserved, terse, and easily irritated by exaggerated praise; glares coldly when Taekyung identifies him
- **Voice:** Quiet and resonant; clipped and blunt in direct speech
- **Relationships:** Taekyung’s older brother and current martial arts instructor; returned to the Jin Family after several years away

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 116
- **Aliases:** Sleeping Dragon of Shanxi
- **Role:** Modern-world protagonist; recently fired after seven years at his job; C-rank Hunter who defeated eight B-rank Minotaurs and killed a Level 70 B-rank Minotaur Warrior in one blow; First Rate martial artist standing before the Peak realm; youngest son of the Jin Family of Taiyuan; new owner of a two-story detached house in Goyang intended for his family; Qi Sense reaches a seventy-meter radius
- **Personality:** Hungry, self-aware, dryly observant, and willing to take a questionable opportunity when desperate; treats the impossible as a game until the danger becomes undeniable
- **Voice:** First-person, conversational, dryly self-mocking; uses vivid trap-and-prey imagery, game jargon, and occasional profanity
- **Relationships:** Jin Mukyung’s younger brother and current student; son of a deceased father; supports his mother and younger sibling; has a strained relationship with Lee Seowol, the current Sect Leader of the Mount Heng Sword Sect

### Jin Wikyung.md

# Jin Wikyung (진위경)

- **Safe through:** Chapter 113
- **Aliases:** Junzi Sword
- **Role:** Thirty-five-year-old Lesser Family Head and future Family Head of the Jin Family of Taiyuan; preparing to consolidate Shanxi Murim under the family's leadership
- **Personality:** Calm and authoritative in public; affectionate and protective toward Taekyung beneath a stern mask; accepts responsibility from his subordinates and shows immediate concern for family
- **Voice:** Restrained, formal, and commanding with subordinates; openly affectionate with Taekyung
- **Relationships:** Taekyung’s eldest brother and future Family Head; head of Wipeng; member of the Jin Family

### Jopil.md

# Jopil (조필)

- **Safe through:** Chapter 110
- **Aliases:** One Question, One Kill
- **Role:** Wandering martial artist and leader of a special detachment attacking the Jin Family of Taiyuan
- **Personality:** Cruel, amused by violence, and motivated by both payment and the pleasure of hunting his targets
- **Voice:** Smoothly mocking and deceptively gentle when threatening victims
- **Relationships:** Leader of roughly fifty wandering martial artists; commands Black Mountain Blade

### Lee Seowol.md

# Lee Seowol (이소월)

- **Safe through:** Chapter 116
- **Aliases:** None
- **Role:** Current Sect Leader of the Mount Heng Sword Sect; third child of Lee Cheonbaek and his last surviving descendant; publicly insists on being addressed as Sect Leader rather than Young Lady
- **Personality:** Cold, commanding, and composed; capable of stopping a fierce confrontation with a calm request
- **Voice:** Clear and cool, gentle with Cheol Mubaek but frost-cold and firm when asserting her authority
- **Relationships:** Daughter of the deceased Lee Cheonbaek; younger sister of the deceased Young Sect Leader, Lee Seogeun, and Lee Seogwang; Cheol Mubaek's niece and protected charge

### Pung Yang.md

# Pung Yang (풍양)

- **Safe through:** Chapter 116
- **Aliases:** Red Wind Band Leader
- **Role:** Leader of the Red Wind Band, commanding at least two hundred mounted bandits; became a mounted bandit at thirteen, reached First Rate by age thirty, and rose from squad leader to band leader three years ago; discovered the Crimson Blood martial arts and a case containing five Temporary Strength Pills in a hidden plateau tomb, reached the Peak realm in two years, and can temporarily manifest imperfect Sword Force by taking a pill
- **Personality:** Foxlike, ruthless, observant, controlled, and willing to kill subordinates who disobey his orders
- **Voice:** Calm, concise, and authoritative when issuing orders
- **Relationships:** Leads the Red Wind Band and controls former members of other mounted-bandit groups who joined his force

## Korean source

```text
＃117화



진무경은 그간 수많은 무공을 익혔다. 그중에는 과거 한 시대를 풍미한 절정 무공부터, 촌구석 좌판에서조차 쉽게 찾아볼 수 있는 삼류 무공까지 가리는 일도 없었다.

그러나 지금 이 순간, 그는 깨달았다.

‘강하다. 내가 지금까지 익힌 어떤 무공보다.’

후우우웅.

일도양단의 기세로 떨어지는 한 자루의 곡도.

남궁세가의 제왕검형, 화산파의 매화검법 같은 초절정의 무공이 아니다. 이건 길거리 삼류 잡배도 안다는 삼재검법의 일초, 태산압정(泰山壓頂)이었다.

‘태산을 누른다. 어떤 느낌인지 알 것 같군.’

도신 위로 일렁이는 붉은 도기(刀氣)는 태산을 누르는 것으로도 모자라 쪼갤 수도 있을 것 같다.

‘막을 수 없어.’

찰나에 불과한 시간, 진무경은 망설임 없이 몸을 날렸다.

쏴아아악!

아슬아슬하게 진무경의 옷깃을 스친 도기가 땅에 닿았다. 어떤 굉음도, 진동도 없이 지면이 쩍 갈라지는 광경은 전율 그 자체였다.

“이걸 피해?”

그러나 정작 풍양은 이 결과가 마음에 들지 않았다.

전력을 다한 일격이었다. 잠력단의 효능을 십이 할 끌어올렸음에도 진무경에게 작은 상처 하나 입히지 못했다.

‘항산호도 받아치는 게 고작이었는데.’

완숙한 절정 고수인 철무백조차 그 대가로 내상을 입고 물러나야 했다. 그런데 이립도 되지 않은 애송이가 어떻게?

“진천검…… 이름값은 한다 이거지?”

자세를 고쳐 잡은 진무경이 덤덤하게 대꾸했다.

“이 정도는 피해야지.”

“막을 수 없었던 건 아니고?”

풍양의 입가에 비웃음이 떠올랐다.

“하긴, 그 대단한 태원진가의 자제께서 나려타곤(懶驢打滾)으로 도망칠 정도니 오죽 다급했을까.”

나려타곤. 게으른 당나귀가 바닥을 구르는 모습에 빗댄 말이다. 위신을 중요시하는 명문 정파 출신의 무인들에게는 치욕이나 다름없는 말이었지만 진무경에겐 달랐다.

“당나귀든 노새든 상관없다. 체면이 밥 먹여 주나?”

“뭐?”

“목숨값에 비하면 싸게 먹힌 거지. 그리고…….”

시종일관 덤덤한 얼굴이던 그가 피식 웃었다.

“왜 웃지?”

“그냥, 절정 고수한테 돌팔매질하는 놈도 있는데 나려타곤이 대수일까 싶어서.”

의중을 알 수 없는 실없는 농담에 풍양은 자신도 모르게 되물었다.

“절정 고수한테 돌팔매질? 제정신인가?”

“처음 그 얘기를 들었을 때는 나도 비슷한 생각이었지. 그런데 곰곰이 생각해 보니 충분히 그러고도 남을 놈이라.”

“어떤 미친놈인지 얼굴 한번 보고 싶군.”

“금방 볼 수 있을 거다.”

“그게 무슨 말이지?”

풍양이 가벼운 의문을 느낀 그때였다.

쐐애애액!

등 뒤에서 느껴지는 날카로운 기세.

돌아선 그의 붉은 눈동자에 잘생긴 청년의 얼굴이 비쳤다.

‘산서잠룡.’

느리게 흐르는 시간 속에서 진태경이 씩 웃었다. 그가 쥔 철창은 이미 풍양의 가슴을 향해 쇄도하고 있었다.

콰아아아아!

일섬.

창날에서 뿜어져 나온 와류가 풍양을 집어삼켰다.



* * *



몸 상태는 완벽했다. 조무래기들을 처리하는 과정에서 레벨 업을 한 덕분에 피로와 체력이 완전히 회복되었기 때문이다.

타이밍도 괜찮았다. 풍양의 넓고 무방비한 등이 꼭 창으로 쑤셔 달라고 유혹하는 것 같았다.

이 그림을 장식할 마지막 화룡점정(畵龍點睛)으로 택한 것이 일섬이다. 지금까지 이거 맞고 멀쩡한 놈을 못 봤으니까.

그런데…….

“사람을 보고 덤볐어야지.”

짐승의 울음처럼 낮은 목소리. 풍양은 자신의 눈처럼 붉은 기(氣)의 장막에 휩싸여 있었다. 일섬이 뿜어내는 와류를 말끔히 막아 낸 그것은 살아 있는 갑옷처럼 꿈틀거렸다.

‘이런 걸 무협 소설에서 뭐라고 하더라.’

아, 그래. 기억났다. 나는 간신히 입술을 뗐다.

“호신강기(護身罡氣)?”

“개 눈깔은 아니군.”

“아니, 시바…….”

검기, 검강으로도 부족해서 이제는 호신강기야?

눈앞이 캄캄해져 멍하니 있는 나를 본 풍양이 입꼬리를 말아 올렸다.

“후회해도 늦었다.”

쉭!

곡도에서 솟구친 도기 한 가닥이 머리칼을 뭉텅 잘라 낸다. 바로 허리를 숙여서 망정이지, 아주 조금이라도 늦었다면 잘리는 건 머리였을 것이다.

‘미친.’

튀어나오려는 욕설을 삼키며 몸을 날리기 무섭게, 사나운 도격이 내가 있던 자리를 난도질했다.

쉬쉬쉬쉭!

문제는 그 도기 하나하나가 강력하기 짝이 없다는 사실이다. 얼어붙은 지면이 순두부처럼 쪼개지는 광경에 등골이 서늘해졌다.

‘이거, 까딱했다가는 진짜 골로 가겠는데.’

A급 마법 방어구를 차도 모자랄 판국에 천 쪼가리 하나 걸치고 싸우려니 살얼음판이 따로 없다.

무엇보다…….

‘저 자식은 지치지도 않나.’

호신강기를 유지하는 것만으로도 막대한 공력이 소모되고 있을 게 분명한데, 지금의 그는 공력이 마르지 않는 샘 같았다.

“형제라더니, 쥐새끼처럼 도망치는 모양새가 아주 똑 닮았구나.”

풍양이 비웃음을 흘린 그 순간이었다.

“별로 듣기 좋은 말은 아닌데.”

등 뒤에서 홀연히 나타난 진무경이 검을 흩뿌렸다. 쭉 뻗어 나간 푸른 섬광이 놈의 목을 노렸다.

쩡!

하지만 무엇이든지 베어 낼 것 같던 진무경의 검기도 호신강기를 뚫을 수는 없었다. 풍양이 여유로운 얼굴로 검기가 후려친 목을 쓰다듬었다.

“뻐근하군. 끝인가?”

“그럴 리가.”

쐐애애애액!

진무경이 거침없이 짓쳐 들어가자 동시에 풍양의 손에 들린 곡도가 움직였다. 공기의 흐름이 바뀌었다고 느낄 정도로 강대한 기세.

이건 내가 끼어들 수 없는 싸움이다.

쉭!

마침내 진무경의 푸른 검기와 풍양의 붉은 도기가 맞닿은 순간, 어마어마한 기파와 함께 귀가 먹먹해질 만큼 커다란 굉음이 터져 나왔다.

콰아아아아!

두 다리를 딛고 서 있던 이들 중 대부분이 중심을 잃고 휘청거렸다.

하지만 나는 눈을 부릅뜨고 이 엄청난 격돌의 결과를 지켜보았다.

‘누구냐.’

격돌의 충격으로 흩날리는 흙먼지 사이, 서로를 마주 보고 있는 두 사람이 보였다.

손잡이만 남은 도검과 굳게 다문 입술. 짧은 침묵을 먼저 깨트린 것은 풍양이었다.

바닥에 무릎을 꿇은 놈은 검붉은 핏물을 토해 냈다.

“큭, 쿠에에엑!”

장내에 작은 환호가 울려 퍼졌다. 당당히 서 있는 진무경과 무릎을 꿇은 풍양. 이 치열한 전투의 승패가 갈린 순간이다.

‘이겼어.’

얼마나 치열한 공방전이 있었는지 모두 보진 못했지만, 그 과정에서 풍양이 먼저 내상을 입은 것이 틀림없다.

그 증거로 놈의 가슴팍에는 지금까지 볼 수 없었던 선명한 장인(掌印)이 찍혀 있었다. 아마 저것이 결정타였을 것이다.

“쿨럭, 쿨럭.”

풍양이 피에 젖은 입가를 닦으며 비틀비틀 일어났다.

“격산타우(隔山打牛)라. 그렇다고 해도 호신강기가 이렇게 허무하게 깨질 줄은 몰랐는데…… 내 깨달음이 부족했던 건가?”

진무경의 묵묵부답에 놈이 혀를 찼다.

“빌어먹을, 잠력단을 쓰고도 이 지경이라니. 당분간은 심산유곡에 틀어박혀 무공이나 수련해야겠군.”

심산유곡? 수련?

나는 진심으로 궁금해져서 물었다.

“어딜 간다고?”

“기다리면 곧 알게 될 것이다. 너희 형제도 데려갈 생각이니까.”

이거 되게 당황스럽네.

집들이 초대니까 티슈라도 한 박스 사 가야 되나?

“어, 우리를?”

“그래, 네가 알고 있는 태원진가의 무공 구결이 필요하거든. 적혈심법의 난폭한 진기 운용을 보완하는 데 큰 도움이 되겠지.”

거기까지 듣고 나니 아까부터 혀끝에 맴돌던 말이 저절로 튀어나왔다.

“혹시 미친놈이세요?”

확인해 보진 않았지만 아마 다들 나와 같은 표정일 거다.

이미 승패가 명확히 갈린 마당에, 뭐?

“심산유곡에서 수련은 개뿔, 북망산 효도 관광 보내 줄 테니까 거기서 수련하시든가.”

“북망산? 네가 나를?”

“꼭 내가 아니더라도 댁을 북망산으로 보내 줄 사람들은 많지.”

어이없다는 듯 웃는 풍양에게 등 뒤를 턱짓해 보였다.

어느새 항산검문의 무인들이 병장기를 빼 들고 슬금슬금 다가오는 중이다.

그중 유난히 원독에 찬 눈빛을 보내는 미녀가 항산검문의 신임 문주 이소월이겠지.

‘이 인간도 편히 죽긴 글렀군.’

이제 지난 악행의 업보를 치를 시간이다. 나는 풍양을 향해 창을 까딱거렸다.

“이래도 자꾸 헛소리할래?”

잠시 우리를 물끄러미 바라보던 놈이 입을 열었다.

“글쎄, 큰 착각을 하고 있는 것 같은데.”

이어지는 목소리에는 숨길 수 없는 웃음기가 묻어 나왔다.

“너희들 중에 나를 쓰러트릴 수 있는 자가 있을까?”

“그게 무슨 개소리…….”

“믿기 힘들다면 내 앞에 있는 진천검에게 물어보는 게 빠르겠지. 자, 내 말에 대해 어떻게 생각하나?”

풍양의 물음에도 진무경은 대답하지 않았고, 나는 그제야 깨달았다.

아까부터 왜 그가 말이 없었는지. 왜 망부석처럼 그 자리에 서 있기만 했는지.

툭.

풍양의 손이 진무경의 가슴에 닿았다. 언제부터였을까, 이미 의식을 잃은 몸뚱어리가 힘없이 허물어진다.

그제야 보이는 그의 상반신에는 다섯 개의 비수가 나란히 꽂혀 있었다.

털썩.

침묵에 휩싸인 좌중을 쓸어 본 붉은 눈동자가 반달처럼 휘었다.

“자, 이제 마무리를 지어 볼까.”



* * *



‘마무리’는 빠르게 시작됐다.

느긋한 발걸음으로 우리를 향해 다가오던 그의 소매에서 튀어나온 십여 개의 비수가 시작이었다.

쉭! 푸푸푸푹!

제아무리 가까운 거리였다지만 진무경도 피하지 못한 비도술이다. 풍양이 던지는 비수는 정확히 표적을 꿰뚫었고, 어김없이 비명이 터져 나왔다.

“큭.”

“커헉!”

이미 피로가 극에 달한 데다 개개인의 무력도 높지 않은 항산검문의 무인들은 쉬운 사냥감이었다.

내가 비로소 풍양을 가로막았을 때는 이미 십여 명이 목숨을 잃은 후였다.

“멈춰.”

놈은 고개를 가로저었다.

“아니지, 그게 아니야. 명령은 강자에게 주어진 권리거든.”

“……넌 내가 죽인다.”

“진천검이라면 모를까, 너 같은 햇병아리가 감히?”

풍양의 비웃음에 나는 입을 다물었다. 틀린 말은 아니다. 놈을 막아선 것은 용기와 만용이 반쯤 뒤섞인 결정이었다.

‘하지만 어떻게 놈을 쓰러트리지?’

머릿속이 새하얗게 타들어 가는 것 같다. 복잡한 생각 속에 떠오르는 두 사람의 얼굴이 있었다.

그중 첫 번째는 대장로다. 지금까지 만난 무인 중 가장 고강하고 절망적이었던 상대. 그러나 그때에는 진위경과 태원진가 무인들의 도움이 있었다.

‘지금은?’

없다. 아무도 없다. 잠력단을 복용한 풍양은 대장로에 비견되거나 그 이상의 고수일 텐데, 놈을 상대할 사람은, 나뿐이다.

그러자 자연스럽게 두 번째 인물이 생각났다.

‘일문일살 조필.’

어쩌면 조필이야말로 나로 하여금 진짜 위기를 겪게 한 인물일지도 모른다. 무림에서 얻은 수하를 처음으로 잃었고, 죽기 직전까지 갔으니까. 그러고 나서야 놈을 쓰러트릴 수 있었다.

하지만 지금의 풍양은 조필과는 격이 다른 존재다.

‘이 개 같은 잠력단…….’

생각할수록 욕만 튀어나온다. 어떤 새끼가 만들었는지 면상 한번 보고 싶을 정도다.

“주제 파악이 끝났으면 조용히 찌그러져 있어라.”

잠력단을 믿고 천하제일 고수 행세를 하는 풍양을 보니 속이 뒤틀린다. 차라리 조필 정도만 됐었어도 어떻게 해 보는 건데…….

‘……어라?’

문득 잊고 있던 사실 하나가 뇌리를 스쳤다.

조필, 놈이 갖고 있던 물건 중에 살벌한 게 하나 있었지 아마?

‘열화신단.’

복용 시 반 갑자의 공력을 얻을 수 있는 희대의 영단(靈丹)인 동시에 까딱하면 영단이 품은 화기(火氣)에 죽을 수도 있는 양날의 검.

‘열화신단, 열화신단이라…….’

다음 순간.

멍하니 생각에 잠겨 있던 나는 불쑥 입을 열었다.

“야.”

어느새 나를 지나쳐 간 풍양이 멈칫하더니 돌아섰다.

“야? 지금 나한테 한 말이냐?”

“그래, 이 약쟁이 새끼야.”

“허, 이 핏덩이가 지금 뭐라 지껄이는…….”

“너만 약 처먹으니까 좋았냐?”

“……뭐?”

나는 황당함과 분노가 점철된 놈의 얼굴을 향해 또박또박 내뱉었다.

“혼자 약 처먹으니까 좋았냐고.”

이에는 이. 도핑에는 도핑.

이제는 나도 약 빨고 싸운다. 이 자식아.
```

## Final English reading copy

```markdown
# Chapter 117

Jin Mukyung had learned countless martial arts over the years. Among them were everything from Peak-level arts that had once defined an era to Third Rate martial arts easily found even on a street stall in some backwater village.

But at this very moment, he realized something.

*It’s strong. Stronger than any martial art I’ve learned until now.*

Fwoooosh.

A curved saber descended with the force of a single slash cleaving something in two.

It wasn’t a Supreme Peak art like the Nangong Family’s Emperor Sword Form or Huashan’s Plum Blossom Sword Technique. This was the first move of the Three Calamities Sword Technique, Mount Tai Presses Down on the Crown—the move even a Third Rate street thug would know.

*Pressing down Mount Tai. I think I know what that feels like.*

The red saber qi rippling over the blade seemed capable of doing more than merely pressing down Mount Tai. It looked like it could split the mountain apart.

*I can’t block it.*

In the briefest instant, Jin Mukyung threw himself aside without hesitation.

Shraaaaak!

The saber qi grazed Jin Mukyung’s clothes by a hair before striking the ground. The sight of the earth splitting wide open without a single boom or tremor sent a shiver through him.

“You dodged that?”

But Pung Yang was dissatisfied with the result.

That had been an all-out attack. Even after drawing out 120 percent of the Temporary Strength Pill’s effects, he hadn’t managed to leave so much as a small wound on Jin Mukyung.

*The Tiger of Mount Heng could barely parry that.*

Even Cheol Mubaek, a fully mature Peak master, had suffered internal injuries and been forced to retreat in exchange for blocking it. So how had a brat not even thirty years old managed this?

“So you do live up to the name Heaven Shaking Sword?”

Jin Mukyung adjusted his stance and replied flatly.

“This much should be dodged.”

“It’s not as though you couldn’t block it, is it?”

A sneer appeared at the corner of Pung Yang’s mouth.

“Of course, a young master of the mighty Jin Family of Taiyuan would have been desperate enough to flee by rolling across the ground like a lazy donkey.”[^1]

Narye tagon. It was a phrase comparing someone to a lazy donkey rolling on the ground. To martial artists from prestigious orthodox factions who valued their dignity, it was practically the ultimate humiliation.

But not to Jin Mukyung.

“Donkey or mule, I don’t care. Does dignity put food on the table?”

“What?”

“Compared to the price of my life, it was cheap. Besides…”

The face that had remained impassive the entire time cracked into a quiet laugh.

“Why are you laughing?”

“Just thinking that if there are people who pelt Peak masters with rocks, rolling across the ground isn’t such a big deal.”

Pung Yang involuntarily asked in response to the nonsensical joke, unable to understand what he meant.

“Throwing rocks at a Peak master? Are they insane?”

“When I first heard about it, I thought the same thing. But after thinking it over, I realized he was exactly the kind of bastard who would do something like that.”

“I’d like to see the face of this lunatic.”

“You’ll see him soon.”

“What does that mean?”

That was when Pung Yang felt a faint sense of puzzlement.

Shiiiiing!

A sharp aura came from behind him.

He turned around, and the face of a handsome young man was reflected in his red eyes.

*The Sleeping Dragon of Shanxi.*

Within the slow flow of time, Jin Taekyung grinned. The iron spear in his hands was already hurtling toward Pung Yang’s chest.

KABOOM!

One Annihilation.

A vortex erupted from the spearhead and swallowed Pung Yang whole.

* * *

My condition was perfect. Leveling up while dealing with the minions had completely restored my fatigue and Stamina.

The timing was pretty good, too. Pung Yang’s broad, defenseless back looked like it was begging to be stabbed with a spear.

As the finishing touch to this beautiful picture, I chose One Annihilation. I hadn’t seen anyone remain fine after taking this attack.

But then…

“You should’ve picked your opponent more carefully before charging in.”

A low voice like the growl of a beast.

Pung Yang was surrounded by a curtain of qi as red as his eyes. It had completely blocked the vortex unleashed by One Annihilation, and now writhed like living armor.

*What did wuxia novels call something like this again?*

Oh, right. I remembered. I barely managed to move my lips.

“Body-Protecting Qi?”

“At least you’re not blind.”

“No, for fuck’s sake…”

Sword Energy and Sword Force weren’t enough, and now he had Body-Protecting Qi too?

As I stood there dumbfounded, the sight before my eyes going dark, Pung Yang curled up the corner of his mouth.

“It’s too late for regret.”

Whoosh!

A strand of saber qi shot up from his curved saber and sliced off a clump of my hair. I had bent at the waist just in time. If I had been even slightly slower, it would have been my head that was cut off.

*Fuck.*

I swallowed the curse trying to burst out and leaped away. No sooner had I done so than savage saber strikes shredded the place where I had been standing.

Shh-shh-shh-shhk!

The problem was that every strand of saber qi was unbelievably powerful. Seeing the frozen ground split apart like soft tofu sent a chill down my spine.

*If I make one wrong move, I’m really going to die.*

Even an A-rank magic armor wouldn’t have been enough here, yet I was fighting while wearing nothing but a scrap of cloth. It was like walking across a sheet of thin ice.

More than anything else…

*Doesn’t that bastard ever get tired?*

Maintaining Body-Protecting Qi alone had to consume a massive amount of internal energy, but Pung Yang seemed like a spring that would never run dry.

“I heard you two were brothers, but the way you run away like rats is exactly the same.”

That was when a voice came from behind him.

“It’s not exactly a pleasant thing to hear.”

Jin Mukyung appeared out of nowhere and scattered a flurry of sword strikes. A long blue flash shot toward Pung Yang’s neck.

Clang!

But even Jin Mukyung’s Sword Energy, which seemed capable of cutting through anything, couldn’t pierce the Body-Protecting Qi. Pung Yang leisurely rubbed the neck struck by the Sword Energy.

“It’s a little stiff. Is that all?”

“Of course not.”

Shiiiiing!

As Jin Mukyung charged in without hesitation, the curved saber in Pung Yang’s hand moved at the same time. The aura was so powerful that I could feel the flow of the air change.

This wasn’t a fight I could join.

Whoosh!

At last, the moment Jin Mukyung’s blue Sword Energy met Pung Yang’s red saber qi, a tremendous wave of force erupted along with a boom loud enough to make my ears ring.

KABOOM!

Most of the people standing firmly on both feet lost their balance and staggered.

But I widened my eyes and watched the result of this incredible clash.

*Which one?*

Through the dust swirling from the impact, I saw two people facing each other.

A sword and saber reduced to nothing but their hilts. Tightly pressed lips.

Pung Yang was the first to break the brief silence.

The man kneeling on the ground spat out dark red blood.

“Urgh—bleeeargh!”

A small cheer rose through the battlefield. Jin Mukyung stood proudly while Pung Yang knelt on the ground. The winner of this fierce battle had been decided.

*We won.*

I hadn’t been able to see the entire exchange, but there was no doubt that Pung Yang had suffered internal injuries first.

The proof was the distinct palm print stamped across his chest—something that hadn’t been there before. That must have been the decisive blow.

“Cough, cough.”

Pung Yang wiped the blood from the corner of his mouth and staggered to his feet.

“Striking the Ox Across the Mountain.[^2] Even so, I never expected my Body-Protecting Qi to break so easily… Was my enlightenment lacking?”

When Jin Mukyung gave him no answer, Pung Yang clicked his tongue.

“Damn it. Even after using the Temporary Strength Pill, I’ve ended up like this. I suppose I should hole up in some remote mountain valley and train my martial arts for a while.”

“A remote mountain valley? Training?”

I was genuinely curious.

“Where are you going?”

“Wait, and you’ll find out soon enough. I plan to take you brothers with me, too.”

This was pretty awkward.

Since we’d been invited to a housewarming, should I at least bring a box of tissues?

“Uh, us?”

“Yes. I need the martial arts formulas you know from the Jin Family of Taiyuan. They should be a great help in supplementing the violent qi circulation of the Crimson Blood Cultivation Technique.”

After hearing that much, the words that had been lingering on the tip of my tongue came out on their own.

“Are you, by any chance, a lunatic?”

I hadn’t checked, but everyone probably wore the same expression I did.

The battle had already clearly decided its winner, and yet—what?

“Forget your remote mountain valley training. I’ll send you on a filial-piety tour of Mount Beimang. You can train there.”[^3]

“Mount Beimang? You think you can send me there?”

“Even if it isn’t me personally, there are plenty of people behind you who can send you to Mount Beimang.”

I jerked my chin toward the people behind him.

The martial artists of the Mount Heng Sword Sect were already approaching slowly, weapons drawn.

The beautiful woman among them, glaring at him with especially venomous hatred, had to be the Mount Heng Sword Sect’s new Sect Leader, Lee Seowol.

*This man isn’t going to get an easy death.*

It was time for him to pay for the karma of his past misdeeds. I flicked my spear toward Pung Yang.

“Are you still going to keep spouting nonsense?”

The bastard stared at us for a moment before opening his mouth.

“Perhaps you’re under a serious misconception.”

The laugh in his voice was impossible to hide.

“Is there anyone among you capable of defeating me?”

“What the fuck does that even—”

“If you find that hard to believe, it would be faster to ask the Heaven Shaking Sword standing before me. Well, what do you think of what I’ve said?”

Jin Mukyung didn’t answer Pung Yang’s question, and only then did I realize it.

Why he hadn’t said a word for some time. Why he had done nothing but stand in place like a stone statue.

Tap.

Pung Yang’s hand touched Jin Mukyung’s chest. At what point had it happened? His body had already lost consciousness, and now it crumpled limply.

Only then did I see the five throwing knives embedded in his upper body in a neat row.

Thud.

The red eyes sweeping across the silent crowd curved like crescent moons.

“Well, shall we finish things up?”

* * *

The “finishing” began quickly.

It started with the more than ten throwing knives that shot from Pung Yang’s sleeve as he approached us at an easy pace.

Whoosh! Thunk-thunk-thunk!

It might have been a close-range attack, but it was a throwing-knife technique that even Jin Mukyung hadn’t been able to evade. Pung Yang’s knives pierced their targets with perfect accuracy, and screams rang out without fail.

“Urgh.”

“Guhk!”

The martial artists of the Mount Heng Sword Sect were already at the limit of their endurance, and their individual martial prowess wasn’t particularly high, making them easy prey.

By the time I finally stepped in front of Pung Yang, more than ten of them had already lost their lives.

“Stop.”

He shook his head.

“No, that’s not how it works. An order is a right reserved for the strong.”

“…I’ll kill you.”

“I could see it if you were the Heaven Shaking Sword, but a wet-behind-the-ears fledgling like you dares?”

I closed my mouth at Pung Yang’s sneer. He wasn’t wrong. My decision to block him had been half courage and half foolhardiness.

*But how do I take him down?*

My mind felt like it was burning itself blank. Amid all the tangled thoughts, two faces surfaced.

The first was the Head Elder. He had been the most powerful and despair-inducing opponent I had ever faced. But back then, I’d had Jin Wikyung and the martial artists of the Jin Family to help me.

*What about now?*

No one. I had no one.

After taking the Temporary Strength Pill, Pung Yang had to be a master comparable to, or even stronger than, the Head Elder. And the only person left to face him was me.

That naturally brought the second person to mind.

*Jopil, One Question, One Kill.*

Perhaps Jopil was the person who had forced me to face a genuine crisis. For the first time, I’d lost one of the subordinates I’d gained in the Murim, and I’d nearly died. Only after that had I managed to defeat the bastard.

But the Pung Yang standing before me was on an entirely different level from Jopil.

*This goddamn Temporary Strength Pill…*

The more I thought about it, the more curses came out. I wanted to see the face of whatever son of a bitch had made it.

“Once you’ve learned your place, curl up quietly.”

Watching Pung Yang act like the greatest master under heaven simply because he trusted that pill twisted my gut. If he’d only been around Jopil’s level, I might have found a way to deal with him…

*…Wait.*

A forgotten fact suddenly flashed through my mind.

There had been something nasty among the things Jopil possessed. What was it again?

*The Blazing Flame Divine Pill.*[^4]

A peerless divine elixir that granted half a jiazi of internal energy when consumed—but was also a double-edged sword that could kill its user through the fire qi contained within it.[^5]

*The Blazing Flame Divine Pill. The Blazing Flame Divine Pill…*

The next moment, I abruptly opened my mouth.

“Hey.”

Pung Yang, who had already passed me, stopped and turned around.

“Hey? Were you talking to me?”

“Yeah, you pill-popping bastard.”

“Hah. What did this little brat just say…?”

“Did you enjoy being the only one popping pills?”

“…What?”

I looked straight at his face, mottled with bewilderment and fury, and enunciated each word.

“I asked if you enjoyed taking pills all by yourself.”

An eye for an eye. Doping for doping.

Now I was going to pop a pill and fight, too.

You bastard.

[^1]: *Narye tagon* literally compares someone to a lazy donkey rolling on the ground. For martial artists from prestigious orthodox factions, it implies humiliatingly abandoning dignity to survive.

[^2]: A martial-arts term describing force that passes through one object to strike another behind it.

[^3]: Mount Beimang is traditionally associated with burial grounds and the dead; sending someone there is a euphemism for killing them.

[^4]: The name literally combines “blazing flame” with “divine pill,” emphasizing the elixir’s dangerous fire qi.

[^5]: A *jiazi* is a sixty-year cycle; half a jiazi is thirty years.
```
