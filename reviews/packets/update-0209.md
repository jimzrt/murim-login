<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0209.txt",
      "sha256": "6847f722af6b06a8e2ae868f1c6e199949ade11f166c0bee3da9b7b2fcaab0d8",
      "bytes": 13369
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "46aa5ce10b24dcde4ae08553407a2171d8d840b42d78ab300e1d0a9427ca506f",
      "bytes": 3690
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "0d3c448b289709efa528a4644e975450aeb1b2e9ff0e1f0c455499ddb86af2a6",
      "bytes": 54192
    },
    {
      "path": "characters/Im Chunsoo.md",
      "sha256": "baf1dc33a9795e07a5a5f64ad06185614b36cb2b85a11d2225264cff208dea9b",
      "bytes": 807
    },
    {
      "path": "characters/Im Kkeokjeong.md",
      "sha256": "fff9fb4603f5809466d381dd8b9c71062d42bdc0456037b6266f83b8d87ca2e0",
      "bytes": 1608
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "cd34c72be2fb72ce2fc04a12dfa3238a461ca73b26ed3903bf34bf9dbc424258",
      "bytes": 27592
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "9c1f5d2fbe5230970dd9a75ba6172c262c78af9dc9dec2fe1a5bb5aaf4a9678e",
      "bytes": 622
    },
    {
      "path": "characters/Song Song.md",
      "sha256": "f683a6c6edcc1f51bbe6e31b5fa4da3c30f30edaada9f09354900117ab7327e3",
      "bytes": 539
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "a3c1c983e6f9bc2c79c86bc1fcd8645adefd8c557a1a4a9f81a9dd4b23bab3fa",
      "bytes": 47138
    }
  ],
  "estimated_tokens": 35807
}
-->

# Durable State Update — Chapter 209

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 209. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 20 concise items, `open_questions` to at most 8
items, and `temporary_decisions` to at most 8 items. Keep the serialized context
under 16384 UTF-8 bytes. Use only chapter
numbers through 209. `profile_updates` may replace one exact, uniquely occurring
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
  "chapter": 209,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 209,
    "continuity_sources": [209],
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
    "One Step Back granted Taekyung two level-ups and 20 Bonus Points.",
    "Jeok Cheongang selected three Scorching Yang Qi elixirs for Taekyung's Fire Gate Clan training and successfully opened Taekyung's Conception and Governor Vessels.",
    "Taekyung is publicly recognized as Jeok Cheongang's Disciple and heir to the Fire Gate Clan's orthodox lineage.",
    "Jin Mukyung remains secluded in the training hall and has not returned to Heaven's Gate Temple.",
    "The Jin Family received an invitation to the Star-Array Grand Banquet in Henan.",
    "Seong Jinho is staying at Taekyung's new family home after losing his housing deposit to Kim Jong-su.",
    "Taekyung remains officially registered as a C-rank Hunter belonging to Hope Guild.",
    "A Gate previously caused casualties at Uldae-ri, Jangheung-myeon, Yangju City; Hunters and the military reported exterminating fifty-eight goblins.",
    "An unidentified black sphere destroyed Mr. Park's taxi, but Taekyung rescued him.",
    "A Gate opened on a congested commute roadway near Hwang Cheol Soo's tollgate.",
    "The System forcibly accepted the Peak-Grade Gate Suppression Quest.",
    "The Gate released ten B-rank ogres after widening, overwhelming the tollgate Hunter team.",
    "Opening the Conception and Governor Vessels greatly increased Taekyung's control and explosive power over his internal energy and heightened his senses.",
    "Taekyung defeated more than ten B-rank ogres, including a Lv.85 Ogre, and gained at least one Level.",
    "Taekyung blocked an arriving military Hunter team from taking the remaining ogres and collected their valuable parts.",
    "The tollgate incident caused four deaths and five severe injuries; an F-rank Gate near Yangju City had caused ten deaths and more than twenty severe injuries earlier that day.",
    "Government personnel acknowledged that Gate casualties were being downplayed and concealed.",
    "Reporter Kim learned Taekyung's identity and C-rank status while preparing a newspaper report about the tollgate incident.",
    "Taekyung realized he was late for work at Hope Guild."
  ],
  "continuity_sources": [
    208
  ],
  "open_questions": [
    "What are the rewards for the Conception Vessel Opening Achievement and the rare Achievement earned after completing the Conception and Governor Vessels Quest?",
    "Will Jin Mukyung return to Heaven's Gate Temple before the appointed deadline?",
    "What event does Jeok Cheongang believe may occur sooner than expected, and why must he endure for several more years?",
    "What is the true condition of the absent Martial God?",
    "Will Taekyung attend the Star-Array Grand Banquet, and what exactly was the answer that changed the three men's expressions?",
    "What are the Reward and Failure conditions of the Gate Suppression Quest?",
    "How will the Gate near Hwang Cheol Soo's tollgate ultimately be contained, and what further monsters may emerge?",
    "Will Reporter Kim's coverage expose Taekyung's identity and C-rank status publicly?"
  ],
  "safe_through": 208,
  "temporary_decisions": [
    "Render 혈도 타통 as “Acupoint Opening.”",
    "Render 회음혈 as “Huiyin Acupoint.”",
    "Render 임맥 타통 as “Conception Vessel Opening.”",
    "Render 성라대연 as “Star-Array Grand Banquet.”",
    "Render 노야 as “Old Master” when Taekyung addresses Jeok Cheongang privately.",
    "Render 고시원 as “goshiwon” and 오피스텔 as “officetel.”",
    "Render 오우거 as “ogre” and 게이트 진압 as “Gate Suppression.”",
    "Render 상도의 as “professional courtesy.”"
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
| 대연무장 | **Grand Training Ground** | The Jin Family's largest training ground and the site of the grand banquet. |
| 주모 | **Lady of the House** | Title used in Wipeng's remark that Jin Wikyung lacks a wife or household mistress. |
| 일장로 | **First Elder** | Title Cheol Mubaek claims within the Mount Heng Sword Sect. |
| 이대 문주 | **second Sect Leader** | Lee Seowol's succession title as the Mount Heng Sword Sect's second Sect Leader. |
| 디그다 | **Diglett** | Pokémon species used in Taekyung's analogy. |
| 닥트리오 | **Dugtrio** | Pokémon species used in Taekyung's analogy. |
| 언더아머 | **Under Armour** | Modern sportswear brand mentioned in Taekyung's joke. |
| 추도환 | **Choo Dohwan** | Level 65 Iron Blood Sect martial artist known as the Iron Fist. |
| 철권 | **Iron Fist** | Choo Dohwan's epithet. |
| 상도문 | **Sangdo Sect** | Sect pledging itself to the Jin Family at the banquet. |
| 황진수 | **Hwang Jinsu** | Level 25 challenger from Hwang Family Manor. |
| 황가장 | **Hwang Family Manor** | Family estate represented by Hwang Jinsu. |
| 갈 모 | **Gal Mo** | Nameless wandering martial artist who challenges Chulwoo. |
| 한 남자가 있어, 널 너무 사랑한 | **There Is a Man Who Loved You So Much** | System Quest title generated by Chulwoo's jealous challenge. |
| 나약한 수컷 | **Weak Male** | System Title granted if Jin Taekyung refuses the Quest. |
| 화산제일의 기재 | **Huashan’s greatest prodigy** | Reputation attributed to Baek Museong; Taekyung privately mocks the title. |
| 연쇄고백마 | **Serial Confession Man** | Taekyung's mocking description of Chulwoo after the duel. |
| 대종남파 | **Great Zhongnan Sect** | Expanded and formal reference to the Zhongnan Sect. |
| 사자후 | **lion's roar** | Taekyung's term for Song Il's crowd-shattering roar. |
| 육합전성 | **Six-Harmonies Voice Transmission** | Supreme Peak martial art that transmits the user's voice from every direction. |
| 천하삼십육검 | **Heavenly River Thirty-Six Swords** | Zhongnan Sect sword technique used by Song Il. |
| 열화문의 신물 | **Fire Gate Clan’s sacred treasure** | The Unnamed Sword entrusted by Jeok Cheongang to Jin Taekyung. |
| 종남산 | **Mount Zhongnan** | Mountain where the Zhongnan Sect’s main sect is located. |
| 혀왕 | **Tongue King** | Taekyung’s joking nickname for Jeok Cheongang after his verbal intimidation. |
| 피독지환 | **Poison-Averting Ring** | Clear-jade ring offered to Jeok Cheongang as a gift. |
| 마이클 천강 | **Michael Cheongang** | Taekyung’s joking nickname for Jeok Cheongang during the banquet. |
| 양천상회 | **Yangcheon Merchant Association** | Merchant association whose owner seeks Jeok Cheongang’s help with the Hebei Peng Family. |
| 철혈도 | **Iron Blood Saber** | Epithet of Peng Cheolyeong. |
| 팽철영 | **Peng Cheolyeong** | Family Head of the Hebei Peng Family and successor to the Thunderbolt Saber King. |
| 화천검 | **Fire Heaven Sword** | The true name of the former Unnamed Sword; beloved sword of the Fire Gate Clan's tenth Sect Leader. |
| 볼케이노문 | **Volcano Gate Clan** | Taekyung's joking nickname and pun for the Fire Gate Clan; not a separate sect. |
| 석가장 | **Seok Family Manor** | Prominent merchant family and estate described as foremost in the merchant world. |
| 사천당문 | **Sichuan Tang Clan** | Martial clan cited for its poison-based cleansing method. |
| 아마존 | **Amazon** | Region referenced in Taekyung's crude joke. |
| 블랙 아나콘다 | **Black Anaconda** | Snake referenced in Taekyung's crude joke. |
| 악불군 | **Ak Bulgun** | Spear Instructor at Heaven's Gate Temple from the Shandong Yue Family. |
| 산동악가 | **Shandong Yue Family** | Family to which Ak Bulgun belongs. |
| 적통 | **orthodox lineage** | The legitimate succession of the Fire Gate Clan's tradition. |
| 구음절맥 | **Nine Yin Severed Meridians** | Rare severed-meridian condition caused by powerful innate yin energy and associated with an early death. |
| 닥터 최태 | **Doctor Choi Tae** | Taekyung’s joking doctor label for Jeok Cheongang. |
| 하 총관 | **Chief Ha** | Surname-and-office form; one of Seok Family Manor's five Outer Stewards. |
| 외총관 | **Outer Steward** | Senior administrative office at Seok Family Manor. |
| 일보 후퇴 | **One Step Back** | Peak-Grade Quest requiring Jin Taekyung to make Jeok Cheongang retreat one step. |
| 탄지공 | **finger-flicking technique** | Head Elder's internal-energy technique, used as a comparison for the stone projectiles. |
| 천마 | **Heavenly Demon** | Demonic title used in Jeok Cheongang's impossible comparison. |
| 천룡 | **Heavenly Dragon** | The ideal form Jeok Cheongang wishes Taekyung to become. |
| 화령초 | **Fire Spirit Grass** | Scorching Yang Qi elixir consumed by Taekyung. |
| 홍화초 | **Red Flower Grass** | Scorching Yang Qi elixir consumed by Taekyung. |
| 염적초 | **Flame Red Grass** | Scorching Yang Qi elixir consumed by Taekyung. |
| 설삼 | **snow ginseng** | Elixir compared with the chapter's three selected roots. |
| 혈도 타통 | **Acupoint Opening** | System Quest created when Taekyung consumes the three elixirs. |
| 회음혈 | **Huiyin Acupoint** | Starting acupoint of the Conception Vessel; its location causes Taekyung particular danger during forced opening. |
| 임맥 타통 | **Conception Vessel Opening** | System Achievement earned after Taekyung opens the Conception Vessel. |
| 성라대연 | **Star-Array Grand Banquet** | Major martial gathering held in Henan every two or three years. |
| 김종수 | **Kim Jong-su** | Jinho's college classmate who absconded with his housing deposit. |
| 제주도 | **Jeju Island** | Referenced in Taekyung's joke about Jinho being a premium-grade sucker. |
| 희망 길드 | **Hope Guild** | Guild to which Taekyung officially belongs; it provides him an officetel. |
| 양주시 | **Yangju City** | Location of the reported F-rank Gate. |
| 장흥면 | **Jangheung-myeon** | Administrative area containing Uldae-ri. |
| 울대리 | **Uldae-ri** | Village where the reported F-rank Gate appeared. |
| 노스트라다무스 | **Nostradamus** | Referenced as someone who could not predict Gate formation. |
| 고블린 | **goblin** | Monster species reported at the F-rank Gate. |
| 황철수 | **Hwang Cheol Soo** | B-rank public-service Hunter and tollgate team leader. |
| 박 씨 | **Mr. Park** | Taxi driver rescued by Taekyung; surname address form. |
| 오우거 | **ogre** | B-rank monster species emerging from the Gate. |
| 유시진 | **Yoo Sijin** | Captain and Team Leader of Support Team 25. |
| 유 대위 | **Captain Yoo** | Rank-and-surname form used for Yoo Sijin. |
| 김 기자 | **Reporter Kim** | Military correspondent assigned to cover the Gate incident. |
| 정 팀장 | **Team Leader Jeong** | Hunter Team Leader serving with the military support team. |
| 대위 | **captain** | Military rank held by Yoo Sijin. |
| 군종 기자 | **military correspondent** | Reporter Kim's military reporting role. |
| 수방사 | **Capital Defense Command** | Abbreviation used for 수도방위사령부. |
| 수도방위사령부 | **Capital Defense Command** | Military command to which the support team belongs. |
| 25 지원팀 | **Support Team 25** | Military and Hunter support unit at the tollgate. |
| 특전사 | **Special Forces** | Military force whose uniform is worn by one of the support-team personnel. |
| 페더 폴 | **Feather Fall** | Descent-slowing spell used by the arriving mage. |
| 그리스 | **Grease** | Spell used to make the ogres lose their footing. |

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
| 공야청 | 진태경 | survivor_guardian_to_benefactor | Young Hero Jin | formal-polite | Gong Yacheong greets Taekyung as 진 소협 after returning to the Jin Family. |
| 소율 | 진태경 | child_survivor_to_benefactor | Uncle | childlike-familiar | Soyul repeatedly calls Taekyung 아저씨 while asking to see him. |
| 청풍 | 백무성 | Martial_Uncle_to_Martial_Nephew | Martial Nephew | affectionate-casual | Cheongpung accepts Baek Museong's apology by calling him 사질. |
| 진태경 | 백무성 | junior_martial_artist_to_Huashan_elite | Young Hero Baek | formal-polite | Taekyung addresses Baek Museong as 백 소협 while asking to change seats. |
| 진위경 | 이소월 | host_to_new_sect_leader | Young Lady | formal-polite | Jin Wikyung addresses Lee Seowol as 소저 before accepting her oath. |
| 이소월 | 진위경 | new_sect_leader_to_lesser_family_head | Lesser Family Head | formal-deferential | Lee Seowol refers to Jin Wikyung as 소가주님 when describing his summons. |
| 철무백 | 진위경 | sect_elder_to_lesser_family_head | Lesser Family Head | formal-deferential | Cheol Mubaek formally greets Jin Wikyung as the Lesser Family Head of the Jin Family of Taiyuan. |
| 무인 | 진위경 | vassal_martial_artist_to_lesser_family_head | Lesser Family Head | formal-deferential | The Mount Heng martial artists greet Jin Wikyung as 소가주님 while pledging loyalty. |
| 진태경 | 이소월 | young_martial_artist_to_allied_sect_leader | Young Lady Lee | formal-polite | Taekyung uses 이 소저 while greeting Seowol at the banquet. |
| 진위경 | 철우 | Jin_Family_host_to_visiting_martial_artist | Defeated Flower Fist | formal-familiar | Wikyung uses Chulwoo's epithet while asking Taekyung why he is acting strangely. |
| 진위경 | 추도환 | banquet_host_to_visiting_challenger | Young Hero Choo | formal-polite | Wikyung uses 추 소협 while accepting Choo Dohwan's request for a duel. |
| 백무성 | 진위경 | visiting_martial_artist_to_lesser_family_head | Great Hero Jin | formal-polite | Baek Museong uses 진 대협 while urging Jin Wikyung to stop the duel. |
| 청풍 | 철우 | martial_uncle_to_martial_nephew | Martial Nephew Chulwoo | affectionate-casual | Cheongpung addresses Chulwoo as his Martial Nephew while assessing Taekyung's speed. |
| 하급 무인 | 진태경 | junior_martial_artist_to_Third_Young_Master | Third Young Master | formal-deferential | The low-ranking gate martial artist uses the family title while reporting Taekyung's victory. |
| 하급 무인 | 혁무진 | subordinate_to_captain | Captain | deferential | The low-ranking gate martial artist addresses Hyuk Mujin while discussing the celebration and visitors. |
| 진위경 | 송일 | Jin Family host to visiting Zhongnan Elder | Senior | formal and guarded | Jin Wikyung respectfully asks Song Il's name before the dispute escalates. |
| 백무성 | 송일 | junior Huashan disciple to Zhongnan Elder | Senior Song | formal-deferential | Baek Museong introduces himself as a junior of Murim and pays respects. |
| 송일 | 백무성 | Zhongnan Elder to younger Huashan elite | Huashan's Lone Crane | condescending and dismissive | Song Il questions Baek Museong's identity and belittles his martial standing. |
| 백무성 | 공일혁 | senior martial artist to hostile Zhongnan junior | Great Hero Gong | formal but admonishing | Baek warns Gong Ilhyuk to watch his words after Gong threatens Taekyung. |
| 송일 | 진태경 | hostile Zhongnan Elder to accused outsider | you / Jin Taekyung | hostile and threatening | Song Il questions Taekyung's identity and later threatens him over Gong Ilhyuk's injury. |
| 송일 | 청풍 | hostile Zhongnan Elder to younger martial artist | Sword Saint's heir / you | hostile and threatening | Song Il identifies Cheongpung as the Sword Saint's heir and demands that he face the consequences of injuring Gong Ilhyuk. |
| 송일 | 적천강 | former rescued junior to former rescuer | Great Hero Jeok | formal, fearful, and defensive | Uses 적 대협 while insisting that Jeok has no business interfering in the dispute. |
| 적천강 | 송일 | former rescuer to former rescued junior | Zhongnan brat; you; insolent bastard | blunt, mocking, and humiliating | Jeok recalls Song's youthful arrogance and addresses him with contempt while publicly disciplining him. |
| 종남삼수 | 노호검객 | junior_Zhongnan_martial_artists_to_sect_elder | Elder | fearful-deferential | The Three Hands of Zhongnan plead with Song Il after he blames them for his humiliation. |
| 노호검객 | 공일혁 | Zhongnan_elder_to_junior_martial_artist | worthless piece of trash | furious and contemptuous | Song Il blames Gong Ilhyuk for inciting the confrontation and threatens him. |
| 진위경 | 적천강 | host_to_legendary_guest | Great Hero Jeok | formal-deferential | Introduces himself and pays respects to Jeok Cheongang as the Fire King. |
| 적천강 | 진위경 | elder_to_younger_family_head | you | gruff and teasing | Uses 자네 while mistaking Wikyung for Taekyung’s father and questioning his age. |
| 상인 | 적천강 | merchant_to_legendary_martial_master | Great Hero Jeok | deferential and flattering | Praises Jeok Cheongang while presenting the Poison-Averting Ring and requesting help. |
| 적천강 | 상인 | legendary_guest_to_merchant | you | blunt and transactional | Cuts off the merchant’s praise, asks his identity and origin, and accepts the gift without committing to the requested favor. |
| 적천강 | 악불군 | protective elder to outsider touching Taekyung | Take your hand off what’s mine | blunt and threatening | Jeok interrupts Ak Bulgun when he places a hand on Taekyung's shoulder; this does not confirm Taekyung as his Disciple. |
| 악불군 | 적천강 | junior_martial_artist_to_legendary_master | Great Hero Jeok | formal-deferential | Ak Bulgun addresses Jeok Cheongang respectfully while explaining Heaven's Gate Temple's offer. |
| 악불군 | 진태경 | academy_instructor_to_young_martial_artist | Young Hero Jin | formal-polite | Ak Bulgun repeatedly addresses Taekyung as 진 소협 while discussing the academy opportunity and apologizing after Jeok's declaration. |
| 진위경 | 하 총관 | host_to_merchant_representative | Chief Ha | formal-polite | Jin Wikyung addresses Seok Family Manor's Outer Steward by surname and office. |
| 하 총관 | 진위경 | merchant_representative_to_lesser_family_head | Lesser Family Head | deferential | Chief Ha repeatedly addresses Jin Wikyung as 소가주님 while seeking cooperation and a favor. |
| 악불군 | 진위경 | visiting_instructor_to_lesser_family_head | Lesser Family Head | formal and blunt | Ak Bulgun uses 소가주 while asking why Jin Wikyung summoned him and warning him about Heaven's Gate Temple's regulations. |
| 진위경 | 악불군 | host_to_visiting_instructor | Sir Ak | formal-polite | Jin Wikyung welcomes Ak Bulgun, explains Jin Mukyung's refusal to return, and personally delivers the Heaven's Gate Temple letter. |
| 진태경 | 악불군 | young_martial_artist_to_Heaven's_Gate_Instructor | Sir Ak | formal-polite | Taekyung addresses Ak Bulgun as 악 대협 while asking why he remains at the Jin Family. |
| 진태경 | 박 씨 | Hunter passenger to taxi driver | Sir | polite-commanding | Taekyung orders Mr. Park to flee and warn others after the Gate opens. |
| 박 씨 | 진태경 | taxi driver to passenger | passenger | startled-polite | Mr. Park recognizes Taekyung as the Hunter passenger who rescued him. |
| 김 기자 | 유시진 | military_correspondent_to_captain | Captain Yoo | formal and familiar | Calls him 유 대위님 while greeting him at the incident scene. |
| 김 기자 | 정 팀장 | reporter_to_hunter_team_leader | Team Leader Jeong | familiar and teasing | Greets him as 정 팀장 and complains about his prickly response. |
| 정 팀장 | 김 기자 | hunter_team_leader_to_military_correspondent | Reporter Kim | blunt and irritated | Says he was avoiding Reporter Kim and criticizes his excitement over the scoop. |
| 유시진 | 정 팀장 | captain_to_support_team_leader | Team Leader Jeong | blunt-commanding | Uses 정 팀장아 while questioning him about the relative severity of the two Gate incidents. |
| 유시진 | 김 기자 | captain_to_military_correspondent | Reporter Kim | formal and admonishing | Uses 김 기자님 while warning him to behave appropriately at the accident scene. |
| 김 기자 | 진태경 | reporter_to_hunter_subject | Hunter Jin Taekyung | formal and probing | Uses 진태경 헌터님 while confirming Taekyung's identity and questioning his rank. |

## Exact glossary matches

| 진태경    | **Jin Taekyung**   |
| 송송이    | **Song Song**     |
| 임춘수    | **Im Chunsoo**    |
| 전음     | **Sound Transmission**                           | Fixed skill terminology; preserve the internal-energy mechanism when the source explains it, but do not add an explanation where it does not |
| 장비               | **Equipment**                  |
| 헌터      | **Hunter**            |
| 게이트     | **Gate**              |
| 몬스터     | **monster**           |
| 레이드     | **raid**              |
| 길드      | **Guild**             |
| 길드장     | **Guild Master**      |
| 팀장      | **Team Leader**       |
| 마법사     | **mage**              |
| 대격변     | **Great Cataclysm**   |
| 임꺽정 | **Im Kkeokjeong** |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 하연 | **Hayeon** | Jin Taekyung’s younger sister |
| 평화 | **Peace Guild** | Guild name. |
| 부천 | **Bucheon** | City with a dense concentration of Gates and Guild headquarters. |
| 패밀리어 | **Familiar** | System classification for the flies detected in Taekyung's home. |
| 대리 | **Assistant Manager** | Corporate title used by Kim Seonhee |
| 송이 | **Song-i** | Short form used for Song Song; Taekyung's love interest. |
| 오우거 | **ogre** | B-rank monster species emerging from the Gate. |

## Listed compact profiles

### Im Chunsoo.md

# Im Chunsoo (임춘수)

- **Safe through:** Chapter 101
- **Aliases:** Frozen
- **Role:** Level 75 A-rank Hunter; founder and Guild Master of Sangdong Guild; renowned ice mage who personally confronted Jin Taekyung; former Class 25 trainee at the Hunter Training Center under Class 3 instructor Kim Hwajong
- **Personality:** Intimidating, severe, and extremely short-tempered, though he has tried to moderate his temper with age
- **Voice:** Sharp and commanding, with a comparatively gentle tone when deliberately controlling his temper; becomes violently profane when enraged
- **Relationships:** Father of Im Changsoo, whom he considers a pathetic disappointment and immediately fires and punishes after learning of Changsoo's actions

### Im Kkeokjeong.md

# Im Kkeokjeong (임꺽정)

- **Safe through:** Chapter 86
- **Aliases:** Im Hyeokjun; Kkeokjeong hyung; Uncle Kkeokjeong
- **Role:** E-rank Hunter; veteran tank in the Peace Guild’s Gate party and current member of the Peace Guild
- **Personality:** Good-natured, sociable, modest about his family, and shamelessly confident about their age difference
- **Voice:** Hearty, casual, teasing, and quick to laugh
- **Relationships:** An old acquaintance of Jin Taekyung from the Ilsan manpower office; calls Taekyung his little brother, recommends him to Team Leader Choi, and is married with two children

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 208
- **Aliases:** Sleeping Dragon of Shanxi
- **Role:** Modern-world protagonist; recently fired after seven years at his job; C-rank Hunter who defeated eight B-rank Minotaurs and killed a Level 70 B-rank Minotaur Warrior in one blow; Peak Master with forty-five years of internal energy and the Scorching Yang Qi attribute after fully absorbing the Blazing Flame Divine Pill; possesses Jopil’s Flame Divine Palm manual, whose cover Jeok Cheongang partly burned after Taekyung threw it during his escape, and the Fire Heaven Sword, formerly the Unnamed Sword, made from Ten-Thousand-Year Cold Iron; Jeok Cheongang falsely identified the sword in public as the Fire Gate Clan’s sacred treasure, then revealed that it is a former Fire Gate Clan Sect Leader’s beloved sword whose true power requires inheriting the Fire Gate Clan’s legacy; youngest son of the Jin Family of Taiyuan; new owner of a two-story detached house in Goyang intended for his family; Qi Sense reaches a seventy-meter radius; possesses one Temporary Strength Pill in his Inventory and has reserved it for a worst-case, life-threatening contingency; was Level 75 after completing the There Is a Man Who Loved You So Much Quest and One Step Back and receiving large EXP and Fame rewards, with 20 unallocated Bonus Points after the latter Quest; has since gained at least one additional Level while defeating more than ten B-rank ogres, including a Lv.85 Ogre, at the Gate; has allocated all seventy remaining stat points, twenty to Strength and fifty to Agility; completed the Find the Master Artisan Quest after securing Jang Taebo’s agreement to forge his Ten-Thousand-Year Cold Iron into a spear; can roughly copy observed martial forms and copied the Plum Blossom Fist after three days of sparring with Cheongpung; killed Jin Baekyang, the Blade of Flowers, and was rendered unconscious with an Internal Injury by Jeok Cheongang’s Flame Divine Palm; narrowly evaded Song Il’s Heavenly River Thirty-Six Swords before Jeok stopped Song and publicly revealed that Taekyung holds the entrusted Fire Gate Clan sacred treasure; spent two days bedridden with severe bruising after Jeok Cheongang beat him with his bare fists over the partly burned manual, then underwent an abbreviated cleansing treatment while unconscious that increased his Muscles and Bones and Sinews and Meridians by 5 each and his Strength, Stamina, and Agility by 1 each; has practiced martial arts for only three months, advancing from Third Rate to the beginning of the Peak realm during that period; was publicly accepted by Jeok Cheongang as his Disciple and declared heir to the Fire Gate Clan’s orthodox lineage, a status that ended his path to Heaven’s Gate Temple and other masters; Jeok Cheongang identifies him as possessing the Heavenly Martial Physique and agrees to personally oversee his martial-arts training until he reaches a certain level, while Taekyung addresses him as Master and, when they are alone, Old Master; completed the Peak-Grade One Step Back Quest after Jeok agreed to defend only and Taekyung used One Annihilation to force him five steps backward, then collapsed from exhausting all his strength and internal energy while Jeok supported him with internal energy; consumed Fire Spirit Grass, Red Flower Grass, and Flame Red Grass, completed the forced Acupoint Opening Quest, and successfully opened both his Conception and Governor Vessels before losing consciousness from exhaustion; blocked an arriving military Hunter team from taking the remaining ogres and personally butchered and collected their valuable parts.
- **Personality:** Hungry, self-aware, dryly observant, and willing to take a questionable opportunity when desperate; treats the impossible as a game until the danger becomes undeniable
- **Voice:** First-person, conversational, dryly self-mocking; uses vivid trap-and-prey imagery, game jargon, and occasional profanity
- **Relationships:** Jin Mukyung’s younger brother and current student; son of a deceased father; supports his mother and younger sibling; loves Song Song; has a strained relationship with Lee Seowol, the current Sect Leader of the Mount Heng Sword Sect, whose marriage proposal he has decided to reject; is publicly recognized as Jeok Cheongang’s Disciple and heir to the Fire Gate Clan’s orthodox lineage, and has begun undergoing Jeok’s deliberate training after consenting to the dangerous attempt to open his Conception and Governor Vessels.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 208
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Song Song.md

# Song Song (송송이)

- **Safe through:** Chapter 85
- **Aliases:** Miss Song
- **Role:** Founding member of the Peace Guild; C-rank healer
- **Personality:** Calm, practical, capable, and attentive; speaks briefly and handles domestic work with practiced skill
- **Voice:** Calm, concise, polite, and capable of devastatingly blunt candor
- **Relationships:** Works alongside Team Leader Choi, Butler Kim, Im Kkeokjeong, and Jin Taekyung as a member of the Peace Guild

## Korean source

```text
＃209화



오전 열 시.

꿀맛 같은 휴가를 보내고 출근한 평화 길드의 D급 헌터 임꺽정은 입을 딱 벌렸다.

“헉, 이게 뭐야.”

그럴 만도 했다.

휴가 전, 그러니까 일주일 전만 하더라도 길드 하우스는 다 무너져 가는 동네 구멍가게였으니까.

하지만 지금 그의 눈앞에는 번쩍거리는 대리석과 고급스러운 폰트로 제작된 간판이 있었다.



<평화 길드>



“이야, 리모델링 끝장나게 했네.”

임꺽정이 감탄하며 외관을 구경 중이던 그때. 어디선가 익숙한 목소리가 들려왔다.

- 안 들어오고 뭐 하십니까?

화들짝 놀란 그가 주위를 둘러봤다. 하지만 그 흔한 CCTV나, 인터폰 하나 보이지 않자 조심스럽게 입을 열었다.

“최, 최 팀장? 최 팀장님 맞지?”

- 예. 접니다.

“뭐야, 이거. 뭐로 말하는 거야?”

마치 그 말만을 기다렸다는 듯, 한 치의 망설임 없는 대답이 들려왔다.

- 별거 아닙니다. 유서 깊은 이탈리아의 장인 가문인 베르체니에 의뢰를 넣어서 특별히 제작한 거죠. 메시지, 관찰, 경보 마법을 포함한…….

“아, 아냐. 거기까지 말 안 해 줘도 돼.”

- 아. 그럼 화염 내성이 있는 샐러맨더의 가죽으로 표면을 감싼 마호가니 문을 열고 들어오시면…….

“들어갈게! 지금 들어간다고!”

- ……예.

철컥.

어딘지 모르게 시무룩한 목소리와 함께 잠겨 있던 문이 스르륵 열린다.

외관만큼이나 엄청나게 바뀐 길드 하우스 내부에서 세 사람이 임꺽정을 기다리고 있었다.

“오셨습니까.”

“임 헌터님.”

“아저씨 왔어요?”

평화 길드의 실질적 주인이라 할 수 있는 최 팀장과 표면상 길드장을 맡고 있는 김 집사, 마지막으로 길드의 홍일점인 송송이까지.

원형 테이블에 빙 둘러앉은 세 사람이 차례대로 건네는 인사에 임꺽정이 사람 좋은 웃음을 흘렸다.

“오랜만에 봐서 그런가, 다들 반갑습니다. 휴가 동안 잘들 쉬셨고?”

말이 끝나기가 무섭게 세 사람의 표정이 묘하게 변했다.

잠깐의 침묵이 흐른 뒤 송송이가 입을 열었다.

“쉬긴 했어요. 집에 하도 벌레가 많아서 신경이 쓰이긴 했지만.”

“벌레?”

“네. 아저씨네 집에는 벌레 없었어요?”

송송이의 물음에 임꺽정이 고개를 갸웃했다.

그러고 보니 휴가 동안 아내가 비슷한 문제로 몇 번 짜증을 낸 것 같기도 하다.

“그냥 뭐, 파리 한두 마리 정도였지. 잡아도 잡아도 계속 들어온다길래 놔뒀더니 잠잠해지던데? 별로 날아다니지도 않고.”

“아, 그래요?”

“응. 그렇게 얌전한 파리는 처음 봤어.”

송송이가 으스스한 듯 치를 떨며 말했다.

“저는 얼마나 많은지 찝찝해서 샤워도 못 하겠더라고요. 꼭 벌레가 지켜보는 것 같아서.”

“벌레가? 으하하! 송 양은 농담도 잘해.”

“…….”

고개까지 젖히며 웃던 임꺽정은 보지 못했다.

자신을 제외한 나머지 세 사람이 의미심장한 눈빛으로 들리지 않는 말을 주고받는 것을.

‘임 헌터님은 모르는 것 같은데요?’

‘눈치 못 챘나 봅니다.’

‘와, 이 아저씨 너무 둔감한 거 아니에요?’

휴가 내내 상동 길드가 보낸 패밀리어의 감시를 받은 세 사람과는 달리, 임꺽정은 아무것도 모른 채 그야말로 꿀 같은 휴식을 취하고 왔다.

감시가 안 붙은 것이 아니다. 붙었지만 모르는 것뿐.

모르는 게 약이라는 말이 딱 어울리는 상황이었다.

“미친 변태 새끼들. 나중에 걸리면 불알을 잡아 뜯어 버려야지.”

상동 길드 소속의 마법사들이 들었다면 모골이 송연해질 만한 송송이의 중얼거림에, 껄껄 웃던 임꺽정이 웃음을 뚝 그쳤다.

“응? 방금 뭐라고 했어? 변태?”

“아니에요. 그냥 벌레들 징그럽다고요.”

“아직도 심해? 아는 사람이 그쪽 업체에서 일하는데, 한번 알아봐 줄까?”

순수한 걱정이 담긴 그의 말에 피식 웃은 송송이가 입을 꾹 다문 채 앉아 있는 두 사람을 가리켰다.

“이제는 다 없어졌어요. 저기 계신 두 분이 힘써 주셨거든요. 특히 김 집사님.”

“그래? 김 형, 아니 길드장님이 그런 쪽에도 조예가 있으신 모양이네.”

김 집사가 어색하게 웃으며 대답했다.

“아닙니다. 마침 저도 아는 후배가 그쪽이라.”

“아아. 해충 퇴치?”

“……예, 뭐. 비슷합니다.”

어떻게 보면 몬스터도 거대한 해충이니 틀린 말은 아니다.

헌터 길드가 많은 부천에서도 수위에 꼽히는 상동 길드를 세스코로 만들어 버린 임꺽정이 진지하게 말을 이었다.

“후배 되시는 분이 솜씨가 좋은가 보네요.”

“아, 그런 편이죠.”

얼마나 잘 때려잡았는지 무려 대격변의 전쟁 영웅 중 한 사람이다.

물론 김 집사에게 있어 상동 길드장 임춘수는 한때 개처럼 굴리던 훈련생 중 하나에 지나지 않았지만.

“그 얘기는 그만들 하시죠. 그보다…….”

아까부터 웃음을 참느라 잔뜩 인상을 쓰고 있던 최 팀장이 서둘러 화제를 돌렸다.

때마침 적절한 주제가 될 인물이 한 사람 있었기 때문이다.

“진태경 씨는 왜 안 오는 겁니까?”

웃고 떠드는 사이 시간은 이미 출근 시간을 넘긴 지 오래.

이제야 진태경의 부재를 알아차린 임꺽정이 당황한 얼굴로 턱수염을 쓸었다.

“무슨 일이지? 태경이 그 녀석, 한 번도 이런 적이 없었는데. 성실함 하나는 내가 아는 사람 중에 최고거든.”

“그 사실은 저도 익히 알고 있습니다.”

최 팀장이 고개를 끄덕였다.

이미 한차례 진태경의 과거를 샅샅이 살펴본 그다. 보고서에 적힌 몇 년의 행적과 지금까지 직접 지켜본 바에 의하면 그 성실함과 집념은 진짜였다.

‘두 시간 후면 레이드 시작인데…….’

무슨 일이라도 있나?

고민하던 최 팀장이 핸드폰을 집어 드는데, 한동안 말이 없던 송송이가 불쑥 입을 열었다.

“황소자리, 아니 진태경 씨 말인데요.”

“……?”

“저기 있는데.”

희고 가느다란 손가락이 최 팀장의 어깨너머를 향했다.

다음 순간, 그녀가 가리키는 방향을 따라 자연스럽게 고개를 돌린 길드원들이 입을 딱 벌렸다.

길드 하우스 벽면에 걸린 TV 속, 낯익은 얼굴이 80인치 화면을 꽉 채우고 있었기 때문이었다.

“……허.”

“태경이! 태경이 아냐?”

“지, 진태경 헌터님이 맞는 것 같습니다만.”

오죽 당황했으면 시종일관 침착하던 김 집사마저 말을 더듬을 정도다.

그러나 길드원들은 이미 진태경의 얼굴 아래로 떠오른 자막에 모든 신경을 뺏긴 후였다.



진태경 (부천시 원미구. C급 헌터)

생중계) 톨 게이트 영웅



“톨게이트 영웅? 저거 뭐야! 소리는 왜 안 들려!”

“음소거! 음소거 모드예요! 빨리 소리 켜요!”

누군가 황급히 TV를 만지고 나서야 막혀 있던 소리가 흘러나오기 시작했다.

쉬쉬쉬쉬슁! 투타타타타!

뭔지 모를 소음과 함께 진태경의 말이 이어졌다.



- ……그래서 이렇게 된 겁니다.

- 예, 그렇군요. 그럼 마지막으로 소감 한마디만 해주시죠.

- 어어, 일단 제 가족들 너무 사랑하고요. 우리 평화 길드원들한테도 너무너무 고맙습니다. 그리고 제가 좋아하는…….

- 네! 그렇군요.

- 잠, 잠깐만요.

- 시간상 여기까지 하겠습니다. 시청자 여러분, 지금까지 톨게이트 영웅, 진태경 씨와의 인터뷰였습니다!



싱글벙글 웃는 기자의 얼굴을 마지막으로 비춘 화면이 화장품 광고로 넘어가자 임꺽정이 고함을 내질렀다.

“뭐야, 이게! 아무것도 못 들었잖아!”

“잠시만요. 바로 검색해 볼게요. 톨게이트 영웅, 톨게이트 영웅…… 헐.”

“송이 씨. 무슨 일입니까?”

눈을 동그랗게 뜬 채 굳어 있던 송송이가 말없이 핸드폰을 내밀었다.

포털 사이트 메인. 진태경이라는 이름 석 자가 떡하니 박혀 있었다.

“진태경 씨, 지금 실시간 검색어 1위예요.”

길드 하우스 내부가 찬물을 뒤집어쓴 것처럼 고요해졌다.

전혀 예상치 못한 상황에 모두가 할 말을 찾지 못하고 침묵만 이어지던 그때였다.

쉬쉬쉬슁! 투타타타!

“헉.”

“설마?”

불과 몇십 초 전 진태경의 인터뷰에서 들었던 그 소리가 들려온다.

후다닥 TV로 시선을 돌린 사람들이 여전히 이어지고 있는 광고에 한숨을 내쉰 것도 잠시.

“잠깐, 그럼 이게 왜 들려?”

가장 먼저 소음의 진원지를 알아차린 최 팀장과 김 집사가 입을 모아 외쳤다.

“바깥!”

“밖입니다! TV가 아니에요!”

우당탕탕!

말이 끝나기가 무섭게 사람들이 자리를 박차고 일어난 그 순간이었다.

- 와, 뭐야.

- 여기 맞습니까?

- 맞아요, 평화 길드. 리모델링 한다더니 엄청 좋아졌네.

- 혹시 길드원분들도 인터뷰 가능한가요?

- 싫어요. 아까 인터뷰 잘랐잖아요.

- 헌터님, 아까 그건…….

스피커 마법을 통해 생생히 전달되는 대화.

길드원들의 시선 속, 호흡을 가다듬은 최 팀장이 메시지 마법 장비를 입에 가져갔다.

“진태경 씨. 접니다.”

- 헉, 뭐야. 전음? 혹시 최 팀장님이세요?

“예.”

- 뭐지? 방금 그거 어떻게 하신 거예요?

최 팀장은 망설임 없이 입을 열었다. 그것은 뼛속 깊이 새겨진 본능이었다.

“별거 아닙니다. 유서 깊은 이탈리아의 장인 가문인 베르체니에 의뢰를 넣어서 특별 제작한…….”

임꺽정이 작은 목소리로 쌍욕을 내뱉었다.



* * *



‘자고 일어났더니 스타가 되어 있더라.’

내 살아생전 저 말을 현실로 체감하게 될 줄은 상상도 못 했다. 그것도 지금처럼 실시간으로.

- 저기, 호적 메이트 씨. 내가 지금 믿을 수 없는 걸 봤는데 말이지.

“호적 메이트? 죽고 싶냐, 너?”

- 아니, 지금 그게 문제가 아니라.

핸드폰 너머로 들리는 하연이의 목소리는 경악과 불신이 가득했다.

- 오빠 이름이 지금 뇌이버 실시간 검색어에…….

무슨 말을 할지 충분히 예상이 간다.

지난 몇 시간 동안 이미 수십 번도 넘게 비슷한 내용의 전화를 받았으니까.

나는 이어지려는 하연이의 말을 가로막았다.

“실시간 검색어 1위. 그래, 그거 나야. 나 맞아.”

- ……진짜야? 서울 외곽 순환도로 톨게이트 영웅? 그게 오빠라고?

“그렇게 부르지 마라. 쪽팔려 죽을 것 같다.”

- 와. 진짠가 보네. 이름 누르자마자 화제의 인물로 프로필 사진도 뜨던데, 보고 나서도 설마 했어.

이렇게 큰 반향을 불러일으킬 줄은 나도 미처 예상하지 못했다.

고작 몇 시간이 지났을 뿐인데, 당장 인터넷에 내 이름을 검색하면 어뷰징 기사 수십 개가 주르륵 뜰 정도다.

- 도대체 무슨 일이 있었던 거야? 기사 읽어 보니까 장난 아니던데. 아, 다친 곳은 없지?

“생채기 하나 안 났고, 처음부터 끝까지 말하자면 길어. 엄마는? 내 소식 아셔?”

- 아직은. 근데 오빠가 그런 괴물들이랑 싸운 걸 알면 기절할걸.

하연이의 말은 결코 과장이 아니었다.

오우거가 어떤 놈인가.

아무리 몬스터에 문외한인 사람이라고 해도 검색 몇 번만 하면 녀석이 흉측한 비주얼만큼이나 강력한 존재라는 것을 알 수 있다.

당신의 자식이 그런 괴물과 싸웠다는 소식에 엄마가 보일 반응이야 눈에 선했다.

“젠장. 그것도 그러네.”

- 어휴, 난 모르겠다. 난리 나기 전에 빨리 와서 얼굴이라도 비춰.

“어. 그럼 인터뷰 끝나고 잠깐 들릴게.”

- 인터뷰? 오빠 지금 인터뷰해?

“응.”

- 어디? 여성 잡지 이런 거?

“KPS 아홉 시 뉴스 데스크. 지금 차례 기다리고 있어.”

- ……헐.

할 말을 잃은 하연이에게 뭐라 대답하려는 찰나, 장비를 주렁주렁 끼고 있던 방송국 피디가 나를 향해 다급하게 손짓했다.

“이거 생방이라 나 지금 가 봐야 돼. 이따 집에서 보자.”

- 어어? 으응…….

전화를 뚝 끊고 TV에서나 보던 뉴스 녹화장으로 걸음을 옮겼다.

사방을 가득 메운 녹화 장비와 방송국 사람들의 시선에 입술이 바짝 마르고 다리가 후들거린다.

‘차라리 오우거 백 마리랑 싸우고 말지.’

일 분 일 초가 억겁처럼 느껴지던 그때, 마침내 기다리던 신호가 떨어졌다.

“들어갑니다. 스탠바이…… 큐!”
```

## Final English reading copy

```markdown
# Chapter 209

Ten in the morning.

Im Kkeokjeong, a D-rank Hunter of the Peace Guild who had come to work after spending a vacation as sweet as honey, stood there with his mouth hanging open.

“Whoa. What is this?”

It was understandable.

Before his vacation—in other words, just a week ago—the Guild House had been nothing more than a rundown neighborhood corner store.

But now, right before his eyes, stood a sign made of gleaming marble and luxurious lettering.

**<Peace Guild>**

“Wow. They went all out with the remodeling.”

Just as Im Kkeokjeong was admiring the exterior, a familiar voice came from somewhere.

“Why are you standing outside instead of coming in?”

Startled, he looked around. But when he saw neither the usual CCTV nor even an intercom, he cautiously opened his mouth.

“Te-Team Leader Choi? Is that you?”

“Yes. It’s me.”

“What is this? How are you talking to me?”

The reply came without the slightest hesitation, as though he had been waiting for that exact question.

“It’s nothing special. We commissioned the Vercheni family, a venerable Italian family of artisans, to make it especially for us. It includes message, observation, and alarm magic…”

“Ah, no. You don’t have to explain all that.”

“Oh. Then, if you open the mahogany door wrapped in salamander leather resistant to flames and come inside…”

“I’m coming in! I said I’m coming in!”

“…Yes.”

Click.

Along with that somehow dejected voice, the locked door slid open.

The interior of the Guild House had changed just as dramatically as the exterior. Three people were waiting for Im Kkeokjeong inside.

“Welcome.”

“Hunter Im.”

“Uncle’s here?”

Team Leader Choi, the practical owner of the Peace Guild; Butler Kim, who nominally served as its Guild Master; and Song Song, the guild’s lone woman.

The three of them were seated around a round table. As they greeted him in turn, Im Kkeokjeong let out a good-natured laugh.

“Maybe it’s because it’s been so long, but it’s good to see you all. Did you get plenty of rest during your vacation?”

The moment he finished speaking, the expressions of all three changed strangely.

After a brief silence, Song Song spoke.

“I rested. But there were so many bugs in the house that it bothered me.”

“Bugs?”

“Yes. Weren’t there any bugs at your place, Uncle?”

At Song Song’s question, Im Kkeokjeong tilted his head.

Come to think of it, his wife had complained about something similar several times during their vacation.

“Nothing much, just a fly or two. She said they kept coming in no matter how many she caught, so I left them alone, and then they quieted down. They hardly flew around, either.”

“Oh, really?”

“Yeah. They were the most well-behaved flies I’ve ever seen.”

Song Song shuddered uneasily.

“There were so many that I felt too uncomfortable even to shower. It felt like the bugs were watching me.”

“The bugs? Ha-ha-ha! Miss Song, you’re quite the joker.”

“…”

Im Kkeokjeong threw his head back and laughed. He failed to notice the other three exchanging meaningful looks and words he could not hear.

*He doesn’t seem to know.*

*Looks like he didn’t notice.*

*Wow. Is this guy seriously that dense?*

Unlike the three people who had been watched throughout their vacation by Familiars sent by the Sangdong Guild, Im Kkeokjeong had returned from a truly blissful vacation without knowing a thing.

It wasn’t that he hadn’t been watched. He had been watched; he simply didn’t know it.

The saying *ignorance is bliss* could not have been more fitting.

“Those fucking perverts. If I catch them later, I’m going to rip their balls off.”

If the mages of the Sangdong Guild had heard Song Song muttering those words, they would have felt the hair on the back of their necks stand up.

Im Kkeokjeong’s laughter abruptly stopped.

“Huh? What did you just say? Perverts?”

“No. I just said the bugs were disgusting.”

“Is it still that bad? I know someone who works for a company in that field. Want me to ask them about it?”

Song Song gave a quiet laugh at his genuine concern, then pressed her lips together and pointed at the two people sitting beside her.

“They’re all gone now. Those two put in a lot of effort. Especially Butler Kim.”

“Really? Kim hyung—I mean, Guild Master. Looks like you know a thing or two about that sort of thing.”

Butler Kim answered with an awkward smile.

“Not at all. I happened to know a junior who worked in that field.”

“Oh, exterminating pests?”

“…Yes, something like that.”

In a way, monsters were just enormous pests, so he was not technically wrong.

Im Kkeokjeong, who had effectively turned one of Bucheon’s leading Hunter Guilds into Cesco,[^1] continued in all seriousness.

“Your junior must be pretty skilled.”

“Ah, yes. He’s quite good.”

He was so good at beating them down that he was one of the war heroes of the Great Cataclysm.

Of course, to Butler Kim, Sangdong Guild Master Im Chunsoo was nothing more than one of the trainees he had once worked like a dog.

“Let’s stop talking about that. More importantly…”

Team Leader Choi had been grimacing as he struggled to hold back his laughter for some time. He hurriedly changed the subject.

There happened to be one person who made for a much more suitable topic.

“Why isn’t Jin Taekyung here?”

While they laughed and chatted, the appointed start time had long since passed.

Only now realizing Jin Taekyung’s absence, Im Kkeokjeong nervously stroked his beard.

“What happened? That kid Taekyung has never been late before. When it comes to diligence, he’s the best person I know.”

“I’m well aware of that.”

Team Leader Choi nodded.

He had already thoroughly investigated Jin Taekyung’s past once. Judging by the years of activity recorded in the report and what he had personally witnessed since then, Taekyung’s diligence and persistence were genuine.

*The raid starts in two hours…*

Had something happened?

As Team Leader Choi pondered the matter and picked up his phone, Song Song, who had been quiet for a while, suddenly spoke.

“Taurus—I mean, Jin Taekyung.”

“…”

“He’s right there.”

Her pale, slender finger pointed over Team Leader Choi’s shoulder.

The next moment, the guild members naturally turned in the direction she indicated, and their mouths fell open.

A familiar face filled the eighty-inch television screen mounted on the wall of the Guild House.

“…Huh.”

“Taekyung! Isn’t that Taekyung?”

“I believe that is indeed Hunter Jin Taekyung.”

Butler Kim was usually calm, but he was so flustered that even he began to stammer.

The guild members, however, had already lost all interest in anything except the caption appearing beneath Jin Taekyung’s face.

**Jin Taekyung** *(Bucheon City, Wonmi-gu. C-rank Hunter)*

**Live broadcast) Tollgate Hero**

“Tollgate Hero? What’s that supposed to mean? Why can’t we hear anything?”

“It’s muted! It’s in mute mode! Turn the sound on, quick!”

Only after someone hurriedly fiddled with the television did the blocked sound begin to spill out.

“Fwoosh-fwoosh-fwoosh-fwoosh! Ta-ta-ta-ta-ta!”

Along with some incomprehensible noise, Jin Taekyung’s voice continued.

“…And that’s how it happened.”

“Yes, I see. Then, finally, could you give us a few words about how you feel?”

“Uh, first of all, I love my family very much, and I’m incredibly grateful to all the members of the Peace Guild. And the person I like…”

“Yes! I see.”

“W-Wait a second.”

“That concludes our interview due to time constraints. Viewers, you have just watched an interview with Jin Taekyung, the Tollgate Hero!”

The screen showed the reporter’s beaming face one last time before switching to a cosmetics commercial.

Im Kkeokjeong shouted, “What the hell was that? I couldn’t hear anything!”

“Just a moment. I’ll search for it right away. Tollgate Hero, Tollgate Hero… Holy crap.”

“Song-i. What is it?”

Song Song had gone rigid, her eyes round. Without saying a word, she held out her phone.

The main page of the web portal was displayed on the screen. The three syllables of Jin Taekyung’s name were plastered across it.

“Jin Taekyung is number one on the real-time search rankings.”

The inside of the Guild House went silent, as though everyone had been doused with ice water.

No one had expected anything like this. They all sat in silence, unable to find the words.

Then—

“Fwoosh-fwoosh-fwoosh-fwoosh! Ta-ta-ta-ta-ta!”

“Whoa.”

“No way.”

It was the same sound they had heard during Jin Taekyung’s interview only a few dozen seconds earlier.

The group hurriedly turned toward the television. They let out sighs when they saw that the cosmetics commercial was still playing.

But only for a moment.

“Wait. Then why can we still hear it?”

Team Leader Choi and Butler Kim were the first to realize where the noise was coming from. They shouted together.

“Outside!”

“It’s outside! It isn’t the television!”

Crash!

The moment they finished speaking, everyone sprang to their feet.

“Wow, what the hell?”

“Is this the right place?”

“Yeah, this is the Peace Guild. I heard they were remodeling, but it looks incredible.”

“Would it be possible to interview the guild members too?”

“No. You cut my interview short earlier.”

“Hunter, about earlier…”

The conversation came through the speaker spell with perfect clarity.

As the guild members watched, Team Leader Choi steadied his breathing and brought the message-magic Equipment to his mouth.

“Jin Taekyung. It’s me.”

“Whoa, what the hell? Sound Transmission? Is that Team Leader Choi?”

“Yes.”

“What was that? How did you do that?”

Team Leader Choi opened his mouth without hesitation.

It was an instinct etched deep into his bones.

“It’s nothing special. We commissioned the Vercheni family, a venerable Italian family of artisans, to make it especially for us…”

Im Kkeokjeong muttered a string of vicious curses under his breath.

* * *

*I went to sleep and woke up a star.*

I had never imagined I would experience that saying for real in my lifetime.

And not merely overnight. I was experiencing it in real time.

“Hey, sibling-on-paper. I just saw something I can’t believe.”

“Sibling-on-paper? Are you trying to die?”

“No, that’s not the issue right now.”

Hayeon’s voice on the other end of the phone was filled with shock and disbelief.

“Oppa, your name is on Naver’s real-time search…”

I could easily guess what she was about to say.

I had already received dozens of calls with similar questions over the past few hours.

I cut Hayeon off before she could continue.

“Number one on the real-time search rankings. Yeah, that’s me. It really is.”

“…Seriously? The Seoul Outer Ring Expressway tollgate hero? That’s you?”

“Don’t call me that. I’m dying of embarrassment.”

“Wow. I guess it really is you. When I tapped your name, your profile picture even came up under ‘Person in the News.’ Even after seeing that, I thought, *No way.*”

I had not expected it to cause such a huge reaction, either.

Only a few hours had passed, but if I searched my name online, dozens of clickbait articles came streaming out.

“What on earth happened? I read the articles, and it sounded insane. You’re not hurt, are you?”

“I didn’t even get a scratch, and it’d take too long to tell you the whole story. What about Mom? Has she heard the news about me?”

“Not yet. But if she finds out you fought monsters like that, she’ll faint.”

Hayeon was not exaggerating.

What kind of creature was an ogre?

Even someone who knew nothing about monsters could search a few times and learn that they were every bit as powerful as their grotesque appearance suggested.

I could already picture how Mom would react to hearing that her son had fought such monsters.

“Damn. You’re right about that.”

“Ugh, I don’t know. Come home before everything blows up and at least show her your face.”

“Okay. I’ll stop by after the interview.”

“Interview? Are you doing an interview right now?”

“Yeah.”

“Where? For a women’s magazine or something?”

“The KPS Nine O’Clock News Desk. I’m waiting for my turn.”

“…Holy crap.”

Just as I was about to answer Hayeon, a television-station producer weighed down with Equipment urgently waved at me.

“This is live, so I have to go. See you at home later.”

“Uh-huh? O-Okay…”

I hung up and walked toward the news studio I had only ever seen on television.

Broadcasting Equipment filled the room in every direction, and the eyes of the station staff were fixed on me. My lips went dry, and my legs trembled.

*I’d rather fight a hundred ogres.*

At a time when every second felt like an eternity, the signal I had been waiting for finally came.

“We’re going live. Stand by… cue!”

[^1]: Cesco is a Korean pest-control company.
```
