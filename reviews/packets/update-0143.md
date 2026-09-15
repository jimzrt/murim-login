<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0143.txt",
      "sha256": "e9466af2e5a6386d13011a79fec09b27b9bc9b1de9a5283fd7c6edfce74d1098",
      "bytes": 14310
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "e4c40d86f817c84dff15399f96a594ed2f70fa9f0197832b1ced7eba789e54fd",
      "bytes": 3101
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "913d360529e0674fd2c50d54dff87de4e9b7299e1ff119da2877391a2ebf11d0",
      "bytes": 30368
    },
    {
      "path": "characters/Cheongpung.md",
      "sha256": "a4769316d26608f8f4461b12121f8aa63fe525606d40ae6bee5a2c06da8176e5",
      "bytes": 876
    },
    {
      "path": "characters/Hong Jin.md",
      "sha256": "5bcd853edf3bd83e71553e5552488731aac22616f9e0207fc91e56177e5579c5",
      "bytes": 809
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "f38740d5e6733a1303df8eed512dd77a677940a04e408898d58b3a74fd78df4a",
      "bytes": 24583
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "3382118cf9f6aeb83b5bec8ee87dee2b0792d4605991af81c93a7af5ed9fe76f",
      "bytes": 622
    },
    {
      "path": "characters/Li Feng.md",
      "sha256": "ec7b3e517d209f76c77db7ad3987f8ddfa18e753effb93c5be7bbcf9e96c15cf",
      "bytes": 888
    },
    {
      "path": "characters/Mae Jonghak.md",
      "sha256": "742c550afe7e2616099bbaadd93247ecd47cbc4da5e1be2d26b63bc9a3fd0aa3",
      "bytes": 468
    },
    {
      "path": "characters/Prince Shangshan.md",
      "sha256": "f96257a15317f0b99c016bcaec90b0955a3811a80a08cf072dba14c2d4789f99",
      "bytes": 630
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "9b5e6e583b838d55b6fc8ec1366fc1a8069480c748616584da6878a82aa699b9",
      "bytes": 25365
    }
  ],
  "estimated_tokens": 24875
}
-->

# Durable State Update — Chapter 143

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 143. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 20 concise items, `open_questions` to at most 8
items, and `temporary_decisions` to at most 8 items. Keep the serialized context
under 16384 UTF-8 bytes. Use only chapter
numbers through 143. `profile_updates` may replace one exact, uniquely occurring
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
  "chapter": 143,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 143,
    "continuity_sources": [143],
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
    "The Jin Family group is attending the City Lord's luncheon at the Shanxi Provincial Office.",
    "Cheongpung is a twenty-year-old Peak master raised by Mae Jonghak, the Sword Saint, and is recognized by Li Feng as his Martial Uncle.",
    "Cheongpung defeated Gong Ilhyuk with one counter using the Taeeul Miri Palm; Gong Ilhyuk remains hostile and refuses to accept the implications of Cheongpung's identity.",
    "Mae Jonghak remained in deep seclusion at a hidden Huashan residence and was still there at least ten years before the luncheon.",
    "Li Feng saw ten-year-old Cheongpung at Mae Jonghak's hidden residence and witnessed him perform the Plum Blossom Sword Technique.",
    "Li Feng left Huashan after becoming discouraged by Cheongpung's extraordinary talent, not because of his defeat by Gong Ilhyuk.",
    "Cheongpung knows several Huashan martial arts and can use the Zaha Divine Technique with potent Extreme Yang internal energy.",
    "Cheongpung's exact parentage or the truth behind his claim that a crane delivered him to Mae Jonghak remains unclear.",
    "The identities of the other two members of the Three Hands of Zhongnan remain unknown.",
    "Hong Jin is a eunuch who has served Prince Shangshan since infancy and is the power behind the Shanxi Provincial Office as Deputy Military Commissioner.",
    "Hong Jin intends to pursue the Shaanxi–Shanxi trade project through Huashan, while Li Feng acts as intermediary and contacts his Master.",
    "Gong Ilhyuk leaves the luncheon humiliated and vows revenge against those who rejected and insulted him.",
    "Taekyung encouraged Cheongpung to insult the Zhongnan disciples, and Cheongpung swore for the first time."
  ],
  "continuity_sources": [
    141,
    142
  ],
  "open_questions": [
    "What is Cheongpung's exact parentage, and what did Mae Jonghak mean by saying a crane delivered him?",
    "Why did Mae Jonghak remain hidden at Huashan despite the sect eventually finding his residence?",
    "What are the names and individual identities of the other two members of the Three Hands of Zhongnan?",
    "What is the full title of the wuxia novel beginning with 군림…… that Taekyung read through volume thirty-four?"
  ],
  "safe_through": 142,
  "temporary_decisions": [
    "Render 전하 as “His Highness” as the formal royal address and 왕 as “king” when Cheongpung uses it literally.",
    "Render 초일류 as “advanced First Rate” and 군문 as “military” when describing an affiliation.",
    "Render 풍운검군 as “Wind-and-Cloud Sword Lord” and 오촌 당숙 as “father's cousin.”",
    "Render 태을미리장 as “Taeeul Miri Palm.”",
    "Render 후배님 and 선배님 as “Junior” and “Senior” in the Gong Ilhyuk exchange.",
    "Render 태사부 as “Grandmaster” and 사숙 as “Martial Uncle” in the Huashan context.",
    "Render 자하신공 as “Zaha Divine Technique.”",
    "Render 군림…… as “The Reign…” and 꼰대 as “boomer” in the chapter 142 exchange."
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

## Exact glossary matches

| 진태경    | **Jin Taekyung**   |
| 매종학    | **Mae Jonghak**    |
| 청풍     | **Cheongpung**     |
| 산서잠룡   | **Sleeping Dragon of Shanxi** | Jin Taekyung   |
| 검성     | **Sword Saint**               | Mae Jonghak    |
| 태원진가   | **Jin Family of Taiyuan**        |
| 화산파    | **Huashan**                      |
| 일류     | **First Rate**    |
| 절정     | **Peak**          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 보법     | **manoeuvre technique** / **footwork technique** | Named Jin technique uses “Manoeuvre”                  |
| 검법     | **sword technique**                              |                                                       |
| 살기     | **killing intent**                               |                                                       |
| 검기     | **Sword Energy**                                 | When functioning as projected weapon qi               |
| 사부     | **Master**                                   |
| 제자     | **Disciple**                                 |
| 사숙     | **Martial Uncle**                            |
| 사질     | **Martial Nephew**                           |
| 은인     | **Benefactor**                               |
| 상태               | **Status**                     |
| 아이템              | **Item**                       |
| 산서     | **Shanxi**             |
| 태원     | **Taiyuan**            |
| 화산     | **Huashan**            |
| 대협      | **Great Hero** or **Sir** depending tone                        |
| 소협      | **Young Hero**                                                  |
| 홍진 | **Hong Jin** | Level 22 man at the City Lord's luncheon; delicate in appearance and voice. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 이풍 | **Li Feng** | Shanxi Province's Assistant Military Commissioner; former Huashan lay disciple |
| 상산왕 | **Prince Shangshan** | The City Lord and a member of the imperial family who orders the luncheon. |
| 산서성 | **Shanxi Province** | Province containing the Lower District Sect branches. |
| 도지휘첨사 | **Assistant Military Commissioner** | Military office held by the unnamed official responsible for training soldiers. |
| 산서성부 | **Shanxi Provincial Office** | Government office where the City Lord resides west of Taiyuan. |
| 도지휘동지 | **Deputy Military Commissioner** | Second-rank military office held by Eunuch Hong |
| 종남삼수 | **Three Hands of Zhongnan** | Three renowned Zhongnan Sect martial artists invited to the gathering |
| 전하 | **His Highness** | Formal royal address for the resident prince; the official insists on this form instead of king. |
| 태사부 | **Grandmaster** | Huashan title referring to Mae Jonghak. |

## Listed compact profiles

### Cheongpung.md

# Cheongpung (청풍)

- **Safe through:** Chapter 142
- **Aliases:** None
- **Role:** Mysterious young man encountered at Honghwa Inn; an exceptionally young Peak master whose Level Jin Taekyung cannot determine through Qi Sense; descended from the mountains to test himself against the Ten Dragons and Phoenixes
- **Personality:** Affable, dreamy, hazy, and childlike in manner, with innocent curiosity, delight in novel public attention, and a martial artist's competitive pride
- **Voice:** Dreamy and hazy, with innocent, polite phrasing
- **Relationships:** Mae Jonghak, the Sword Saint, is his grandfather and martial instructor; Cheongpung was living with him at a hidden Huashan residence by age ten and learned Huashan martial arts; calls Jin Taekyung and Hyuk Mujin Benefactors after they feed him

### Hong Jin.md

# Hong Jin (홍진)

- **Safe through:** Chapter 142
- **Aliases:** None
- **Role:** Level 22 Deputy Military Commissioner of Shanxi Province and a eunuch who has served beside Prince Shangshan since infancy; the power behind the Shanxi Provincial Office and the military's second-ranking official, he manages the City Lord's luncheon and redirects a planned Shaanxi–Shanxi trade project toward Huashan.
- **Personality:** Composed, observant, and socially deft; eases tension by redirecting attention to the arriving guests and flattering Taekyung.
- **Voice:** Delicate, complimentary, and conversational.
- **Relationships:** No established relationship with Taekyung beyond recognizing him as a young hero of the Jin Family of Taiyuan.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 142
- **Aliases:** Sleeping Dragon of Shanxi
- **Role:** Modern-world protagonist; recently fired after seven years at his job; C-rank Hunter who defeated eight B-rank Minotaurs and killed a Level 70 B-rank Minotaur Warrior in one blow; First Rate martial artist standing before the Peak realm who now possesses forty-five years of internal energy with the Scorching Yang Qi attribute after fully absorbing the Blazing Flame Divine Pill; youngest son of the Jin Family of Taiyuan; new owner of a two-story detached house in Goyang intended for his family; Qi Sense reaches a seventy-meter radius; possesses one Temporary Strength Pill in his Inventory and has reserved it for a worst-case, life-threatening contingency; Level 61 with 2,100 Fame and 60 unspent stat points, and the Sleeping Dragon of Shanxi Title now grants all stats +15 and Fame +200
- **Personality:** Hungry, self-aware, dryly observant, and willing to take a questionable opportunity when desperate; treats the impossible as a game until the danger becomes undeniable
- **Voice:** First-person, conversational, dryly self-mocking; uses vivid trap-and-prey imagery, game jargon, and occasional profanity
- **Relationships:** Jin Mukyung’s younger brother and current student; son of a deceased father; supports his mother and younger sibling; loves Song Song; has a strained relationship with Lee Seowol, the current Sect Leader of the Mount Heng Sword Sect, whose marriage proposal he has decided to reject

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 142
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Li Feng.md

# Li Feng (이풍)

- **Safe through:** Chapter 142
- **Aliases:** None
- **Role:** Assistant Military Commissioner of Shanxi Province; former Huashan lay disciple who left the sect nearly ten years ago
- **Personality:** Resolute, proud, blunt, and hostile toward political and martial rivals
- **Voice:** Formal and restrained in official settings; dry and cutting with opponents
- **Relationships:** Former lay disciple of Huashan; visited the hidden residence of his Grandmaster Mae Jonghak and saw ten-year-old Cheongpung there; recognizes Cheongpung as his Martial Uncle; direct subordinate and political rival of Hong Jin, the Deputy Military Commissioner; agrees to act as Hong Jin's intermediary with Huashan and send a messenger pigeon to his Master; bears a humiliating martial grievance involving Gong Ilhyuk

### Mae Jonghak.md

# Mae Jonghak (매종학)

- **Safe through:** Chapter 142
- **Aliases:** Sword Saint
- **Role:** Sword Saint and Cheongpung's grandfather; remained in deep seclusion at a hidden residence on Huashan
- **Personality:** Not established in this chapter.
- **Voice:** Not established in this chapter.
- **Relationships:** Cheongpung's grandfather and martial instructor; taught him the Taeeul Miri Palm.

### Prince Shangshan.md

# Prince Shangshan (상산왕)

- **Safe through:** Chapter 142
- **Aliases:** None
- **Role:** The City Lord and a member of the imperial family who summons martial officials and young Murim prodigies to a noon luncheon.
- **Personality:** His personal temperament is not established; his authority is treated as commanding and difficult to refuse.
- **Voice:** No direct speech appears in this chapter.
- **Relationships:** Commands the unnamed Third-Rank Assistant Military Commissioner to attend the luncheon and hosts the gathering of young Murim prodigies.

## Korean source

```text
＃143화



개망신당한 종남삼수가 쿵쾅거리며 떠나자 홍진이 품에서 자그마한 종을 꺼내 흔들었다.

“자, 그럼 불청객들도 갔으니 정리가 필요하겠군요.”

뎅, 뎅, 뎅.

정확히 세 번. 종소리가 채 사라지기도 전에 철문이 열리더니 수십 명의 하인이 들어와 허리를 굽힌다.

“대전을 깨끗이 치우고 새로 음식을 내오너라.”

“명을 받들겠습니다.”

재차 허리를 굽힌 그들은 일사불란하게 움직였다.

쪼개진 탁자와 널브러진 음식물들, 심지어 청풍의 토사물조차도 눈썹 하나 깜짝하지 않고 척척 치워 나가기 시작했다.

‘프로네, 프로야.’

어지간한 청소 업체 저리 가라다.

감탄하는 나와는 달리 뭐 마려운 표정으로 끙끙거리던 청풍이 하인들을 향해 조심스레 다가갔다.

“죄, 죄송합니다. 제가 도와드릴게요.”

하인 중 하나가 고개를 저었다.

“아닙니다. 저희가 해야 할 일입니다.”

“그래도 제가 어질러 놨으니 이것만이라도…….”

하인들이 아무리 건장한 사내들이라고 해도 상대는 절정 고수. 그들은 청풍의 뜻을 따를 수밖에 없었다.

그러나 억지로 청소 도구를 빼앗아 토사물을 치우던 청풍의 움직임이 순간 덜컥 멈췄다.

“우욱, 우웨에에엑!”

“…….”

제발 가만히 있어. 괜히 일거리 늘리지 좀 말고.

또다시 한바탕 거하게 쏟아 내는 녀석의 모습에, 홍진이 미심쩍은 눈빛으로 이풍을 바라봤다.

“이 첨사, 저 청년이 정말 검성 매종학 대협의 제자가 맞나요?”

“확실합니다.”

“그런데 상태가 왜 저래요?”

“크흠.”

이풍이 붉어진 얼굴로 헛기침을 했다. 그에게 있어 청풍은 검성 매종학의 제자이자 사문의 어른이지만, 살짝 이상한 놈인 것도 부정할 수 없는 사실일 테다.

“아무래도 속세와는 동떨어진 삶을 살아오다 보니 저러시는 것 같습니다만.”

“아니, 아무리 그래도 그렇지. 매 대협이 기본적인 것도 안 가르쳐 줬단 말이에요?”

“그게…… 제가 보고 듣기로는 태사부께서도 범상치 않으신 분이라.”

범상치 않은 분이라.

혼신의 힘을 다한 포장이었지만 내 귀에는 ‘그놈이 그놈인데요.’로 들린다.

홍진도 비슷한 느낌을 받았는지 잠깐 침묵을 지켰다.

“이번 일, 화산파에게 맡겨도 되는 거죠?”

“……예.”

어쩐지 한 박자 늦은 이풍의 대답에 홍진이 고개를 절레절레 저었다.

“그 이야기는 나중에 나누도록 하고, 슬슬 가 볼까요?”

그 말에 의구심을 느낀 내가 물었다.

“어디를요? 아직 전하도 안 오셨는데.”

“바로 그 전하를 모시러 가려고요.”

“네?”

“이대로라면 기다리다가 해 떨어져요. 난 전하가 어디에 계시는지 대충 알거든.”

눈을 찡긋하며 돌아서는 홍진을 보며 생각했다.

‘저 짓거리만 안 해도 괜찮은 놈인데.’

우리 편 들어 준 건 고맙긴 한데, 그건 그거고 이건 이거다.

내 엉덩이는 소중하니까.



* * *



홍진과 이풍. 두 사람이 나란히 앞장서서 걸었다.

그 뒤를 따라가다 보니 그들이 이곳에서 어떤 위치이며, 어느 정도의 위상을 갖고 있는지 대강 파악할 수 있었다.

“충!”

사람은 눈빛과 태도, 목소리에서 감정이 묻어나오는 법.

이풍을 향해 힘차게 군례를 올리는 군사들의 모습에서 무한한 존경심을 읽어 낼 수 있었다.

‘그럴 만도 하지.’

화산파의 속가제자인 이풍은 초일류의 고수다. 강함을 숭상하는 건 수컷들의 본능인 데다 그는 척 봐도 사내다운 냄새가 물씬 풍겼다. 잠깐 지켜본 바로는 우직하고, 과묵하다.

‘그렇다고 해서 아주 꽉 막힌 사람도 아니고.’

홍진의 제안을 받아들인 것만 봐도 알 수 있다. 서로 으르렁거리던 관계가 분명한데, 손을 잡을 때와 놓을 때를 안다.

적당히 융통성 있는 상관을 싫어할 사람은 없지.

‘그럼 홍진은?’

나는 시선을 옆으로 옮겼다.

경박하게 궁둥이를 씰룩거리며 걸어가는 홍진에게는 군사 중 그 누구도 존경심을 표하지 않았다. 오히려 몇몇은 경멸 어린 시선을 던지기까지 했다.

다만…….

“도, 도지휘동지 대감을 뵙습니다.”

“응. 그래. 수고해요.”

“예, 옛!”

가는 길에 마주친 몇몇 관리와 하인들은 과장스러울 정도로 설설 기었다.

떨리는 목소리와 조심스러운 발걸음. 그들이 보여 준 감정은 명백한 두려움이다.

‘존경과 두려움이라.’

상반되는 감정이지만 한 가지 맥락에서는 같다.

그건 바로 사람들 다루는 용인술(用人術)이다. 이풍과 홍진은 각각 존경과 두려움으로 수하들의 지지를 받고 있었다.

‘한 사람은 군부를, 한 사람은 내정을 손에 쥔 셈인가?’

산서성은 변방으로 불리지만 그 규모는 무시할 수 없다.

광활한 면적과 호적에 등록된 인구만 수백만에 이르는 당당한 자치 구역인 것이다.

땅이 있는 곳에 사람이 모이고, 사람이 모인 곳에는 권력과 재물이 흐른다. 산서성부 내에서도 보이지 않는 치열한 힘겨루기가 계속되고 있었다.

‘아까부터 들어 보니 홍진이 더 앞선 것 같긴 하지만, 뭐. 내가 신경 쓸 문제는 아니지.’

먹고 살기도 바쁜 마당에 남의 집 권력 싸움에 끼어들 생각은 추호도 없다.

이런저런 생각을 하며 얼마나 걸었을까, 우리는 어느덧 아홉 개의 문을 지나 일단의 무리와 맞닥뜨렸다.

“도지휘동지, 그리고 도지휘첨사 오셨습니까.”

열 번째 문은 유독 크고 높았다. 정말 그렇게 지었는지, 아니면 물 샐 틈 없이 주위를 둘러싼 일백의 병력 때문에 그렇게 보이는지는 모르겠다.

‘이야, 경계 삼엄한 것 보소.’

절정 고수, 그것도 검기를 쓸 수 있을 정도는 돼야 어떻게 해 볼 수 있을까? 하나같이 갑주와 창, 검, 활 등으로 중무장한 그들은 투구 사이로 날카로운 눈빛을 뿜어냈다.

지금까지 주위를 구경하며 연신 탄성을 내지르던 청풍도 목소리를 한껏 죽이고 내게 속삭였다.

“우와아. 이분들은 뭐 하시는 분들이세요?”

“글쎄요, 아마도 상산왕 전하를 경호하는 근위대가 아닐까요?”

“근위대요? 멋있다…….”

멍한 얼굴로 중얼거리던 청풍이 주먹을 불끈 쥐었다.

“은인, 저 결심했어요.”

“뭘요?”

난 왜 얘가 입을 열 때마다 불안해질까?

물론 이번에도 예감은 정확히 들어맞았다.

“저도 근위대에 들어갈래요!”

“……그렇게 좋은 생각은 아닌 것 같은데요.”

검성이 좋아할 것 같지 않은 소식이다.

나는 지끈거리는 이마를 문지르며 말했다.

“그, 조부님 허락은 맡아야 하지 않겠어요?”

“괜찮아요. 할아버지가 그랬어요. 인생은 짧으니까 하고 싶은 게 생기면 뭐든 해 보라고.”

“그래서 그게 근위대다?”

“네.”

청풍은 반짝거리는 눈빛으로 칼같이 늘어선 근위대를 뚫어져라 응시했다. 정확히는 그들의 번쩍거리는 흑색 갑옷을.

아니, 이 새끼가 설마?

“……혹시 갑옷이 멋있어서 그런 건 아니죠?”

“헉.”

맞네. 이런 미친놈을 봤나.

‘근위대 굿즈가 탐나서 근위대에 들어가는 놈이 어디 있냐.’

우리의 대화를 듣고 있던 이풍이 10년은 늙은 얼굴로 다가왔다.

“청풍 사숙, 저야 보잘것없는 속가제자라지만 사숙께서는 화산의 미래를 짊어지실 적전제자이십니다. 사문을 버리고 군문에 투신하신다니요, 제발 언행에 주의를…….”

정곡이 찔린 얼굴로 서 있던 청풍이 다급하게 손을 내저었다.

“아, 아니에요. 진짜 아닌데.”

“정말이십니까?”

“네, 네!”

“그럼 그렇게 알고 있겠습니다. 혹시 필요하시다면 가시는 길에 갑옷 한 벌 챙겨 드리려고 했는데…….”

덥석.

“감사히 받을게요. 이 대협.”

“…….”

“…….”

아니, 이 새끼가 진짜?

싸해진 주변 상황도 모르고 청풍이 헤헤 웃었다.

“이 대협은 좋은 사람이에요.”

“대협이 아니라 사질입니다. 청풍 사숙.”

“사숙, 사질. 이런 말은 어색한데…… 그냥 서로 편하게 부르면 안 돼요?”

“안 됩니다. 본 파의 위계는 엄격합니다. 앞으로 사질이라고 부르십시오. 그래야 갑옷을 드릴 겁니다.”

“으음. 그래도…….”

망설이는 청풍을 향해 이풍이 마지막 한 방을 날렸다.

“앞으로 저를 사질이라고 부르신다면 근위대가 쓰는 병장기도 함께 드리겠습니다.”

“헉……!”

게임 끝이다.

굿즈의 완성은 세트 아이템인 법. [근위대 갑옷 세트]를 손에 넣게 된 청풍이 환희에 가득 찬 얼굴로 양팔을 벌렸다.

“이풍 사질!”

이풍이 엉거주춤 대답했다.

“처, 청풍 사숙.”

“저는 이풍 사질이 세상에서 제일 좋아요!”

“……감사합니다. 사숙.”

저런 놈을 손자라고 20년 동안 키운 검성이 불쌍해진다.

근위대마저 이 뜻밖의 촌극에 정신이 팔려 있을 때, 홍진이 한숨을 푹 내쉬며 입을 열었다.

“뭐 해요, 문 안 열고?”



* * *



가슴팍에나 닿으려나? 어린 왕, 상산왕(上山王) 주표(朱豹)는 내가 생각한 것보다 훨씬 작았고, 또 강했다.

쉬쉬쉬쉭!

고작 열 살짜리 어린아이가 휘두르는 검에서 날 만한 소리가 아니다. 날카로운 검로, 바쁘게 연무장 바닥을 누비는 보법.

검공에는 그리 조예가 깊지 않은 내게도 충분히 고개가 끄덕여질 만한 수준이었다.

‘괜히 우리를 초청한 게 아니었군.’

처음 상산왕의 초청을 받았을 때 든 생각은 하나였다.

가서 적당히 듣고 싶어 하는 무용담이나 몇 개 들려줘야지. 딱 이 정도?

하지만 저 아이는 다르다. 무용담이 아니라 무공에 대해 알려 줘야 할지도 모른다.

“전하를 본 소감이 어때요?”

연무장 바깥에서 대기 중이던 수행원들을 손짓 하나로 전부 물린 홍진이 물었다.

그 와중에도 무공에 몰입한 어린 왕은 누가 왔는지, 누가 가는지도 눈치채지 못하고 있었다.

“정확히 어떤 소감을 말씀하시는 겁니까?”

“글쎄, 일단은 무공?”

나는 솔직히 대답했다.

“생각 이상입니다. 아니, 뛰어나요. 언제부터 익히기 시작한 겁니까?”

“삼 년 전부터 무공에 흥미를 보이기 시작하셨죠.”

“삼 년…….”

“네. 처음 검을 쥔 그날부터 특별한 일이 없는 한 하루도 빠짐없이 무공을 수련하세요.”

이풍이 흐뭇하게 웃으며 덧붙였다.

“여러모로 어린아이답지 않으신 분이오. 대단한 집념의 소유자시지. 마치 진 소협처럼 말이오.”

“저요?”

“그렇소. 진 소협도 어린 시절부터 뼈를 깎는 노력을 했다지요? 태원진가가 비밀리에 심혈을 기울여 키운 고수답게 큰 활약을 펼치고 있잖소.”

“어…… 그렇죠.”

저건 대외적으로 태원진가에서 퍼트린 헛소문이다.

정작 나는 내가 열 살 때 뭘 했는지는 기억도 안 난다.

‘초등학교 다녔겠지, 뭐.’

이풍이 말을 이었다.

“전하께서 산서잠룡의 이야기를 들으시고는 얼마나 좋아하셨는지 모르오. 아마 오늘도 진 소협과 만나기를 학수고대하셨겠지.”

“……그런 것치고는 꽤 오래 기다리지 않았나요?”

거의 한 시간은 기다린 것 같은데. 왕이라서 그런가, 어린 녀석이 벌써부터 기본 매너가 없어요.

소심하게 투덜거리는 내게 이풍이 빙긋 웃었다.

“전하께선 긴장을 할수록 무공에 몰두하는 습관이 있으시지. 혹시 마음 상했다면 사과드리겠소.”

뭘 또 사과씩이나. 내가 손사래를 치던 그때, 홍진이 입에 두 손을 모아 외쳤다.

“저어어언하-!”

간드러진 외침에 검법을 펼치던 자그마한 신형이 우뚝 멈춘다. 이윽고 우리를 발견한 녀석이 손을 까딱였다.

“뭡니까 저게?”

“뭐긴, 전하께서 부르시는 거지요.”

“아니, 우리가 동네 똥갭니까?”

“와, 저 동네 똥개 처음 해 봐요!”

“……제발 입 좀 다물어. 여기 동네 똥개 해 본 사람 아무도 없어.”

나는 울화를 참으며 연무장을 향해 다가갔다.

상산왕 주표. 한 걸음마다 그의 얼굴이 가까워진다.

‘꼭 싸가지 없는 놈들이 잘생겼더라.’

어린 나이임에도 이미 완성된 이목구비는 뚜렷했고, 검은 눈동자는 나를 빤히 응시하고 있었다.

녀석의 앞에 다다르자 아직 한참 앳된 목소리가 흘러나왔다.

“과인이 누구인지 아는가?”

이미 기본적인 예의는 배웠다. 나는 한쪽 무릎을 꿇어 주표와 시선을 맞췄다.

“예. 상산왕 전하.”

“과인은 아직 그대의 이름을 모른다.”

“태원진가의 진태경이라 합니다.”

위엄 있던 눈동자에 희미한 놀라움이 떠올랐다.

“사, 산서잠룡 진태경이란 말이냐?”

“그렇습니다.”

과연 그가 무슨 반응을 보일까?

한참 말이 없던 어린 왕이 돌연 품에서 뭔가를 꺼냈다. 어른 손바닥만 한 목판과 단검이었다.

“이거…….”

“……?”

일단 주니까 받긴 했는데. 뭘 어쩌라고?

어리둥절한 내게 주표가 위엄 있는 한마디를 던졌다.

“서명을 부탁하마.”

“…….”

아, 사인해 달라고?
```

## Final English reading copy

```markdown
# Chapter 143

After the Three Hands of Zhongnan left in disgrace, their footsteps echoing heavily, Hong Jin pulled a small bell from inside his robes and shook it.

“Well, now that the uninvited guests are gone, I suppose we should clean up.”

*Ding. Ding. Ding.*

Exactly three times. Before the sound had even faded, the iron doors opened and dozens of servants entered, bowing at the waist.

“Clean the grand hall and bring out a fresh meal.”

“We’ll carry out your orders.”

After bowing once more, they moved with perfect coordination.

They began clearing away the broken tables and scattered food without batting an eye—not even at Cheongpung’s vomit.

*They’re professionals. Absolute professionals.*

They put most cleaning companies to shame.

Unlike me, Cheongpung had been groaning with an expression like he needed to use the bathroom. He cautiously approached the servants.

“I-I’m sorry. Let me help.”

One of the servants shook his head.

“No, sir. This is our duty.”

“But I made the mess, so at least let me…”

No matter how sturdy the servants were, they were facing a Peak master. They had no choice but to follow Cheongpung’s wishes.

However, the moment Cheongpung forcibly took the cleaning tools from them and began wiping up the vomit, his movements abruptly stopped.

“Urk, uweeek!”

“……”

*Please stay still. Stop making more work for them.*

As Cheongpung emptied his stomach once again, Hong Jin looked at Li Feng with a doubtful expression.

“Assistant Commissioner Li, is that young man really Sword Saint Mae Jonghak’s Disciple?”

“Certainly.”

“Then why is he like that?”

“Ahem.”

Li Feng cleared his throat, his face reddening.

To him, Cheongpung was both Sword Saint Mae Jonghak’s Disciple and an elder of his sect. But it was also impossible to deny that he was a slightly strange young man.

“I suppose he’s like this because he’s spent his life completely removed from the secular world.”

“No, but even so. Are you saying Great Hero Mae didn’t teach him the basics?”

“Well… from what I’ve seen and heard, my Grandmaster is not an ordinary person himself.”

*Not an ordinary person.*

It was an impressive effort at putting things politely, but what I heard was, *They’re two of a kind.*

Hong Jin must have gotten a similar impression, because he remained silent for a moment.

“Would it really be all right to leave this matter to Huashan?”

“……”

“Yes.”

Li Feng’s answer came half a beat late. Hong Jin shook his head in disbelief.

“We can discuss that later. Shall we get going?”

His words made me suspicious, so I asked,

“Where? His Highness hasn’t even arrived yet.”

“That’s exactly who I’m going to fetch.”

“What?”

“If we stay here, we’ll be waiting until sunset. I have a rough idea where His Highness is.”

I watched Hong Jin turn away with a wink.

*He’d be a decent guy if he just stopped doing that.*

I was grateful that he had taken our side, but that was that, and this was this.

*My backside is precious.*

* * *

Hong Jin and Li Feng walked side by side at the front.

As I followed them, I gradually began to understand what positions they held here and how much influence they possessed.

“Loyalty!”

People’s emotions show in their eyes, their posture, and their voices.

The soldiers snapped off energetic military salutes toward Li Feng, and I could read boundless respect in their faces.

*It’s understandable.*

Li Feng, a lay disciple of Huashan, was an advanced First Rate master. Respecting strength was a male instinct, and he radiated an unmistakably masculine presence. From what I had observed, he was steadfast and taciturn.

*But he isn’t completely inflexible, either.*

I could tell from the fact that he had accepted Hong Jin’s proposal. Their relationship had clearly been hostile, but Li Feng knew when to join hands and when to let go.

No one disliked a superior who was reasonably flexible.

*Then what about Hong Jin?*

I shifted my gaze to the side.

Not a single soldier showed Hong Jin any respect as he walked along, frivolously wiggling his backside. If anything, some of them even cast contemptuous looks his way.

However…

“I-I pay my respects to Deputy Military Commissioner Hong.”

“Mm. Yes. Good work.”

“Yes, sir!”

Several officials and servants we passed on the way practically groveled before him.

Their trembling voices and cautious footsteps made their emotions obvious.

They were afraid.

*Respect and fear.*

They were opposing emotions, but they were the same in one respect.

Both came from the art of handling people. Li Feng and Hong Jin each held the support of their subordinates through respect and fear.

*So one of them controls the military, while the other controls civil affairs?*

Shanxi Province was called a frontier region, but its size couldn’t be ignored.

It was a respectable autonomous territory with a vast area and a population of several million registered in its household records.

Where there was land, people gathered. And where people gathered, power and wealth flowed. Even within the Shanxi Provincial Office, an invisible and fierce struggle for power was still underway.

*From what I’ve heard, Hong Jin seems to be ahead. But that’s not my problem.*

I was too busy trying to make a living to get involved in someone else’s power struggle.

After walking for some time while lost in thought, we passed through nine gates and came upon a group of people.

“Deputy Military Commissioner, and Assistant Military Commissioner, have you arrived?”

The tenth gate was particularly large and tall. I couldn’t tell whether it had genuinely been built that way or only seemed so because a hundred soldiers surrounded it without leaving even a gap.

*Wow. Talk about tight security.*

Would a Peak master, and one capable of using Sword Energy at that, be needed to try anything here? Every one of the guards was heavily armed with armor, spears, swords, bows, and more. Sharp eyes gleamed from beneath their helmets.

Cheongpung, who had been looking around and exclaiming in wonder this entire time, lowered his voice and whispered to me.

“Wow. What do these people do?”

“I’m not sure. Perhaps they’re the royal guard protecting Prince Shangshan?”

“The royal guard? They’re amazing…”

Cheongpung muttered with a vacant expression, then clenched his fists.

“Benefactor, I’ve made up my mind.”

“About what?”

*Why do I get nervous every time he opens his mouth?*

Of course, my premonition proved correct again.

“I want to join the royal guard too!”

“……I don’t think that’s such a good idea.”

This was news the Sword Saint probably wouldn’t like.

I rubbed my throbbing forehead.

“Um, shouldn’t you get your grandfather’s permission first?”

“It’s all right. Grandfather said life is short, so whenever I want to do something, I should try it.”

“So that’s why you want to join the royal guard?”

“Yes.”

Cheongpung stared intently at the royal guards standing in perfect rows, his eyes shining.

More precisely, he was staring at their gleaming black armor.

*No way. Is this guy…?*

“……It’s not because the armor looks cool, is it?”

“Gasp.”

That was it.

What kind of lunatic joined the royal guard because he wanted their merchandise?

Li Feng, who had overheard our conversation, approached us with a face that looked ten years older.

“Martial Uncle Cheongpung, I may be nothing more than a lowly lay disciple, but you are Huashan’s direct Disciple, someone who will bear the future of the sect on your shoulders. To abandon the sect and devote yourself to the military… Please be careful with what you say and do…”

Cheongpung stood there with an expression that had clearly been hit right in the bull’s-eye, then frantically waved his hands.

“N-No, that’s not it. Really.”

“Is that so?”

“Yes, yes!”

“Then I’ll take your word for it. I was considering bringing you a suit of armor on the way out, if you needed one, but…”

Cheongpung took the bait immediately.

“Thank you. I’ll accept it gratefully, Great Hero Li.”

“……”

“……”

*Is this guy serious?*

Cheongpung, oblivious to the sudden chill in the air around us, grinned.

“Great Hero Li is a good person.”

“I’m not Great Hero. I’m your Martial Nephew, Martial Uncle Cheongpung.”

“Martial Uncle, Martial Nephew. Those words feel awkward…”

Cheongpung tilted his head.

“Can’t we just call each other whatever feels comfortable?”

“No. Our sect’s hierarchy is strict. Call me Martial Nephew from now on. Then I’ll give you the armor.”

“Hmm. Even so…”

Li Feng delivered his final blow to the hesitating Cheongpung.

“If you call me Martial Nephew from now on, I’ll give you the weapons used by the royal guard as well.”

“Gasp…!”

The game was over.

The finishing touch for merchandise was a complete set. Cheongpung, now on the verge of obtaining the Royal Guard Armor Set, spread both arms with a face full of joy.

“Martial Nephew Li Feng!”

Li Feng answered awkwardly.

“M-Martial Uncle Cheongpung.”

“I like Martial Nephew Li Feng best in the world!”

“……Thank you, Martial Uncle.”

I felt sorry for the Sword Saint, who had raised that guy as his grandson for twenty years.

While even the royal guards were distracted by this unexpected farce, Hong Jin let out a deep sigh and spoke.

“What are you doing? Why haven’t you opened the gate?”

* * *

The young prince barely came up to my chest, if that. Prince Shangshan, Zhu Bao,[^1] was much smaller than I had expected—and much stronger.

*Ssshhk, ssshhk, ssshhk!*

That was not a sound a mere ten-year-old child should have been able to make with a sword.

His sword paths were sharp, and his footwork technique carried him busily across the training ground.

Even I, who wasn’t particularly well versed in sword techniques, could tell that his skill was more than enough to make me nod in approval.

*So there was a reason he invited us.*

When I first received Prince Shangshan’s invitation, I had one thought.

*I’ll go and tell him a few of the heroic tales he wants to hear. That was about all I had expected.*

That was all I had expected.

But that child was different. I might have to teach him about martial arts instead of telling him stories about my exploits.

“What do you think of His Highness?”

Hong Jin had waved away all the attendants waiting outside the training ground with a single gesture before asking me.

Even then, the young prince, absorbed in his martial arts, didn’t notice who had arrived or who had left.

“What kind of opinion are you asking for?”

“Well, for starters, his martial arts?”

I answered honestly.

“He’s beyond my expectations. No, he’s outstanding. When did he begin learning?”

“He began showing an interest in martial arts three years ago.”

“Three years…”

“Yes. Ever since the day he first held a sword, he has trained in martial arts every single day unless something unusual happened.”

Li Feng smiled proudly and added,

“He is not like an ordinary child in many ways. He possesses astonishing determination. Much like Young Hero Jin.”

“Me?”

“That’s right. I heard Young Hero Jin worked himself to the bone from a young age. You’ve been making quite a name for yourself, just as one would expect from a master the Jin Family of Taiyuan secretly raised with such painstaking care.”

“Uh… yes, I suppose.”

That was a bogus rumor the Jin Family of Taiyuan had spread for public consumption.

In reality, I didn’t even remember what I had been doing at the age of ten.

*I must have been attending elementary school or something.*

Li Feng continued.

“You have no idea how delighted His Highness was when he heard the story of the Sleeping Dragon of Shanxi. He must have been eagerly awaiting the chance to meet Young Hero Jin today.”

“……For someone who was looking forward to it, didn’t he make us wait rather a long time?”

I felt as though we had been waiting for almost an hour. Was it because he was a prince? The little brat already had no basic manners.

Li Feng smiled faintly at my timid complaint.

“His Highness has a habit of immersing himself in martial arts whenever he is nervous. If he has offended you, please accept my apologies.”

There was no need to apologize over something like that. I was waving my hands dismissively when Hong Jin cupped both hands around his mouth and shouted,

“His Hiiiighness—!”

The little figure who had been practicing his sword technique stopped abruptly at the shrill call. A moment later, he noticed us and crooked a finger.

“What is that supposed to be?”

“What do you mean? His Highness is calling us.”

“No, I mean, are we neighborhood mutts?”

“Wow, this is my first time being a neighborhood mutt!”

“……Please shut your mouth. No one here has ever been a neighborhood mutt.”

Suppressing my frustration, I walked toward the training ground.

Prince Shangshan Zhu Bao. His face came closer with every step.

*The rude ones always seem to be handsome.*

Even at such a young age, his already fully formed features were sharp and distinct. His black eyes stared directly at me.

When I reached him, a voice that was still unmistakably childish drifted out.

“Do you know who I am?”

I had at least learned the basics of etiquette by now. I lowered myself onto one knee so that our eyes were level.

“Yes. His Highness, Prince Shangshan.”

“I do not yet know your name.”

“My name is Jin Taekyung of the Jin Family of Taiyuan.”

A faint trace of surprise appeared in his previously dignified eyes.

“T-The Sleeping Dragon of Shanxi, Jin Taekyung?”

“That’s right.”

I wondered what his reaction would be.

The young prince remained silent for a long moment. Then he suddenly pulled something from inside his robes.

A wooden tablet about the size of an adult’s palm, and a dagger.

“This…”

“……?”

He had handed them to me, so I accepted them. But what was I supposed to do with them?

As I stood there in bewilderment, Zhu Bao delivered a single dignified word.

“I would like your signature.”

“……”

*Oh. He wants an autograph?*

[^1]: Zhu Bao (朱豹) is Prince Shangshan’s personal name.
```
