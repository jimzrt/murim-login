<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0313.txt",
      "sha256": "a5b116d640af4ef63556e67b50af5537a46bfb7e90dbdc6ae6228b7832a33512",
      "bytes": 14244
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "829eb8e4049ba4c89e3083a6853af7323186f13fe7064d599fe2ffeccec1b566",
      "bytes": 1381
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "5b1a5119a71cbc3933b6e4bbc92de054062050a84aeae56680d8192f6e0500e7",
      "bytes": 103544
    },
    {
      "path": "characters/Baek Museong.md",
      "sha256": "edb7a2ccf4848a320697f704144ed7a1f0580ebac1faeb0a899929b76e180540",
      "bytes": 975
    },
    {
      "path": "characters/Cheongpung.md",
      "sha256": "53e798321e1095ae02e762b3f52a2b88311fd1062371405af11f55bb7796066f",
      "bytes": 3397
    },
    {
      "path": "characters/Gung Gibang.md",
      "sha256": "dabeb9b56fa8894972c181c19a31e8e791c5b0dd65cc1b6ee5ac60a41ec9021f",
      "bytes": 1007
    },
    {
      "path": "characters/Hong Dao.md",
      "sha256": "f29d6e99103e7507f570b560a49296614a9c3f97bcf4e6488d939f9c27023275",
      "bytes": 1001
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "f5e3250bff869be3822b563e3593d6d9f06c7bb1ccf65b73a95c7f2e90776605",
      "bytes": 6933
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "c954fad64a00d9a4ce82384ad160ab62af7222720b55400b5224edb05552dbb5",
      "bytes": 30798
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "4d9b5ff19231a28127f1291f217bc9dbd824a88c54ef2fd6ac4178a9c60a70f9",
      "bytes": 622
    },
    {
      "path": "characters/Mae Jonghak.md",
      "sha256": "5c0a1f82985917956751b9867de1e4475af470539579208c5a2ad57bf34dc1f5",
      "bytes": 1477
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "19717732f14b59da0a933177727c2e01b984dbd668cb84ee3f6f3b3d0250ca07",
      "bytes": 80838
    }
  ],
  "estimated_tokens": 60982
}
-->

# Durable State Update — Chapter 313

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 313. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 20 concise items, `open_questions` to at most 8
items, and `temporary_decisions` to at most 8 items. Keep the serialized context
under 16384 UTF-8 bytes. Use only chapter
numbers through 313. `profile_updates` may replace one exact, uniquely occurring
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
  "chapter": 313,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 313,
    "continuity_sources": [313],
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
    "The Jin Family Escort Bureau and the Yongbong Escort Bureau are business competitors; the Yongbong Escort Bureau remains dominant in Shaanxi, while the Jin Family Escort Bureau reportedly has more than five branches.",
    "Ju Hwaran suspects an internal Yongbong Escort Bureau betrayal involving the leak of the Thousand-Year Snow Ginseng information and the attacks sustained over four months.",
    "Ju Hwaran told Heo Jun to watch Song Ilseom; Taekyung and Cheongpung also noticed Song Ilseom's hostile attention toward Taekyung.",
    "Song Ilseom is a Level 110 escort captain of the Yongbong Escort Bureau.",
    "Cheongpung is now known by the title Huashan Divine Dragon, bestowed after the Star-Array Grand Banquet.",
    "Taekyung's party has left Black Stone Stronghold and is traveling toward Xi'an while continuing the search for the Divine Physician.",
    "Baek Museong arrived alone at Xi'an Tower and identified himself as the direct Disciple of Huashan Sect Leader Heavenly Sword True Person."
  ],
  "continuity_sources": [
    312
  ],
  "open_questions": [
    "Is Song Ilseom involved in the Yongbong Escort Bureau's information leak and the repeated attacks?"
  ],
  "safe_through": 312,
  "temporary_decisions": [
    "Use Huashan Divine Dragon for 화산신룡.",
    "Use Xi'an Tower for 서안루."
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
| 베르체니 | **Vercheni** | Venerable Italian artisan family commissioned to make the Peace Guild's magical equipment. |
| 이탈리아 | **Italy** | Country associated with the Vercheni artisan family. |
| 원미구 | **Wonmi-gu** | District of Bucheon shown in Taekyung's televised caption. |
| 서울 외곽 순환도로 | **Seoul Outer Ring Expressway** | Expressway whose tollgate incident made Taekyung famous. |
| 톨게이트 영웅 | **Tollgate Hero** | Media nickname given to Jin Taekyung after the tollgate incident. |
| 황소자리 | **Taurus** | Zodiac sign Song Song uses as a nickname for Taekyung. |
| 뇌이버 | **Naver** | Source-spelling variant used in Hayeon's reference to the real-time search rankings. |
| 아홉 시 뉴스 데스크 | **Nine O'Clock News Desk** | KPS live news program where Taekyung is waiting to be interviewed. |
| 한국일보 | **Korea Daily** | Daily newspaper carrying a feature on Taekyung. |
| 고려일보 | **Goryeo Daily** | Daily newspaper carrying a feature on Taekyung. |
| 행복한 생각 | **Happy Thoughts** | Publication carrying a human-interest feature on Taekyung. |
| 시사 핫 토픽 | **Current Hot Topic** | Current-affairs publication. |
| 국회 말말말 | **Parliament’s Words of the Day** | Publication covering remarks made in Parliament. |
| 자유 애국당 | **Freedom Patriot Party** | Political party whose chairman makes the quoted remark. |
| KPS | **KPS** | Broadcaster carrying the Nine O’Clock News. |
| 아홉 시 뉴스 | **Nine O’Clock News** | KPS news program Taekyung appeared on. |
| 헤일리 뉴스 | **Hailey News** | Media outlet identified in the online comments. |
| ㅂㅎㅇ | **B.H.Y.** | Initials of a Hailey News reporter; no full name is given. |
| 오마이갓 뉴스 | **Oh My God News** | News outlet approaching Taekyung in the parking garage. |
| 주부 일간지 | **Housewives’ Daily** | Daily publication represented by Reporter Hong. |
| 생생 시사 토크 | **Vivid Current-Affairs Talk** | Current-affairs talk program approaching Taekyung. |
| 피터 필립 | **Peter Philip** | Swiss watchmaker credited with making the Universe-302. |
| 유니버스-302 | **Universe-302** | Luxury automatic mechanical watch used as Choi’s deterrent. |
| 제갈량 | **Zhuge Liang** | Historical strategist invoked in Taekyung’s comparison of Choi’s cleverness. |
| 스위스 | **Switzerland** | Country associated with the watchmaker. |
| 청와대 | **Blue House** | Presidential office mentioned in an online comment about proposed legislation. |
| 스타 길드 | **Star Guild** | Guild in Incheon acquired and renamed by Won Myunghoon. |
| 주간 헌터즈 | **Weekly Hunters** | Hunter magazine carrying Taekyung's interview. |
| 벙어리 삼룡이 | **Mute Samryong** | Title character of a well-known Korean short story. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 쫄보 | **Coward** | Song associated with Won Myunghoon. |
| 헌터를 몰라 | **I Don't Know Hunters** | Song associated with Won Myunghoon. |
| 탈주 | **Escape** | Song associated with Won Myunghoon. |
| 유니콘 차트 | **Unicorn chart** | Japanese music chart mentioned in relation to Won Myunghoon. |
| 원명훈 신드롬 | **Won Myunghoon Syndrome** | Taekyung's joking name for Won's former cultural influence. |
| 도원결의 | **Peach Garden Oath** | Oath Taekyung jokes that Jinho would want the three men to swear together. |
| A급 헌터 | **A-Rank Hunter** | System Achievement and Hunter status Taekyung receives in this chapter. |
| 아이튜브 | **iTube** | Live-streaming platform hosting the Hunter Association ceremony. |
| 태경좌 | **Taekyung the Lord** | Online nickname created by viewers during Taekyung's live broadcast. |
| 시벌좌 | **Lord Fuck** | Crude online nickname created from Taekyung's accidental broadcast profanity. |
| 라이칸스로프 | **Lycanthrope** | B-rank Gate monster species. |
| 은빛 갈기 라이칸스로프 | **Silver-Mane Lycanthrope** | Lv. 83 boss monster of The Lycanthrope’s Black Forest. |
| 라이칸스로프의 검은 숲 | **The Lycanthrope’s Black Forest** | B-rank Gate cleared in this chapter. |
| 도민수 | **Do Minsu** | A-rank star Hunter and Won Myunghoon’s close friend; died in the Myeongdong Station Mutated Gate Catastrophe. |
| 명동역 변이 게이트 대참사 | **Myeongdong Station Mutated Gate Catastrophe** | Eight-year-old Gate disaster in which Do Minsu and around thirty others died. |
| 소나무 위키 | **Sonamu Wiki** | Online wiki consulted about Won Myunghoon. |
| 종훈 | **Jonghun** | Personal name of Star Guild Team 1 Leader. |
| 블랙 와이번 | **Black Wyvern** | A-Rank Gate monster remembered by Taekyung. |
| 블랙 와이번의 둥지 | **The Black Wyvern’s Nest** | A-Rank Gate and destination of the joint raid. |
| 와이번 | **Wyvern** | High-tier dragonkin monster. |
| 드레이크 | **Drake** | High-tier dragonkin monster. |
| 용족 | **dragonkin** | Monster classification including wyverns and drakes. |
| 마지막 잎새 | **The Last Leaf** | Story referenced in Taekyung's comparison. |
| 만티코어 | **Manticore** | A-Rank Gate monster and original raid target. |
| 만티코어의 밀림 | **Manticore’s Jungle** | Original joint-raid location. |
| 예티의 목걸이 | **Yeti’s Necklace** | Cold-producing System Item lent by Won Myunghoon. |
| 한서불침 | **Unaffected by Cold and Heat** | Condition attributed to Taekyung after opening both vessels. |
| 상동역 변이 게이트 사건 | **Sangdong Station Mutated Gate incident** | Traumatic Gate incident Taekyung survived three years earlier. |
| 그린 와이번 | **Green Wyvern** | Lv. 97 A-Rank monster encountered during the joint raid. |
| 진우 | **Jinwoo** | Name called out by Im Kkeokjeong during the Wyvern attack. |
| 소원 | **Sowon** | Name called out by Im Kkeokjeong during the Wyvern attack. |
| 김종훈 | **Kim Jonghun** | Star Guild Team 1 Leader's personal name. |
| 오크 | **Orc** | Monster species. |
| 오크 워리어 | **Orc Warrior** | B-Rank Orc designation. |
| 블라디미르 스탈린 | **Vladimir Stalin** | Russian jewelry maker named by Team Leader Choi. |
| 프로즌 아이 | **Frozen Eye** | Necklace worn by Team Leader Choi. |
| 설원의 바람 | **Wind of the Snowfield** | Effect activated by Yeti's Necklace. |
| 트롤 | **Troll** | Monster species with extraordinary regenerative ability. |
| 북한 | **North Korea** | Country referenced in Taekyung's comparison. |
| 수령님 | **Supreme Leader** | Title used in Taekyung's North Korean TV comparison. |
| 마에스트로 | **maestro** | Conductor title used in Won's Guild-management analogy. |
| 디스패스 | **Dispass** | Celebrity-gossip site cited by Taekyung. |
| 네임드 몬스터 | **Named Monster** | Classification given to the Wyvern that killed the scouts. |
| 변이 게이트 | **Mutated Gate** | Gate classification identified at the raid site. |
| 레어 몬스터 | **Rare Monster** | Anomalously powerful monster designation introduced for monsters exceeding their expected Grade. |
| 피어 | **Fear** | Monster effect that overwhelms a target’s mental fortitude. |
| 힘껏 찌르기 | **Stab with All My Strength** | Taekyung’s descriptive alternate name for the spear strike he used against the Black Wyvern. |
| 김현수 | **Kim Hyunsu** | Four-month Hunter and first victim of the incident three years earlier; Taekyung’s deceased comrade. |
| 이혜림 | **Lee Hyerim** | Deceased comrade of Taekyung from the incident three years earlier. |
| 송동혁 | **Song Donghyeok** | Deceased comrade of Taekyung from the incident three years earlier. |
| 박상호 | **Park Sangho** | Deceased comrade of Taekyung from the incident three years earlier. |
| 김한웅 | **Kim Haneung** | Deceased comrade of Taekyung from the incident three years earlier. |
| 박광현 | **Park Gwanghyeon** | Deceased comrade of Taekyung from the incident three years earlier. |
| 홍천수 | **Hong Cheonsu** | Ten-year veteran Hunter and deceased comrade who saved Taekyung from goblins. |
| 기의 발현 | **Manifestation of Qi** | System Achievement completed by Taekyung. |
| 백독불침 | **Unaffected by a Hundred Poisons** | System effect granted to Taekyung's body. |
| 에어 브레스 | **Air Breath** | Unique dragonkin ability used by Carus. |
| 힐 | **Heal** | Healing spell cast by Carus. |
| 슬로우 | **Slow** | Spell cast five times in succession by Carus. |
| 카루스 | **Carus** | Name of the Black Wyvern. |
| 외눈박이 | **One-Eyed** | Epithet of Carus, who has only one eye. |
| 다크 바인딩 | **Dark Binding** | Spell cast by Carus. |
| 매직 애로우 | **Magic Arrow** | Spell cast by Carus. |
| 속박 마법 | **Binding Magic** | System description of Carus's thorny-vine spell. |
| 마비 독 | **Paralysis Poison** | Poison carried by Carus's binding vines. |
| 신경 독 | **Nerve Poison** | Poison carried by Carus's binding vines. |
| 중독 | **Poisoned** | System status abnormality caused by the poisons. |
| 네임드 몬스터 처치 | **Named Monster Defeated** | Achievement granted for killing Carus. |
| 파이어 레인 | **Fire Rain** | A-Rank mage spell used by Butler Kim. |
| 개보린 | **Dogvorin** | Taekyung's dog-themed pun on Gevorin, a Korean painkiller. |
| 대법원 | **Supreme Court** | Court invoked in Won Myunghoon's metaphor for an irreversible verdict. |
| 어스퀘이크 | **Earthquake** | Named spell cast by Butler Kim. |
| 헌터TV | **HunterTV** | Major Hunter-focused cable channel that conducts the exclusive live broadcast. |
| 합스부르폰 가 | **Hapsburphon family** | Long-established German family of equipment makers. |
| PSV-96K | **PSV-96K** | Concealed camera that evades detection magic and functions in unstable-Gate mana. |
| 검찰 | **prosecutors’ office** | Government prosecutorial institution that summons and investigates Taekyung. |
| 법무부 | **Ministry of Justice** | Government ministry whose Hunters could have accompanied the prosecutor. |
| 대한제국 | **Korean Empire** | Historical-era reference used in Taekyung’s joke. |
| 크리스티 | **Christie’s** | Auction house whose appraisers valued Carus’s remains. |
| 소더비 | **Sotheby’s** | Competing major auction house. |
| 고조선TV | **GojoseonTV** | Television outlet that reports the Christie’s auction. |
| 카타르 | **Qatar** | Country of Prince Cheonsur. |
| 천수르 | **Cheonsur** | Qatar’s prince who wins the auction for Carus’s remains. |
| 박형석 | **Park Hyeongseok** | Online commenter who identifies himself during the argument. |
| 낙양 | **Luoyang** | Historic city in Henan Province and the chapter’s setting. |
| 하남성 | **Henan Province** | Province containing Luoyang. |
| 회면 | **huimian noodles** | Famous Henan noodle dish served at the inn; explained in a footnote. |
| 백주 | **baijiu** | Strong distilled liquor ordered at the inn. |
| 동천파 | **Dongcheon Sect** | Long-established dark-path faction ruling Luoyang’s nights. |
| 동천방 | **Dongcheon Gang** | Source variant used in the description of Heukgeol’s epithet. |
| 흑걸 | **Heukgeol** | Lower-ranking Dongcheon Sect officer known as its lone beast. |
| 궁소 | **Gungsu** | Dark-path swordsman killed during the Dongcheon Sect’s initial attack. |
| 화주 | **strong liquor** | Liquor stored and consumed by the dark-path swordsmen. |
| 박도 | **broad-bladed saber** | Rough weapon swung by the bald swordsman. |
| 아미타불 | **Amitabha** | Buddhist invocation spoken by the unidentified arriving group. |
| 무명 | **Unnamed** | Dharma name given by Hong Dao; literally means having no name. |
| 독룡파 | **Poison Dragon Sect** | Dark-path faction mentioned as a possible origin of the monk. |
| 흑혈문 | **Black Blood Sect** | Dark-path faction mentioned as a possible origin of the monk. |
| 나한권 | **Arhat Fist** | Shaolin martial art used by Unnamed. |
| 숭산 | **Mount Song** | Mountain where Shaolin Temple is located. |
| 소실봉 | **Shaoshi Peak** | Peak of Mount Song that must be climbed to reach the Shaolin Abbot. |
| 지객당 | **Guest Reception Hall** | Shaolin area where visitors without a specific purpose must remain. |
| 관세음보살 | **Avalokiteshvara** | Buddhist invocation shouted by Unnamed during his attack. |
| 신성 | **Morning Star** | Term in the summons referring to the Master of Morning Star. |
| 계율원 | **Discipline Hall** | Shaolin disciplinary office that urges Hong Dao to return to a formal residence. |
| 녹옥불장 | **Green Jade Buddha Staff** | Ancient Shaolin sacred treasure carried by Hong Dao. |
| 천기 | **heavenly patterns** | Celestial patterns Hong Dao studies to perceive major changes and omens. |
| 태양권 | **Solar Fist** | Martial art mentioned in Taekyung's joke about Unnamed's forehead strike. |
| 천년독각사 | **Thousand-Year Poison Horned Snake** | Extremely venomous horned snake used to make Hong Dao's thirty-year-old liquor. |
| 비선 | **Hidden Thread** | Secret intelligence network and its chief hidden informant serving the Family Head. |
| 소선 | **Lesser Threads** | Informants operating beneath the Hidden Thread. |
| 황산파 | **Huangshan Sect** | Prestigious sect that has already collapsed. |
| 산주 | **Mountain Lord** | Anhui title for Jeok Cheongang as master of Mount Jiuhua. |
| 남궁 | **Namgung** | Surname of the family led by Namgung Ryong. |
| 남궁룡 | **Namgung Ryong** | Family Head of the Namgung family. |
| 은형술 | **concealment technique** | Peak-level technique used by the Hidden Thread to erase his presence. |
| 점혈 | **Pressure-Point Strike** | System-named technique used by Jeok Cheongang on Taekyung. |
| 수혈 | **Sleep Acupoint** | Acupoint whose successful strike prevents the target from resisting sleep. |
| 천급 | **Heaven-grade** | Highest classification in the Namgung family's intelligence system. |
| 창천 | **azure heaven** | The cloudless sky seen by Namgung Ryong. |
| 화왕 특제 금제단 | **Fire King's Special Restriction Pill** | System consumable that suppresses internal energy and reduces three physical stats for one week. |
| 화왕의 불지옥 수련-1 | **Fire King's Inferno Training-1** | Nonrefusable training Quest created when Jeok blasts Taekyung from the summit. |
| 화왕의 지옥불 수련-1 | **Fire King's Hellfire Training-1** | Source-title variant used for the completed Quest. |
| 근골 | **Muscles and Bones** | System attribute increased by 2 during the climb. |
| 만년 한철 | **Ten-Thousand-Year Cold Iron** | Spaced source variant for the chain material. |
| 일각 | **fifteen minutes** | Quarter of a shichen; used for the remaining completion time. |
| 화왕의 지옥불 수련-2 | **Fire King's Hellfire Training-2** | System Quest completed after the waterfall training. |
| 요지부동 | **Unmoving** | Achievement earned after the waterfall training. |
| 맷집 | **Toughness** | System attribute that changes into Endurance. |
| 인내 | **Endurance** | System attribute replacing Toughness. |
| 권각 수련 | **Fist-and-Foot Training** | Repeat Quest for basic fist-and-foot exercises. |
| 권각술 | **fist-and-foot martial arts** | Unlearned martial-arts category referenced by the System. |
| 열화동 | **Fire Gate Cavern** | Ancestral cavern where the Fire Gate Clan began and its legacy continues. |
| 열화의 계승자 | **Heir of the Fire Gate** | Quest generated when Jeok begins passing on the Fire Gate Clan's inheritance. |
| 문방사우 | **Four Treasures of the Study** | The brush, inkstone, ink, and paper used for calligraphy and painting. |
| 한림학사 | **Hanlin Academician** | Scholarly office used in Wipeng's teasing comparison. |
| 대화백 | **master painter** | Title used jokingly for an accomplished painter. |
| 해동 | **Haedong** | Traditional name for Korea. |
| 칠로군 | **Seven-Route Army** | Seven-pronged force led by Wipeng and the Jin Dragon Squad. |
| 황금 씨족 | **Golden Clan** | Traditional name for the ruling lineage descended from the khans. |
| 합비 | **Hefei** | City on the Jin Family's new escort-trade route. |
| 진가표국 | **Jin Family Escort Bureau** | New name for the former Seongun Escort Bureau under the Jin Family. |
| 잠룡출사 | **The Sleeping Dragon Enters Service** | Title of Jin Wikyung's planned painting. |
| 검미새 | **sword nut** | Taekyung's joking term for someone obsessed with swords. |
| 노환 | **infirmities of old age** | Jeok Cheongang's age-related illness. |
| 헨젤과 그레텔 | **Hansel and Gretel** | Fairy-tale siblings used in Taekyung's chained-iron-ball joke. |
| 남궁옥 | **Nangong Ok** | Namgung Ryong's only son, the Nangong Family's Lesser Family Head and the Sword Dragon. |
| 검룡 | **Sword Dragon** | Epithet of Nangong Ok; one of the Ten Dragons and Phoenixes. |
| 제왕검형 | **Emperor's Sword Form** | Sword form invoked by the Azure Sky Sword King. |
| 삼초살 | **Three-Move Kill** | Sudden Quest requiring Taekyung to withstand three moves. |
| 남만 | **Nanman** | Historical regional term used for the source of the imported ebony. |
| 오기조원 | **Five Qi Returning to Origin** | High martial realm displayed by Jeok Cheongang. |
| 잠룡 | **Hidden Dragon** | Epithet or metaphor for Jin Taekyung. |
| 검왕 | **Sword King** | Short form for the Azure Sky Sword King, Nangong Cheon. |
| 대성 | **Great Completion** | Completion stage of a martial technique. |
| 흑산채 | **Black Mountain Stronghold** | Bandit organization on a major route between Henan and Anhui. |
| 흑종필 | **Heuk Jongpil** | Leader of Black Mountain Stronghold. |
| 금와상단 | **Geumwa Merchant Group** | Merchant group targeted by Black Mountain Stronghold. |
| 녹림맹 | **Green Forest Alliance** | Bandit alliance receiving Black Mountain Stronghold’s tribute. |
| 묘안석 | **cat’s-eye stone** | Valuable stone used as an example of a profitable haul. |
| 성마대연 | **Demonic Grand Banquet** | Hypothetical banquet the Demonic Cult would hold if the Central Plains Murim had lost. |
| 여아홍 | **Yeoahong** | Traditional Chinese rice wine; literally Daughter's Red. |
| 절강성 | **Zhejiang Province** | Province where the Geumwa Merchant Group ranks among the top three merchant groups. |
| 적살부 | **Red-Killing Axe** | Epithet of Heuk Jongpil. |
| 송호 | **Song Ho** | Elderly martial artist known as the Thousand-Faced Fox. |
| 천면호리 | **Thousand-Faced Fox** | Epithet of Song Ho. |
| 개봉 | **Kaifeng** | City where the preliminary competition will be held. |
| 섬 | **seom** | Traditional Korean measure of rice. |
| 종리추 | **Jongni Chu** | Young Peak martial artist from Yunnan; conceals his sect. |
| 상승검 | **Always-Victorious Sword** | Jongni Chu's self-styled epithet, coined in this chapter. |
| 운남 | **Yunnan** | Region from which Jongni Chu comes. |
| 마이클 존슨 | **Michael Johnson** | False name Taekyung gives Jongni Chu. |
| 호철 | **Hocheol** | Jin Dragon Squad martial artist and Hyuk Mujin's subordinate. |
| 간장 | **Gan Jiang** | Legendary swordsmith named in comparison with Mo Ye. |
| 막야 | **Mo Ye** | Legendary swordsmith named in comparison with Gan Jiang. |
| 백염 | **White Flame** | Name of Jin Taekyung's newly forged spear. |
| 풍운전신 | **Wind-and-Cloud War God** | Jeok Cheongang's mistaken version of Gong Iljung's title. |
| 정력도왕 | **Virility Saber King** | Jeok Cheongang's insulting replacement title for the Thunderbolt Saber King. |
| 하북 팽가 | **Hebei Peng Family** | Family of the Thunderbolt Saber King. |
| 하북제일미 | **Hebei's greatest beauty** | Description of the Thunderbolt Saber King's great-grandson's wife. |
| 참회동 | **Repentance Cave** | Zhongnan Sect place of penance. |
| 철수신룡 | **Iron-Water Divine Dragon** | Title of Cheol Soo, a member of the Ten Dragons and Phoenixes. |
| 도곤 | **Dogon** | Title for a Peak-level gambler. |
| 곽철융 | **Kwak Cheolyung** | One of the three legendary Dogons. |
| 아귀 | **A-Gwi** | Legendary Dogon from Sichuan. |
| 짝귀 | **Jjak-Gwi** | Legendary Dogon from Guangdong. |
| 노르웨이 | **Norway** | Taekyung's temporary nickname for the huge foreign-looking applicant. |
| 호접문 | **Butterfly Sect** | Sect of the eliminated martial artist Jangyu. |
| 장유 | **Jangyu** | Martial artist eliminated during the fist-and-foot assessment. |
| 소당문 | **Sodang Sect** | Sect of the martial artist Gobul. |
| 고불 | **Gobul** | First Rate martial artist who passes the fist-and-foot assessment. |
| 장보고 | **Jang Bogo** | Historical Korean maritime commander used in Taekyung's joke about the Seafaring King. |
| 화왕의 분노 | **Fire King's Wrath** | Failure penalty for the Star-Array Grand Banquet Quest. |
| 파선권 | **Ship-Breaking Fist** | Named fist technique demonstrated by the Iron-Water Divine Dragon. |
| 멸염신권 | **Flame-Extinguishing Divine Fist** | Named fist technique Taekyung announces at the chapter's end. |
| 서역 | **Western Regions** | Region from which the glasses were imported. |
| 청성산 작두 | **Qingcheng Mountain Guillotine** | Epithet of the unnamed martial artist who cut off A-Gwi's wrist. |
| 도도 | **Dodo** | Term for the Star-Array Grand Banquet's major gambling matches. |
| 곤륜운룡 | **Kunlun Cloud Dragon** | Epithet of a Kunlun Sect young prodigy. |
| 후개 | **Successor Beggar** | Title of the Beggars' Sect successor competing in the preliminaries. |
| 혼뢰각 | **Hunroe Leg** | Epithet of the Guangxi Peak master specializing in leg techniques. |
| 신기묘룡 | **Divine Marvel Dragon** | Epithet of the Zhuge Clan's Lesser Family Head. |
| 금면공자 | **Gold-Faced Young Master** | Title of the unnamed gambler who bet on Taekyung. |
| 기관진식 | **mechanisms and formations** | Fifth preliminary assessment category. |
| 궁기방 | **Gung Gibang** | Beggars' Sect Successor Beggar and finalist. |
| 낭왕 | **Wave King** | One of the Ten Kings; already deceased. |
| 나한동 | **Arhat Cave** | Shaolin cave where Unnamed is preparing. |
| 항룡십팔장 | **Eighteen Dragon-Subduing Palms** | Beggars' Sect martial art mentioned by Gung Gibang. |
| 제갈무후 | **Zhuge Wuhou** | Honorific title for Zhuge Liang in the Three Visits allusion. |
| 유비 | **Liu Bei** | Historical ruler in the Three Visits to the Thatched Cottage allusion. |
| 삼고초려 | **Three Visits to the Thatched Cottage** | Allusion Zhuge Gyun uses to justify choosing the third option. |
| 천마신교 | **Heavenly Demon Divine Cult** | The Demonic Cult's self-styled formal name. |
| 흑수표 | **Black Water Dart** | Epithet of Taekyung's defeated main-event opponent. |
| 운룡대팔식 | **Cloud-Dragon Eight Forms** | Baek Woo's Kunlun movement technique. |
| 오태식 | **Oh Tae-sik** | Taekyung's joking alternate name for the Cloud-Dragon Eight Forms. |
| 권기 | **Fist Energy** | Projected martial energy produced by a fist technique. |
| 은영각 | **Hidden Shadow Pavilion** | Former Murim Alliance intelligence organization. |
| 은영각주 | **Chief of the Hidden Shadow Pavilion** | Office formerly held by Song Ho. |
| 연명검 | **Life-Sustaining Sword** | Nickname earned by Jongni Chu for repeatedly winning by a narrow margin. |
| 무적신검 | **Invincible Divine Sword** | Epithet of Zhuge Gyun's unidentified opponent. |
| 강풍 | **Kang Pung** | False name Cheongpung uses while disguised as the Invincible Divine Sword. |
| 암중살 | **Shadow Killer** | The Hidden Shadow Pavilion's finest agent. |
| 태원박가 | **Taiyuan Park Family** | Fabricated family identity Taekyung uses to bait Cheongpung. |
| 호남성 | **Hunan Province** | Province mentioned during Cheongpung's account of his travels. |
| 혼원도 | **Hunyun Saber** | Epithet of the Hebei Peng Family’s eldest grandson, defeated by Jin Taekyung in the quarterfinals. |
| 유운신룡 | **Willow-Cloud Divine Dragon** | Wudang direct disciple and Cheongpung’s quarterfinal opponent. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 승패병가지상사 | **Victory and defeat are simply part of war** | Common saying Jeok Cheongang uses while taunting the Thunderbolt Saber King. |
| 송문고검 | **Pine-Pattern Ancient Sword** | Willow-Cloud Divine Dragon’s sword. |
| 태청검법 | **Great Clarity Sword Technique** | Wudang sword technique used by the Willow-Cloud Divine Dragon. |
| 태극혜검 | **Taiji Wisdom Sword** | Wudang’s supreme sword technique. |
| 매화삼십육검 | **Thirty-Six Plum Blossom Swords** | Huashan sword technique used by Cheongpung. |
| 타구봉법 | **Dog-Beating Staff Technique** | Beggars’ Sect staff technique. |
| 반로환동 | **Returned to Youth** | Possible explanation for an apparently young Supreme Peak master. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 극상승의 안법 | **ultimate eye technique** | Advanced visual technique Cheongpung learned from Mae Jonghak. |
| 허초 | **feint** | Deceptive attack Jongni Chu says he used against Cheongpung. |
| 심력 | **mental strength** | Inner mental capacity injured by Jongni Chu's feint. |
| 좌장 | **presiding chair** | Authority overseeing the Star-Array Grand Banquet. |
| 천산 | **Tianshan** | Mountain region identified as the Demonic Cult's headquarters. |
| 천산산맥 | **Tianshan Mountains** | Mountain range associated with the Demonic Cult. |
| 천라지망 | **net over heaven and earth** | Jeok Cheongang's figurative threat to pursue a culprit everywhere. |
| 마공 | **demonic martial arts** | Martial arts that appear to defy common principles. |
| 팔 성 | **eighth stage** | Current stage of Taekyung's Qi Sense Skill. |
| 화룡 | **fire dragon** | Fire-dragon image within Taekyung's dantian that awakens before the duel. |
| 심사관 | **Judge** | Official supervising the Star-Array Grand Banquet duels. |
| 화륜각 | **Flame Wheel Kick** | Taekyung's blue-flame kicking technique. |
| 화룡신창 | **Fire Dragon Divine Spear** | Taekyung's spear technique, at the seventh stage in this chapter. |
| 사량발천근 | **Four Ounces Deflecting a Thousand Catties** | Principle Jongni Chu cites for redirecting force rather than opposing it directly. |
| 만리추행 | **Myriad-Mile Pursuit** | Epithet of the Beggars' Sect Leader and master of movement techniques. |
| 염화일로 | **Flamefire Path** | Fire Gate Clan signature movement technique; Jeok Cheongang has reached its ninth stage. |
| 허공답보 | **Stepping on Empty Air** | Technique that allows Jongni Chu to move through empty air as if climbing invisible stairs. |
| 명문혈 | **Mingmen acupoint** | Acupoint into which Jeok Cheongang sends internal energy while treating Hong Dao. |
| 석가 | **Shakyamuni** | Buddhist figure invoked by Hong Dao in his earlier conversation with Jeok Cheongang. |
| 한수 | **Han Su** | Scholar-like Dark Heaven operative who kills a Hidden Shadow Pavilion messenger. |
| 염호 | **Flame Tiger** | Red-bearded Dark Heaven operative and Han Su's longtime friend. |
| 불장 | **Buddhist Staff** | Generic term in Hong Dao's final words; the specific treasure is 녹옥불장. |
| 굉천 | **Hongcheon** | Hong Dao's youngest Junior Brother; Supreme Peak Shaolin master defending the temple. |
| 백중 | **Baekjung** | Traditional Buddhist observance during which the Shaolin attack occurs. |
| 오악 | **Five Sacred Mountains** | Mountain grouping that includes Mount Song. |
| 태산북두 | **Mount Tai and Northern Dipper of the Murim** | Honorific description of Shaolin's standing in the Murim. |
| 계인 | **Buddhist precept seals** | Seals carved into the foreheads of Shaolin martial monks. |
| 백보신권 | **Hundred-Step Divine Fist** | Hongcheon's named martial art. |
| 천주 | **Lord of Heaven** | Authority invoked by the masked attackers. |
| 음양쌍괴 | **Yin-Yang Twin Freaks** | Shared epithet of Flame Tiger and Han Su. |
| 범공 | **Beomgong** | Dharma name of a Shaolin monk killed by Han Su during the Great Faction War. |
| 면벽동 | **Face-Wall Cave** | Shaolin cave where Unnamed is located. |
| 음귀 | **Yin Ghost** | Han Su's epithet. |
| 사대금강 | **Four Great Vajras** | Four elite Shaolin martial monks killed by Han Su. |
| 장경각 | **Scripture Depository** | Shaolin repository whose martial arts manuals the attackers intend to burn. |
| 살문 | **Killing Gate** | Command given while the Hundred and Eight Arhats Formation is deployed. |
| 계도 | **precept blades** | Blades carried by the Hundred and Eight Arhats. |
| 선장 | **Zen staffs** | Staff weapons carried by the Hundred and Eight Arhats. |
| 백팔나한 | **Hundred and Eight Arhats** | Shaolin's elite formation unit of 108 martial monks. |
| 백팔나한진 | **Hundred and Eight Arhats Formation** | Formation used by the Hundred and Eight Arhats. |
| 폭혈마공 | **Exploding Blood Demonic Art** | Demonic art used by masked attackers as a battlefield self-detonation technique. |
| 부동심 | **Unshakable Mind** | Mental discipline Hongcheon is accused of abandoning when he loses composure. |
| 음한지공 | **Yin-Cold Technique** | Han Su's extreme cold-based internal technique. |
| 삼도천 | **Sanzu River** | Buddhist river associated with the boundary between life and death; footnote on first use. |
| 혈주 | **Blood Lord** | Title of the unidentified young man encountered by Han Su. |
| 진천뢰 | **Heaven-Shaking Thunder** | Powerful gunpowder explosive named in the Blood Lord's false threat to lure Hong Dao away. |
| 사성 | **Four Saints** | Rank the Blood Lord says Jeok Cheongang might have attained if the Great Faction War had continued another year. |
| 염라 | **Yama** | Buddhist lord of the underworld invoked as the one awaiting the dead. |
| 절체절명 | **Life-or-Death Crisis** | Sudden System Quest forcibly accepted during the confrontation at Mount Song. |
| 노야 | **Old Master** | Taekyung's private address for Jeok Cheongang. |
| 천독마군 | **Heaven-Poison Demon Lord** | Archfiend of the Heavenly Demon Divine Cult and former second-in-command of the Demonic Cult. |
| 혈귀검마 | **Blood Ghost Sword Demon** | Title Song Ho mistakenly attributes to Mae Jonghak before recognizing him as Jongni Chu. |
| 태원 진가 | **Jin Family of Taiyuan** | Source-spaced form of the Jin Family's name. |
| 토토 | **Toto** | Gambling or lottery reference contrasted with Dodo in Taekyung's joke. |
| 낙양괴의 | **Luoyang Strange Physician** | Renowned Central Plains physician; eccentric and fiercely temperamental, he examined Jeok Cheongang. |
| 염왕채 | **Yama's Debt** | Taekyung's joking term for a ruinous loan or loan-shark debt. |
| 골렘 | **Golem** | Magical rock-based monster classification. |
| 스톤 골렘 | **Stone Golem** | A-rank stone-bodied monster faced by the rookie Hunters. |
| 아이언 골렘 | **Iron Golem** | Higher-ranking golem type appearing in a group after the Stone Golem raid. |
| 헤이스트 | **Haste** | Buff spell cast by Song Song. |
| 스트렝스 | **Strength** | Strength-enhancing buff spell cast by Song Song. |
| 힐링 | **Healing** | Healing spell cast by Song Song. |
| 파이어 월 | **Fire Wall** | Fire spell cast by Butler Kim. |
| 내가중수법 | **Inner-Family Heavy Hand** | Taekyung's joking comparison for his mother's painful palm strike. |
| 모친신장 | **Mother's Palm Strike** | Taekyung's humorous name for the beating delivered by his mother. |
| 국정원 | **NIS** | South Korea's National Intelligence Service, mentioned in Taekyung's joke. |
| 노재헌 | **No Jaehun** | Middle-school student from the adjacent class, remembered as tall and boastful about working out. |
| 선웅제 | **Seon Woongje** | Taekyung's middle-school classmate who fought with No Jaehun. |
| 한국대 | **Hankuk University** | Short form for the country's most prestigious university; Jihoon's university. |
| 한국대학교 | **Hankuk University** | Full form of the university attended by Jihoon. |
| 게이트 관리청 | **Gate Management Agency** | Agency that provides Taekyung's VIP limousine. |
| 8학군 | **School District 8** | Prestigious Gangnam education district associated with affluent families and elite schools. |
| 김진수 | **Kim Jinsoo** | Peace Guild rookie who graduated first in the training camp’s B-rank course. |
| 블랙 헌터 | **Black Hunter** | Unregistered Awakened person who has received systematic training comparable to a Hunter. |
| 미등록자 | **unregistered Awakened person** | Awakened person who fails to register with the Association within the designated period. |
| 특수 치료 병동 | **Special Treatment Ward** | Hospital ward where healers, rather than ordinary doctors, treat severe injuries. |
| 통합당 | **United Party** | Political party identified in the article about Yoon Seoyoon. |
| 윤서윤 | **Yoon Seoyoon** | United Party Supreme Council member and assemblywoman named in a political article. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 임영준 | **Im Yeongjun** | Level 95 A-rank Black Hunter concealed as a rural resident. |
| 세 얼간이 | **Three Idiots** | Taekyung's mocking collective nickname for three acquaintances. |
| 멸천신권 | **Heaven-Destroying Divine Fist** | Taekyung's full-power fist technique used to destroy the mansion's defensive barriers; distinct from 멸염신권. |
| 한남동 | **Hannam-dong** | District where Park Tae Seop's mansion is located. |
| 11팀 | **Team 11** | Myeongdong Guild's officially nonexistent team of Black Hunters. |
| 김철수 | **Kim Cheol Soo** | C-rank junior Hunter in Myeongdong Guild's Security Team. |
| 1팀 | **Team 1** | Myeongdong Guild's elite team. |
| 이민수 | **Lee Minsu** | C-rank Hunter in Myeongdong Guild's Security Team; distinct from Kim Minsu. |
| 김 실장 | **Manager Kim** | Park Tae Seop’s security manager; his phone is used by Choi Minwoo. |
| 그분 | **that person** | Unidentified figure whom Jihoon reveres and credits with disabling cameras and microphones. |
| 어른폰 | **AdultPhone** | Taekyung’s Korean pun on iPhone; retain the child/adult explanation in a footnote. |
| 행신동 불닭볶음손 | **Haengsin-dong Fire-Chicken Stir-Fried Hand** | Taekyung's former nickname for his painful hand strike; the translation preserves the buldak-bokkeum-myeon/son pun. |
| 산군 | **mountain lord** | Traditional epithet for a tiger; retain an explanatory footnote on first use. |
| 석 팀장 | **Team Leader Seok** | Lee Jungryong's security-team leader and direct Disciple. |
| 고준 | **Go Jun** | Personal name of Team Leader Seok; Lee Jungryong's prized Disciple. |
| 준이 | **Jun** | Family nickname used in the form Jun's dad. |
| 석고준 | **Go Jun** | Source full-name form for the established Go Jun, also known as Team Leader Seok. |
| 소영 | **Soyeong** | Team Leader Choi's deceased mother and Cheon Taemin's daughter. |
| 슬레이어 | **Slayer** | Cheon Taemin's title after killing the Demon King. |
| 마왕 | **Demon King** | The being Cheon Taemin killed. |
| 도련님 | **Young Master** | Address used for Team Leader Choi by Butler Kim. |
| 한강 | **Han River** | River associated with the bridge-collapse incident Lee Jungryong recalls. |
| 마포대교 | **Mapo Bridge** | Bridge that collapsed when Kim Hwajong saved Lee Jungryong eighteen years earlier. |
| 비급제작 | **Martial Arts Manual Creation** | System Skill for creating martial arts manuals; requires at least 300 sheets of A4 paper. |
| 마나 연공법 | **Mana Cultivation Method** | Modern Hunter cultivation method recognized by Team Leader Choi and Butler Kim. |
| 고양진가 | **Jin Family of Goyang** | Taekyung's joking modern-world counterpart to the Jin Family of Taiyuan. |
| 2차 각성자 | **Second Awakener** | Hunter classification for someone who has awakened a second time. |
| 진기도인 | **True Qi Guidance** | System-named method for guiding another person's internal energy. |
| 소주천 | **Small Circulation** | Circulation of qi according to the Jin Family's Cultivation Technique. |
| 일주천 | **complete circulation** | Completion of one full qi circulation. |
| 등짝, 등짝을 보자! | **Back, Back—Let's See Your Back!** | Peak-grade repeat Quest title. |
| 난 소화한 공력의 반만 가져가 | **I'll Take Only Half the Internal Energy I Digest** | Sudden Quest title generated in Team Leader Choi's dantian. |
| 백년설삼 | **Hundred-Year-Old Snow Ginseng** | Elixir whose undigested internal energy remained in Taekyung's dantian. |
| 삼화취정 | **Three Flowers Gather at the Crown** | Near-completed phenomenon associated with entering the Supreme Peak realm. |
| 무아지경 | **Trance** | State Taekyung briefly enters during the energy digestion. |
| 내가고수 | **I'm a Master** | System Title granted to Taekyung. |
| 이순신 | **Admiral Yi Sun-sin** | Historical admiral invoked in Taekyung's comparison. |
| 명량대첩 | **Battle of Myeongnyang** | Historical naval victory used in Taekyung's comparison. |
| 수련자 | **Trainee** | System Title replaced in this chapter. |
| 훈련 교관 | **Training Instructor** | System Title awarded after several trainees reach One Star. |
| 킹태경 | **King Taekyung** | Online nickname praising Taekyung. |
| 로그인 무림 | **Login Murim** | Web novel recommended in the Hunter community comments. |
| 제로빅 | **Zerobic** | Name used in a forum joke about the recommended web novel. |
| 둘리 | **Dooly** | Korean cartoon character referenced in the goodwill proverb. |
| 흑마법사의 검은 숲 | **Black Wizard’s Black Forest** | A-rank Gate ruled by a black wizard or necromancer. |
| 게이트 공략 | **Gate Raid** | Quest automatically generated upon entering the Gate. |
| 흑마법사 | **black wizard** | Ruler or magical classification associated with the Gate. |
| 네크로맨서 | **necromancer** | Alternate description of the black wizard ruling the Gate. |
| 도사견 | **Tosa mastiff** | Taekyung’s nickname for the veteran third-week trainees. |
| 댕댕이 | **pup** | Taekyung’s nickname for first-day trainees. |
| 피리 부는 사나이 | **the Pied Piper** | Nickname for Taekyung when he lures monsters toward the Guild formation. |
| 구울 | **Ghoul** | Undead monster species. |
| 스켈레톤 | **Skeleton** | Undead monster species. |
| 좀비 | **Zombie** | Undead monster species. |
| 언데드 몬스터 | **Undead Monster** | Classification for the cursed dead in the Gate. |
| 스켈레톤 솔져 | **Skeleton Soldier** | Skeleton subtype. |
| 메이지 | **Mage** | Skeleton subtype mentioned alongside Soldiers and Warriors. |
| 워리어 | **Warrior** | Skeleton subtype mentioned alongside Soldiers and Mages. |
| 스켈레톤 나이트 | **Skeleton Knight** | A-rank undead monster that commands lower-level skeletons. |
| 골검 | **Bone Sword** | Sword wielded by the Skeleton Knights. |
| 스켈레톤 워로드 | **Skeleton Warlord** | Level 105 undead monster created when the leading Skeleton Knight transforms. |
| 정몽주 | **Jeong Mong-ju** | Historical Korean scholar-official referenced through the Warlord’s quotation. |
| 단심가 | **Song of My Single Heart** | Poem associated with Jeong Mong-ju and unwavering loyalty. |
| 통합 언어 팩 | **Unified Language Pack** | System function that lets Taekyung understand demon-world speech. |
| 서울지부 협회장 | **Seoul Branch President** | Hunter Association official overseeing the rescue response at the Black Forest. |
| 서울 협회장 | **Seoul Branch President** | Source variant for the Seoul Branch President. |
| 스켈레톤 아처 | **Skeleton Archer** | Skeleton subtype defeated during the Warlord's EXP harvest. |
| 서울 중앙 협회장 | **Seoul Branch President** | Hunter Association official who delayed the rescue response and authorized the Peace Guild's entry. |
| 경호팀장 | **Head of Security** | Go Jun's security-team office under Lee Jungryong. |
| 이우중 | **Lee Woojoong** | Seoul Branch President of the Hunters Association. |
| 서울 중앙지부 헌터 협회장 | **Seoul Branch President** | Source title for Lee Woojoong; variant of the established Seoul Association title. |
| 열화 | **Blazing Flame** | Lineage term in Taekyung's declaration as the Fire King's successor. |
| 소르코바체 | **Sorkovache** | Russian furniture master credited with making Team Leader Choi's seventeenth-century-style imperial sofa. |
| 존슨 | **Johnson** | Co-host of the American talk show that replays Taekyung's viral interview. |
| 코난 | **Conan** | Host of the American talk show discussing Taekyung's viral interview. |
| 워로드몬 | **Warlordmon** | Taekyung's mocking nickname for the Skeleton Warlord. |
| CNM | **CNM** | American broadcaster requesting an interview with Taekyung. |
| BCC | **BCC** | British broadcaster offering Taekyung a live special-guest interview. |
| 러시아 | **Russia** | Country associated with Sorkovache and the imperial-style sofa. |
| 미국 | **United States** | Country associated with the talk show and CNM. |
| 영국 | **United Kingdom** | Country associated with BCC. |
| 전광석화 | **Quick Attack** | Warlordmon’s rapid-movement command; used as a Pokémon-style gag. |
| 전광 | **Quick Attack** | Shortened form of Warlordmon’s rapid-movement command. |
| 몸통박치기 | **Body Slam** | Comic attack command Taekyung gives Warlordmon. |
| 수능 | **college entrance exam** | National university entrance examination taken by Hayeon. |
| 내신 | **school grades** | School-record grades referenced in Taekyung’s insult. |
| 파블로프 | **Pavlov** | Reference to Pavlov’s dogs. |
| 중국 | **China** | Country from which Team Leader Choi’s video originates. |
| 몬스터 웨이브 | **Monster Wave** | Catastrophic release of monsters when Gate mana exceeds its capacity. |
| 리치 | **Lich** | Named Monster; fallen archmage and apex undead monster. |
| 공안 무력부 | **Public Security Armed Forces Division** | Chinese state Hunter force deployed against the Monster Wave. |
| 오성홍기 | **Five-Starred Red Flag** | China's national flag. |
| 쓰촨성 | **Sichuan Province** | Source spelling variant of the established Sichuan location. |
| 난충시 | **Nanchong City** | City near the disaster site shown in the reconnaissance footage. |
| 중화인민공화국 | **People's Republic of China** | Formal country name shouted by the Chinese Hunters. |
| 중앙위원회 총서기 | **General Secretary of the Central Committee** | Office held by Xiao Yang. |
| 빙빙 | **Bingbing** | Name or nickname of the child in the Monster Wave footage. |
| 샤오 양 | **Xiao Yang** | General Secretary of China's Central Committee who specifically requests Taekyung's participation. |
| 백한성 | **Baek Hanseong** | Twenty-seventh President of Korea and youngest president elected in Korean history. |
| 대통령 | **President** | Title for Korea's head of state. |
| 대통령 각하 | **Mr. President** | Formal address for the President. |
| 주석 | **Chairman** | Political title used for Xiao Yang. |
| 중국 공산당 | **Chinese Communist Party** | China's ruling political party. |
| 중국 중앙위원회 | **China's Central Committee** | Chinese Communist Party leadership body referenced in the crisis response. |
| 중앙 군사 위원회 | **Central Military Commission** | Chinese military leadership body that requested Lee Jungryong's participation. |
| 인민해방군 | **People's Liberation Army** | Chinese military deployed to seal off the catastrophe area. |
| 주한 중국 대사 | **Chinese ambassador to Korea** | Diplomatic representative who met Lee Jungryong secretly. |
| 포케불프 | **Focke-Wulf** | German aircraft manufacturer. |
| 종석이 아저씨 | **Chairman Jongseok** | Taekyung's joking misrendering of Chairman Xiao Yang's title and name. |
| 보잉 747-8 VIP | **Boeing 747-8 VIP** | Chinese private jet used for the Sichuan response. |
| 중국 중앙 위원회 | **China's Central Committee** | Source-spaced variant of the established Chinese Central Committee title. |
| 첫이슬 후레쉬 | **First Dew Fresh** | Soju brand served aboard the private jet. |
| 청두 | **Chengdu** | Administrative capital of Sichuan Province and destination airport city. |
| 마계어 | **Demon Realm language** | Language spoken by monsters from the Demon Realm. |
| 국제 게이트 연구소 | **International Gate Research Institute** | Research body studying the increase in Gate mana. |
| 게이트 마력 급증 조사 결과 | **Investigation Results: Sudden Increase in Gate Mana** | Title displayed on Choi Minwoo's tablet. |
| 도쿄핫 | **Tokyo Hot** | Adult-video studio referenced in Taekyung's insult; footnoted. |
| 도쿄루 | **Tokyo-ru** | Red-light establishment referenced in Taekyung's joke. |
| 미미 | **Mimi** | Worker at Honghwaru referenced in Taekyung's joke. |
| 키라라 | **Kirara** | Worker at Tokyo-ru referenced in Taekyung's joke. |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 의선 | **Medicine Immortal** | Alternate sobriquet for the Divine Physician. |
| 홍길동 | **Hong Gil-dong** | Legendary Korean outlaw invoked in Taekyung's joke about the Divine Physician. |
| 오씨 | **Oh** | Surname form used in the clue identifying the Luoyang Strange Physician. |
| 오배자 | **Chinese gallnut** | Medicinal ingredient named in the Divine Physician's clue. |
| 신 서방 | **Mr. Shin** | Name form used in the System Quest targeting the Divine Physician. |
| 당문 | **Tang Clan** | Short form for the Sichuan Tang Clan. |
| 아미 | **Emei** | Short form for Emei Sect. |
| 아미파 | **Emei Sect** | Murim sect in Sichuan. |
| 청성 | **Qingcheng** | Short form for Qingcheng Sect. |
| 국자감 | **Guozijian** | The empire's highest educational institution. |
| 제갈공후 | **Zhuge Gonghu** | Former Murim Alliance Chief Strategist and deceased member of the Ten Kings. |
| 팽 | **Peng** | Surname form for the Thunderbolt Saber King, Peng Cheolhu. |
| 화란 | **Hwaran** | Familiar short form of Ju Hwaran. |
| 주호군 | **Ju Hogun** | Ju Hwaran's father and former leader of the Yongbong Escort Bureau. |
| 석 표두 | **Chief Escort Seok** | Yongbong Escort Bureau Chief Escort and the thirty-third casualty of the current escort journey. |
| 총 표두 | **Chief Escort** | Senior escort-bureau office held by Heo Jun. |
| 만리추풍신법 | **Myriad-Li Chasing Wind Movement Technique** | Beggars' Sect movement technique known for speed. |
| 연검 | **flexible sword** | Ju Hwaran's weapon. |
| 쟁자수 | **caravan porter** | Porters who lead the escort caravan's horses and carts. |
| 녹림도 | **Green Forest bandit** | Bandit belonging to the Green Forest Alliance. |
| 흑석산 | **Black Stone Mountain** | Mountain named for its black stones and located on the route to Mount Zhongnan. |
| 흑석채 | **Black Stone Stronghold** | A powerful Green Forest Alliance stronghold led by Heavenly Axe. |
| 십팔채 | **Eighteen Strongholds** | Short form for the Green Forest Alliance's eighteen major strongholds. |
| 송일섬 | **Song Ilseom** | Young escort captain of the Yongbong Escort Bureau; distinct from Song Il of Zhongnan. |
| 노필중 | **Noh Piljung** | Middle-aged escort captain and member of the Dragon-Phoenix Three Escorts. |
| 미향이 | **Mihyang** | Yongbong Escort Bureau maid who relayed rumors about Song Ilseom. |
| 용봉삼표 | **Dragon-Phoenix Three Escorts** | Collective title for the Yongbong Escort Bureau's three outstanding escort captains. |
| 천년설삼 | **Thousand-Year Snow Ginseng** | Secret Zhongnan Sect cargo; a fully digested specimen can grant a full jiazi of internal energy. |
| 유엽도 | **willow-leaf saber** | Saber wielded by Song Ilseom. |
| 살인멸구 | **Silencing the Witnesses** | Killing witnesses to prevent a secret from being exposed. |
| 방열 | **Bangyeol** | Personal name of Heavenly Axe; Level 93 Peak master and leader of Black Stone Stronghold. |
| 버뮤다 삼각지대 | **Bermuda Triangle** | Taekyung's joking collective label for the three companions descending the hill. |
| 용봉표국의 위기 | **Crisis of the Yongbong Escort Bureau** | Sudden Quest accepted and completed by Taekyung. |
| 천력부 처치 | **Defeat Heavenly Axe** | Quest objective completed when Taekyung kills Bangyeol. |
| 흑석채 제압 | **Subdue Black Stone Stronghold** | Quest completed when the surviving bandits surrender. |
| 화산신룡 | **Huashan Divine Dragon** | Title given to Cheongpung after the Star-Array Grand Banquet. |
| 서안루 | **Xi'an Tower** | Prominent pleasure house in Xi'an. |
| 백 씨 | **Baek** | Surname form used when Baek Museong introduces himself. |

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
| 진태경 | 성진호 | junior_to_older_friend | Jinho | casual-but-junior | Spoken 형 may stay hyung; narration uses Jinho. Jinho is three years older. |
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
| 임꺽정 | 최 팀장 | guild_member_to_team_leader | Team Leader Choi | formal-polite | Greets Choi after returning from vacation. |
| 임꺽정 | 김 집사 | older_guild_member_to_guild_master | Kim hyung, then Guild Master | casual-but-respectful and self-correcting | Initially uses the familiar hyung address before correcting himself to Butler Kim's nominal Guild Master title. |
| 진태경 | 원명훈 | younger_brother_to_older_friend | hyung | casual-but-junior | Taekyung asks Won to speak casually and adopts hyung after they establish a friendly younger-brother relationship. |
| 원명훈 | 진태경 | older_friend_to_younger_brother | Taekyung | casual-affectionate | Won calls Taekyung 태경아 and welcomes him as a good younger brother. |
| 부천 헌터 협회장 | 진태경 | Hunter_Association_president_to_new_A-rank_Hunter | Mr. Jin Taekyung | formal-polite | Addresses Taekyung during the live A-Rank Hunter certification ceremony. |
| 최 팀장 | 원명훈 | Guild team leader to visiting Guild CEO | Mr. Won Myunghoon | formal-polite and probing | Choi questions Won about his eight-year absence and recruitment offer. |
| 원명훈 | 최 팀장 | visiting Guild CEO to Peace Guild team leader | Team Leader | formal-polite and deferential | Won asks Choi for permission to conduct a joint raid. |
| 원명훈 | 1팀장 | Star Guild CEO to Team 1 Leader | Team Leader 1; Jonghun | blunt-commanding | Won first uses the subordinate’s title, then switches to his personal name while ordering him to stay alert. |
| 1팀장 | 원명훈 | Star Guild Team 1 Leader to CEO | CEO | formal-deferential | Repeatedly addresses Won as 대표님 during the phone call. |
| 1팀장 | 진태경 | Star Guild Team 1 Leader to visiting Hunter | Hunter Jin Taekyung | formal-polite and flattering | Uses 진태경 헌터님 while praising Won Myunghoon's Aura. |
| 원명훈 | 김종훈 | Guild CEO to longtime subordinate | Jonghun | familiar and threatening | Uses Jonghun's personal name while rebuking him and warning him to stay focused. |
| 최 팀장 | 진태경 | guild_team_leader_to_guild_member | Mr. Jin Taekyung | formal-polite | Uses the full-name form 진태경 씨 while calling Taekyung during the emergency. |
| 홍천수 | 진태경 | older_comrade_to_younger_comrade | Taekyung | affectionate-casual | His remembered final words address Taekyung familiarly while ordering him to go ahead. |
| 진태경 | 홍천수 | younger_comrade_to_older_comrade | Cheonsu hyung | casual-but-junior | Taekyung called Hong Cheonsu hyung after being saved from goblins. |
| 카루스 | 진태경 | hostile monster to human enemy | human | halting and hostile | Carus addresses Taekyung as the human who took his eye. |
| 진태경 | 카루스 | hostile_enemy | Wyvern | hostile-casual | Taekyung addresses Carus as Wyvern while taunting him during their final battle. |
| 진태경 | 담당 검사 | interview_subject_to_prosecutor | Prosecutor | polite | Taekyung uses 검사님 while discussing the investigation. |
| 담당 검사 | 진태경 | prosecutor_to_investigated_Hunter | Mr. Jin Taekyung | formal-polite | The prosecutor uses 진태경 씨 while discussing the self-defense issue and thanking Taekyung. |
| 하연 | 김정희 | daughter_to_mother | Mom | casual-familiar | Hayeon calls 엄마 while reporting that Taekyung hit her. |
| 무명 | 거한 | monk_to_attacking_dark_path_officer | Benefactor | deferential but frightened | Uses 시주 while pleading with the officer and insisting that he started the attack. |
| 무명 | 진태경 | newly_met_monk_to_benefactor | Benefactor | formal-polite | Uses 시주 while asking Taekyung's name. |
| 무명 | 적천강 | junior_monk_to_legendary_martial_master | Great Hero Jeok Cheongang | formal-deferential | Identifies Jeok by the title Fire King and the honorific 대협. |
| 무명 | 굉도 | disciple_to_master | Master | deferential | Refers to Hong Dao as 스승님 while explaining his Dharma name and training. |
| 적천강 | 굉도 | old_friends | Hong Dao | familiar and teasing | Uses Hong Dao's personal name in their casual reunion. |
| 굉도 | 적천강 | old_friends | Fire Gate Sect Leader | familiar and teasing | Teases Jeok as the carefree Fire Gate Sect Leader. |
| 굉도 | 무명 | master_to_disciple | Disciple | affectionate and familiar | Hong Dao addresses Unnamed as 제자야 while discussing his residence. |
| 굉도 | 진태경 | senior_monk_to_guest_benefactor | Benefactor | formal-polite and probing | Hong Dao repeatedly addresses Taekyung as 시주 while identifying him as the Master of Morning Star. |
| 호위 | 남궁룡 | guard_to_family_head | Family Head | formal-deferential | The guards kneel and greet Namgung Ryong after he exits the pavilion. |
| 홍가 | 적천강 | frightened_stranger_to_overwhelming_martial_master | Mountain Spirit | fearful and pleading | The herbalist mistakes Jeok Cheongang for a mountain spirit and repeatedly begs for help. |
| 남궁룡 | 적천강 | family_head_to_legendary_martial_master | Fire King | formal-deferential | Namgung Ryong accepts three hundred silver nyang as compensation for offending Jeok Cheongang. |
| 시비 | 진태경 | household_servant_to_visiting_young_hero | Young Hero Jin | formal-polite | The maid summons Taekyung to meet the Family Head. |
| 젊은 호위 | 진태경 | family_guard_to_visiting_young_hero | Young Hero | formal but firm | The young guard questions Taekyung's iron balls and orders him to disarm. |
| 남궁룡 | 진태경 | Family Head to younger visiting martial artist | you | formal-but-familiar | Namgung Ryong uses 자네 while asking Taekyung to stop the duel. |
| 진태경 | 남궁룡 | younger visiting martial artist to Family Head | Family Head | formal-polite | Taekyung addresses Namgung Ryong as 가주님 while acknowledging his inability to stop his father. |
| 진태경 | 남궁천 | junior martial artist to legendary martial master | Great Hero Nangong Cheon | formal-deferential | Taekyung uses the title and honorific 대협 when formally greeting the Azure Sky Sword King. |
| 남궁천 | 진태경 | legendary martial master to audacious junior | you / brat | blunt and intimidating | Namgung Cheon uses 네 녀석 and 놈 while testing and threatening Taekyung. |
| 남궁옥 | 진태경 | hostile young family heir to visiting martial artist | you bastard | hostile and enraged | Nangong Ok confronts Taekyung after overhearing the conversation with his father. |
| 진태경 | 남궁옥 | older martial artist to hostile young family heir | young friend | mock-polite and patronizing | Taekyung calls Nangong Ok 젊은 친구 after stopping his sword draw. |
| 남궁천 | 남궁룡 | father_to_son | you | formal-but-familiar | Nangong Cheon speaks to his sixty-year-old son while discussing martial mastery and Taekyung. |
| 수하 | 흑종필 | subordinate_to_bandit_leader | Boss | deferential | A Black Mountain Stronghold subordinate reports the Green Forest Alliance’s letter and the merchant route. |
| 상인 | 청년 | stranger_to_stranger | Young Brother | formal-polite | A merchant uses 소형제 after noticing the young man's sword, and the young man approves of the address. |
| 청년 | 상인 | stranger_to_stranger | friend | casual and shameless | The young man declares that they should be friends after drinking their Yeoahong. |
| 점소이 | 상인 | waiter_to_customers | gentlemen | formal-polite | The waiter addresses the merchants as 손님들 while charging them for their supposed friend's bill. |
| 점소이 | 송호 | waiter_to_respected_martial_master | Great Hero Song | formal-deferential | The waiter recognizes Song Ho and bows before accepting payment. |
| 송호 | 청년 | elderly_martial_artist_to_younger_martial_artist | Young Hero | formal-polite | Song Ho calls out to the young man as 소협 at the chapter's end. |
| 아이들 | 청년 | children_to_stranger | beggar bastard | childlike-insulting | The children repeat their mother's insulting description of Taekyung's beggar-like appearance. |
| 종리추 | 진태경 | new acquaintances | friend; you | casual and overly familiar | Jongni Chu immediately declares Taekyung his friend and persistently follows him. |
| 진태경 | 종리추 | new acquaintances | you; Jongni Chu; punk | blunt and dismissive | Taekyung rejects Jongni Chu's forced friendship and repeatedly tells him to leave. |
| 포목점 종업원 | 진태경 | shop employee to customer | beggar | condescending and hostile | The employee assumes Taekyung entered the cloth shop to beg and insults him over his clothing and money. |
| 위팽 | 혁무진 | mentor_to_junior_martial_artist | Hyuk Mujin | blunt and testing | Wipeng addresses Mujin by name when beginning to assess and train him. |
| 혁무진 | 위팽 | junior_martial_artist_to_mentor | Great Hero Wipeng | formal-deferential | Mujin uses 위팽 대협 when reacting to Wipeng's recognition and instruction. |
| 호철 | 혁무진 | squad_subordinate_to_vice_squad_leader | Vice Squad Leader | deferential | Hocheol addresses Mujin by his Jin Dragon Squad office. |
| 적천강 | 남궁룡 | legendary_martial_master_to_family_head | Family Head Nangong | familiar and teasing | Jeok calls him 남궁 가주 while asking whether his son will compete. |
| 적천강 | 공일중 | senior_martial_master_to_sect_leader | you; man with the sycophant's beard | blunt and insulting | Jeok mocks Gong's beard and dismisses the title Wind-and-Cloud Sword Lord. |
| 적천강 | 벽력도왕 | rival_martial_master_to_rival_martial_master | Virility Saber King | insulting and taunting | Jeok coins 정력도왕 as a taunting replacement for the established title. |
| 벽력도왕 | 적천강 | rival_martial_master_to_rival_martial_master | Jeok Cheongang | boisterous and hostile-teasing | The Thunderbolt Saber King calls Jeok by name before their argument escalates. |
| 대머리 사내 | 곽철융 | bookmaker_to_respected_gambler | Great Hero Kwak | formal-deferential | The bald bookmaker respectfully addresses Kwak Cheolyung while acknowledging his status as a legendary Dogon. |
| 감독관 | 진태경 | exam_supervisor_to_candidate | Young Hero Jin | formal-polite | Uses 진 소협 while calling Taekyung for the cliff test. |
| 진태경 | 감독관 | candidate_to_exam_supervisor | Supervisor | polite | Uses 감독관님 while asking about the test conditions and result. |
| 감독관 | 철수신룡 | exam_supervisor_to_overpowering_candidate | you | formal-commanding | Orders the Iron-Water Divine Dragon to control himself and warns him against fighting. |
| 철수신룡 | 감독관 | overpowering_candidate_to_exam_supervisor | you | blunt-commanding | Orders the supervisor to move aside while asserting his status as Pa Ryun's disciple. |
| 진태경 | 철수신룡 | rival_candidates | you; weakling | insulting-casual | Uses 너 and later insults him as 좆밥아 while provoking him. |
| 철수신룡 | 진태경 | rival_candidates | brat; you | condescending and taunting | Uses 애송아 and 네놈 while belittling Taekyung and the Fire Gate Clan. |
| 백우 | 진태경 | rival_finalists | Fellow Daoist Jin Taekyung | formal-polite and admonishing | Baek Woo uses 도우 while criticizing Taekyung's vulgarity. |
| 궁기방 | 진태경 | rival_finalists | you bastard | insulting-casual | Gung Gibang answers Taekyung's collective insult with a profane threat. |
| 진태경 | 백우 | rival_finalists | you three idiots | insulting-casual | Taekyung addresses Baek Woo, Gung Gibang, and Zhuge Gyun collectively as 세 얼간이. |
| 진태경 | 궁기방 | rival_finalists | you three idiots | insulting-casual | Taekyung addresses Gung Gibang as part of the trio and threatens them before a duel. |
| 진태경 | 제갈균 | rival_finalists | you three idiots | insulting-casual | Taekyung addresses Zhuge Gyun as part of the trio and threatens them before a duel. |
| 송호 | 진태경 | senior_martial_artist_to_junior_martial_artist | you | familiar-polite | Uses 자네 while recognizing Taekyung and discussing his preliminary performance. |
| 중년 감독관 | 송호 | exam_supervisor_to_respected_Peak_master | Sir Song | formal-deferential | Uses 송 대협 while respectfully asking why Song Ho has come. |
| 종리추 | 청풍 | newly met fellow finalist | friend | casual and overly familiar | Jongni Chu immediately calls the disguised Cheongpung friend after learning his false identity. |
| 청풍 | 종리추 | newly met fellow martial artist | friend | casual and exuberant | Cheongpung enthusiastically accepts Jongni Chu's offer of friendship while still using his disguise. |
| 굉도 | 팽 시주 | senior_martial_master_to_rival_martial_master | Benefactor Peng | formal-polite | Hong Dao uses the Buddhist 시주 address while asking Peng Cheolhu to explain Jongni Chu's hidden strength. |
| 심사관 | 진태경 | judge_to_finalist | Young Hero Jin | formal-polite and flustered | Warns Taekyung that entering the semifinal violates the banquet rules. |
| 진태경 | 심사관 | finalist_to_judge | Judge | blunt and defiant | Rejects the judge's demand that he stand by while Cheongpung is apparently endangered. |
| 적천강 | 심사관 | presiding_chair_to_judge | you | commanding and intimidating | Orders the judge to abandon the original schedule and begin the final. |
| 적천강 | 종리추 | legendary_master_to_suspicious_rival | you / tongue-cut bastard | grave and threatening | Questions Jongni Chu about Tianshan and threatens him over harm to Taekyung or Cheongpung. |
| 종리추 | 적천강 | suspicious_rival_to_legendary_master | you | polite and taunting | Refuses to answer Jeok Cheongang directly and hints at the danger to his Disciple. |
| 개방의 제자들 | 적천강 | Beggars' Sect disciples to legendary martial master | Great Hero Jeok | formal-deferential | They bow and report that their Sect Leader is pursuing Jongni Chu. |
| 개방의 제자들 | 굉도 | Beggars' Sect disciples to injured Buddhist master | Master | formal-urgent | They urgently plead with Hong Dao to come to his senses after finding him gravely wounded. |
| 염호 | 한수 | old friends | Han Su; you bastard | rough and familiar | Flame Tiger insults Han Su while criticizing his treatment of the captured agent. |
| 한수 | 염호 | old friends | Flame Tiger | familiar and conversational | Han Su addresses his longtime friend by his epithet while agreeing to proceed together. |
| 한수 | 무명 | hostile_intruder_to_Shaolin_monk | Hong Dao's Disciple; you | cold and threatening | Han Su identifies Unnamed as Hong Dao's Disciple and threatens to take his life. |
| 무명 | 한수 | Shaolin_monk_to_hostile_intruder | Benefactor | formal-polite but guarded | Unnamed uses 시주 while refusing Han Su's demand for the Green Jade Buddha Staff. |
| 염호 | 굉천 | hostile_martial_opponents | Brat; bald monk | condescending and taunting | Flame Tiger repeatedly belittles Hongcheon during their battle. |
| 굉천 | 염호 | hostile_martial_opponents | old monster; demonic fiend | defiant and condemning | Hongcheon condemns Flame Tiger as an old monster and demonic fiend while continuing to resist. |
| 염호 | 적천강 | hostile martial opponents | old man; Fire King | hostile and taunting | Flame Tiger taunts Jeok while using Hongcheon as a hostage and later recognizes him as the Fire King. |
| 적천강 | 염호 | rival martial opponents | Flame Tiger; bear | blunt, threatening, and contemptuous | Jeok dismisses Flame Tiger's attempt to imitate a fox and calls him a foolish bear before killing him. |
| 진태경 | 염호 | hostile martial opponents | yellow old geezer | insulting and casual | Taekyung exchanges color-based insults with Flame Tiger during their joint attack. |
| 염호 | 진태경 | hostile martial opponents | green little brat | hostile and condescending | Flame Tiger insults Taekyung while attempting to kill him first. |
| 한수 | 혈주 | operative to rendezvous contact | Blood Lord | relieved and deferential | Han Su calls out to the Blood Lord after escaping Jeok Cheongang. |
| 혈주 | 적천강 | claimed enemy to enemy | your enemy | calm and threatening | The Blood Lord identifies himself as Jeok's enemy and claims to have killed Jeok's most precious friend. |
| 혈주 | 한수 | rendezvous_contact_to_senior_operative | Senior Yin Ghost | mock-polite and lightly taunting | Uses 음귀 선배님 while teasing Han Su for hesitating to make his request. |
| 혈주 | 진태경 | hostile_opponent_to_hostile_opponent | Sleeping Dragon of Shanxi | casual, amused, and taunting | Addresses Taekyung by his established epithet while asking whether he agrees with the Blood Lord's judgment of Han Su. |
| 혈주 | 청풍 | hostile_opponent_to_newly_revealed_identity | Huashan's Invincible Divine Sword; Sword Saint's Disciple or grandson | mocking and taunting | Recognizes Cheongpung's public identity and needles him with his Sword Saint lineage while dismissing the added threat. |
| 혈주 | 종리추 | hostile_opponents | you; fearless bastard | hostile and suspicious | The Blood Lord questions Jongni Chu's identity and calls him the fearless man who interfered with his attack on Hong Dao. |
| 종리추 | 혈주 | opponents | you | calm and admonishing | Jongni Chu addresses the Blood Lord as 자네 while explaining that he must stop him by force. |
| 매종학 | 혈주 | legendary_martial_master_to_enemy | you | cold and judgmental | After revealing himself, Mae Jonghak condemns the Blood Lord's accumulated sins and orders him to pay the price. |
| 혈주 | 매종학 | enemy_to_revealed_legendary_master | you | shocked and hostile | The Blood Lord addresses Mae Jonghak with 당신 immediately after recognizing him as the Sword Saint. |
| 종리추 | 송호 | old_acquaintances; former_savior_and_survivor | Thousand-Faced Fox Song Ho; you | casual-familiar | Mae Jonghak addresses Song Ho informally, asks about his prosthetic leg, and recalls that Song would be the first to recognize him. |
| 매종학 | 송호 | savior_to_survivor | you | casual-familiar | Mae uses 자네 while speaking to Song Ho after his identity is recognized. |
| 송호 | 매종학 | rescued_survivor_to_savior | Great Hero; you | formal-deferential and familiar | Song Ho credits Mae with saving his life and addresses him as 대협. |
| 매종학 | 진태경 | older_ally_to_younger_friend | friend | casual-familiar | Mae Jonghak uses 친구 when arriving at Taekyung's window and asking to talk. |
| 진태경 | 진하연 | older_brother_to_younger_sister | Jin Hayeon | blunt-familiar; deliberately stern | Taekyung uses Hayeon's full name to make her hesitate while defending his implausible explanation for sleeping forty-two hours. |
| 최 팀장 | 송송이 | guild_team_leader_to_guild_member | Miss Song | formal-polite | Directs Song Song to take charge of post-raid cleanup and perimeter security. |
| 박지훈 | 진태경 | former_middle_school_classmates | Taekyung | casual-familiar and teasing | Uses 태경아 and 너 while reconnecting after eleven years. |
| 진태경 | 박지훈 | former_middle_school_classmates | you | casual-familiar and teasing | Uses 너 while joking about Jihoon's wealth, appearance, and school memories. |
| 박지훈 | 1팀장 | de_facto_superior_to_nominal_team_leader | Team Leader | commanding and condescending | Orders the nominal Team 1 Leader to wait, arrange an A-Rank raid, and stop imitating a superior. |
| 1팀장 | 박지훈 | nominal_team_leader_to_de_facto_superior | Mr. Jihoon | formal-deferential and anxious | Uses 지훈 씨 while cautiously reporting on Team Leader Jung Hyunwoo and obeying Jihoon's instructions. |
| 김진수 | 진태경 | rookie_guild_member_to_senior_Hunter | Senior | formal-deferential | Jinsoo addresses Taekyung as 선배님 while introducing himself and asking permission to speak comfortably. |
| 진태경 | 김진수 | senior_Hunter_to_rookie_guild_member | Jinsoo | formal-polite | Taekyung uses 진수 씨 after praising Jinsoo’s performance. |
| 임영준 | 진태경 | hostile_black_hunter_to_target | Jin Taekyung; kid | hostile and condescending | Recognizes Taekyung and taunts him as an overconfident child before ordering the attack. |
| 진태경 | 임영준 | target_to_black_hunter_attacker | you | insulting and casual | Demands that Im Yeongjun surrender with the other two attackers and mocks his lack of judgment. |
| 블랙 헌터 | 임영준 | subordinate_to_team_leader | Team Leader | formal-urgent | A surviving Black Hunter cries out to Im Yeongjun after Taekyung destroys his shoulder. |
| 박지훈 | 박태섭 | Myeongdong Guild subordinate to Guild Master; junior to senior | Guild Master; great senior | formal but sarcastic | Uses 길드장님 and 대선배님 while openly challenging Park Tae Seop's authority. |
| 박태섭 | 박지훈 | Guild Master to subordinate; senior to junior | you; brat | furious and condescending | Uses hostile forms while confronting Jihoon over Jung Hyunwoo's death and the Black Hunter problem. |
| 진태경 | 김철수 | visiting Hunter to Security Team Hunter | Hunter Kim Cheol Soo | polite and manipulative | Taekyung addresses him formally while promising to mention his loyalty to the Guild Master. |
| 김철수 | 진태경 | Security Team Hunter to visiting Hunter | Hunter Jin Taekyung | formal-polite and admiring | Initially uses 선생님, then recognizes Taekyung and addresses him as 진태경 헌터님. |
| 진태경 | 선배님들 | junior_to_senior_team_members | Seniors | polite-but-threatening | Taekyung addresses the Myeongdong Guild Team 1 Hunters while ordering them to clear a path. |
| 최민우 | 박지훈 | rival Guild Team Leader to hostile Guild Hunter | Hunter Park Jihoon | formal-polite and controlled | Calls Jihoon through Manager Kim’s phone after the Peace Guild captures Myeongdong personnel. |
| 진태경 | 박태섭 | visiting Hunter to Guild Master | Guild Master | polite but sarcastic | Uses 길드장님 while asking whether Jihoon is Tae Seop's son and warning him not to interfere. |
| 박태섭 | 진태경 | Guild Master to hostile visiting Hunter | you | formal-but-familiar and cautioning | Uses 자네 while warning Taekyung about the danger of opposing 'that person' before reluctantly fighting him. |
| 이정룡 | 진태경 | senior S-rank Hunter to younger Hunter and adversary | Young man | polished, teasing, and veiled-threatening | Uses a genial tone and indirect threats while trying to make Taekyung release the captives. |
| 진태경 | 이정룡 | younger Hunter to senior S-rank Hunter and adversary | you | polite but mocking and defiant | Taekyung answers Lee's soft threats with the wolf-and-tiger metaphor and refuses to yield. |
| 박태섭 | 이정룡 | Guild Master to Vice Guild Master; former Great Cataclysm acquaintance | Vice Guild Master Lee Jungryong | formal-deferential | Park Tae Seop greets Lee respectfully while apologizing for the scene. |
| 이정룡 | 박태섭 | Vice Guild Master to Guild Master; former Great Cataclysm acquaintance | Guild Master Park | formal-but-familiar | Lee minimizes their relationship as occasional acquaintances while presenting himself as conciliatory. |
| 박지훈 | 이정룡 | Disciple to master | Master | terrified and pleading | Jihoon cries out to Lee as Master after Taekyung begins stabbing him. |
| 이정룡 | 박지훈 | master to Disciple | Disciple | commanding, protective, and enraged | Lee restrains himself to protect Jihoon while ordering Taekyung to stop and later carries Jihoon's mutilated body. |
| 이정룡 | 석 팀장 | Vice Guild Master to security-team leader | Team Leader Seok | formal-but-familiar and commanding | Lee addresses Seok while assuring Park Tae Seop that the Myeongdong Guild members will be safe and later orders him to watch Taekyung. |
| 석 팀장 | 이정룡 | security-team leader to Vice Guild Master | Vice Guild Master | formal-deferential | Seok reports on Park Tae Seop and the operation, then accepts Lee's orders. |
| 이정룡 | 고준 | Master to Disciple | Go Jun | familiar and testing | Lee switches from Seok's office title to his personal name while considering whether he can defeat Taekyung. |
| 고준 | 이정룡 | Disciple to Master | Master | deferential | Go Jun responds to Lee's personal-name address as 스승님. |
| 마법사 | 이정룡 | Ares Guild mage subordinate to Vice Guild Master | Vice Guild Master | formal-deferential | Lee's five direct A-rank mages greet him and receive instructions for concealing the battle. |
| 임꺽정 | 최 팀장 | guild_member_to_team_leader | Team Leader Choi | hearty and grateful | Thanks Choi for paying for and arranging his treatment. |
| 최 팀장 | 이정룡 | former_subordinate_to_former_superior; junior_to_senior | Vice Guild Master; Senior | formal but hostile and controlled | Uses the official title in greeting Lee and 선배님 while confronting him about the overseas transfer and their shared past. |
| 김 집사 | 이정룡 | former_savior_to_saved_senior; hostile acquaintances | Senior | formal-polite turning openly threatening | Uses 선배 while greeting Lee and later threatens him after recalling the Mapo Bridge rescue. |
| 이정룡 | 김 집사 | older_acquaintance_to_former_savior | Hwajong; you | familiar, needling, and amused | Calls Butler Kim 화종이 and 자네 while provoking him about his temper and the rescue. |
| 김 집사 | 석고준 | senior_Hunter_to_junior_security_leader | Hunter; Team Leader Seok | blunt and contemptuous | Initially addresses Go Jun as 헌터님, then dismisses him as 석고준 팀장 and orders him to stay out of the conversation. |
| 이정룡 | 천태민 | younger_to_older_brother_by_choice | older brother | reverent and familiar; internal | Lee Jungryong uses 형님 in unspoken thoughts and regards Cheon Taemin as an older brother despite having no blood relation. |
| 김 집사 | 진태경 | butler_to_hunter_client | Hunter Jin Taekyung | formal-deferential | Uses Taekyung's full Hunter title while asking how he possesses the Mana Cultivation Method. |
| 김 집사 | 송송이 | guild_master_to_guild_member | Hunter Song Song | formal-deferential | Uses Song Song's full Hunter title while checking on her after the retching. |
| 댕댕이 | 진태경 | new_hire_to_senior_Hunter | Senior Jin Taekyung | fearful-deferential | A first-day trainee begs Taekyung to let him leave the A-rank Gate. |
| 진태경 | 스켈레톤 워로드 | hostile_monster_encounter | friend; Warlord | mocking-casual | Taekyung sarcastically calls the damaged Warlord his friend, then addresses it by its title while threatening to kill it. |
| 스켈레톤 워로드 | 진태경 | undead_ruler_to_human_enemy | Human | halting-hostile, then desperate-deferential | The Warlord addresses Taekyung as 인간이여 while trying to recruit or dominate him, then shifts into polite pleading when threatened. |
| 서울지부 협회장 | 최민우 | Hunter Association official to Peace Guild Master | you | authoritative and patronizing | Uses 자네 while delaying the Peace Guild's entry and ordering them to follow procedure. |
| 최민우 | 서울 중앙 협회장 | Peace Guild Master to Hunter Association official | Association President | formal but defiant | Choi openly treats his declaration that the Peace Guild will lead as a notification rather than a request. |
| 서울 중앙 협회장 | 최민우 | Hunter Association official to Peace Guild Master | you | authoritative and patronizing | Uses 자네 while objecting to Choi's defiance and later dismissing the Guild's responsibility. |
| 석고준 | 서울 중앙 협회장 | Ares security leader to Hunter Association official | Association President | formal-polite and coercive | Encourages the Association President to let the Peace Guild lead while applying indirect pressure. |
| 서울 중앙 협회장 | 석고준 | Hunter Association official to Ares security leader | Team Leader Seok | formal-polite and deferential | Asks Go Jun to put in a good word with Lee Jungryong and accepts his framing of the operation. |
| 석고준 | 최민우 | Ares security leader to rival Guild Master | Team Leader Choi Minwoo | formal but barbed | Uses 평화 길드 최민우 팀장님 while belittling Choi and blaming the Peace Guild for Taekyung's apparent death. |
| 진태경 | 석고준 | returning Hunter to hostile Ares security leader | you fucking bastard | hostile and profane | Taekyung directs his final insults and challenge at Go Jun after returning alive. |
| 진태경 | 이우중 | Hunter to Association President | President Lee Woojoong | mock-polite and confrontational | Taekyung addresses him as 이우중 협회장님 while condemning his conduct during the delayed rescue. |
| 이우중 | 진태경 | Association President to Hunter | Jin Taekyung; young man | authoritative and indignant | Woojoong addresses Taekyung with 젊은 친구 and 진태경 당신 while objecting to his insults. |
| 석고준 | 진태경 | hostile_opponents | brat | hostile and overconfident | Go Jun addresses Taekyung internally as 애송아 while launching his full-strength attack. |
| 현장 리포터 | 진태경 | field_reporter_to_returned_Hunter | Mr. Jin Taekyung | formal and startled | The reporter urgently confirms Taekyung's identity during the live broadcast. |
| 진태경 | 워로드몬 | captor_to_captured_monster | Warlordmon | mocking-commanding | Taekyung uses the childish nickname while ordering the Skeleton Warlord to perform tricks. |
| 여성 | 빙빙 | mother_to_daughter | Bingbing | urgent-familiar | The mother urgently tells Bingbing to hold her hand while they flee the Monster Wave. |
| 이정룡 | 백한성 | Ares authority to national head of state | Mr. President | formal-polite | Uses 대통령 각하 while greeting Baek Hanseong. |
| 백한성 | 이정룡 | President to Ares Guild Vice Guild Master | Vice Guild Master Lee | formal-polite | Uses 이정룡 부길드장님 while discussing the Chinese proposal. |
| 낙양괴의 | 매종학 | physician_to_renowned_martial_master | Great Hero Mae | formal-polite | Addresses Mae while asking him to protect Taekyung and while requesting that he calm down. |
| 매종학 | 낙양괴의 | renowned_martial_master_to_physician | Strange Physician | familiar-but-respectful | Uses 괴의 while checking on the physician and calming him. |
| 진태경 | 낙양괴의 | young_martial_artist_to_physician | Elder; Strange Physician | deferential and urgent | Uses 어르신 and 괴의 while asking for Jeok Cheongang's diagnosis and treatment. |
| 낙양괴의 | 진태경 | senior_physician_to_young_martial_artist | young brat | gruff and murderous | Threatens Taekyung's eyes and mouth while maintaining a deceptively genial demeanor. |
| 주화란 | 허준 | niece_to_uncle | Uncle Heo | formal-polite | Hwaran addresses her uncle and Chief Escort as 허 숙부. |
| 허준 | 주화란 | uncle_to_niece | Hwaran; Young Bureau Head | concerned-familiar and commanding | Heo Jun calls her 화란아 and orders the escorts to protect the Young Bureau Head. |
| 천력부 | 허준 | familiar_enemies | Brother Heo | taunting and insulting | Heavenly Axe recognizes Heo Jun and mocks his service to Hwaran. |
| 허준 | 천력부 | escort_chief_to_mounted_bandit_leader | Heavenly Axe | alarmed and guarded | Heo Jun identifies the approaching bandit leader by his epithet. |
| 천력부 | 주화란 | mounted_bandit_leader_to_young_bureau_head | little girl | condescending and insulting | Heavenly Axe refers to Hwaran contemptuously while mocking Heo Jun. |
| 주화란 | 석 표두 | childhood_siblings_by_affection | Brother Seok; Chief Escort Seok | grieving and respectful | Hwaran calls him Brother Seok before correcting herself to his office title while mourning his death. |
| 송일섬 | 주화란 | escort_captain_to_young_bureau_head | Hwaran | urgent and familiar | Calls out 화란아 while urgently warning Ju Hwaran before stepping into the confrontation. |
| 주화란 | 진태경 | escort_bureau_leader_to_famous_younger_martial_artist | Young Hero Jin | formal-deferential | Hwaran introduces herself as the Young Bureau Head and formally greets Taekyung as 진 소협. |
| 진태경 | 천력부 | superior_martial_artist_to_defeated_bandit_leader | Axe; our Axe | mocking-casual | Taekyung deliberately shortens Heavenly Axe's epithet to 력부야 and 우리 력부 while preventing his retreat. |
| 천력부 | 진태경 | bandit_leader_to_overwhelming_younger_martial_artist | Sleeping Dragon of Shanxi; Young Hero Jin; young punk | shifting from startled-deferential to condescending | Bangyeol recognizes Taekyung by his epithet and formal title, then becomes contemptuous after believing Jeok Cheongang is absent. |
| 진태경 | 주화란 | visitor_to_young_bureau_head | Young Lady Ju | formal-polite | Taekyung uses 주 소저 while announcing that his party must leave. |
| 주화란 | 혁무진 | rescued_survivor_to_benefactor | Benefactor | formal-deferential | Hwaran includes Mujin among the Benefactors when greeting Taekyung's companions. |
| 주화란 | 궁기방 | rescued_survivor_to_benefactor | Benefactor | formal-deferential | Hwaran includes Gung Gibang among the Benefactors when greeting Taekyung's companions. |
| 주화란 | 청풍 | rescued_survivor_to_benefactor | Benefactor | formal-deferential | Hwaran includes Cheongpung among the Benefactors when greeting Taekyung's companions. |

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 적천강    | **Jeok Cheongang** |
| 백무성    | **Baek Museong**   |
| 매종학    | **Mae Jonghak**    |
| 청풍     | **Cheongpung**     |
| 혁소평    | **Hyuk Sopyung**   |
| 굉도     | **Hong Dao**       |
| 검성     | **Sword Saint**               | Mae Jonghak    |
| 법왕     | **Dharma King**               | Hong Dao       |
| 화산파    | **Huashan**                      |
| 종남파    | **Zhongnan Sect**                |
| 소림     | **Shaolin**                      |
| 무림맹    | **Murim Alliance**               |
| 암천     | **Dark Heaven**                  |
| 삼류     | **Third Rate**    |
| 일류     | **First Rate**    |
| 절정     | **Peak**          |
| 무인     | **martial artist**                               | Default term                                          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 깨달음    | **enlightenment** / **insight**                  | Martial enlightenment                                 |
| 낭인     | **wandering martial artist**                     |                                                       |
| 기루     | **pleasure house**                               |                                                       |
| 장문인    | **Sect Leader**                              |
| 장로     | **Elder**                                    |
| 사부     | **Master**                                   |
| 제자     | **Disciple**                                 |
| 사제     | **Junior Brother**                           |
| 사질     | **Martial Nephew**                           |
| 은인     | **Benefactor**                               |
| 상태               | **Status**                     |
| 사천     | **Sichuan**            |
| 안휘     | **Anhui**              |
| 화산     | **Huashan**            |
| 귀가      | **your family**                                                 |
| 대협      | **Great Hero** or **Sir** depending tone                        |
| 소협      | **Young Hero**                                                  |
| 궁기방 | **Gung Gibang** | Beggars' Sect Successor Beggar and finalist. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 섬서 | **Shaanxi** | Province bordering Shanxi. |
| 맹주 | **Alliance Leader** | Leader of the regional Murim alliance. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 전서응 | **messenger eagle** | Emergency courier used by the Lower District Sect. |
| 구파일방 | **Nine Sects and One Gang** | Major Murim grouping. |
| 개방 | **Beggars' Sect** | Murim organization counted among the Nine Sects and One Gang. |
| 서안 | **Xi’an** | Historic city near Huashan. |
| 화산일학 | **Huashan’s Lone Crane** | Epithet of Baek Museong. |
| 매화삼절 | **Three Plum Blossom Elites** | Collective title for the current Sect Leader’s three exceptional disciples. |
| 천검진인 | **Heavenly Sword True Person** | Taoist-style title of the current Sect Leader of Huashan, who once commissioned a sword from Jang Taebo. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 준이 | **Jun** | Family nickname used in the form Jun's dad. |
| 화산신룡 | **Huashan Divine Dragon** | Title given to Cheongpung after the Star-Array Grand Banquet. |
| 서안루 | **Xi'an Tower** | Prominent pleasure house in Xi'an. |

## Listed compact profiles

### Baek Museong.md

# Baek Museong (백무성)

- **Safe through:** Chapter 312
- **Aliases:** Huashan’s Lone Crane
- **Role:** First-generation disciple of Huashan, first of the Three Plum Blossom Elites, and leader of the effort to return Cheongpung, his Martial Uncle, to Huashan; after Cheongpung claims permission to follow Jeok Cheongang, Baek plans either to escort him back to the main sect or search the Central Plains for Mae Jonghak, awaiting a message from Huashan.
- **Personality:** Calm, responsible, principled, and patient, though visibly weary of his junior disciples’ antics.
- **Voice:** Gentle and polite with strangers; measured and stern when correcting junior disciples.
- **Relationships:** The current Huashan Sect Leader is his Master; Chulwoo and Eunhyang are his junior disciples; Cheongpung is his Martial Uncle through Mae Jonghak and the current Sect Leader; he met Cheongpung ten years ago.

### Cheongpung.md

# Cheongpung (청풍)

- **Safe through:** Chapter 312
- **Aliases:** Huashan Divine Dragon
- **Role:** Mysterious young man encountered at Honghwa Inn; an exceptionally young Peak master whose Level Jin Taekyung cannot determine through Qi Sense; the grandson and disciple of Sword Saint Mae Jonghak, who secretly descended from Huashan to seek out and defeat the Ten Dragons and Phoenixes, beginning with Jin Mukyung; he has no martial title yet, naturally opened his Governor Vessel through enlightenment two years ago, has begun teaching Jin Taekyung and Hyuk Mujin using Mae Jonghak's training method, has now used Sword Energy and the Zaha Divine Technique during his spar with Taekyung, defended Taekyung from Jeok Cheongang with Huashan martial arts, and Prince Shangshan will only accept his autograph after he gains one; he claims Mae Jonghak has permitted him to become Jeok Cheongang’s Disciple and follow Taekyung to Anhui; after fleeing the Three Plum Blossom Elites on the way back to Huashan, he concealed himself as the Invincible Divine Sword under the false name Kang Pung, defeated Zhuge Gyun and the Willow-Cloud Divine Dragon, and faced Jongni Chu in the Star-Array Grand Banquet semifinals; during the semifinal, Jongni Chu revealed overwhelming hidden strength, wounded him, prompted him to identify Mae Jonghak publicly as his grandfather, and drove him into his first experience of fear before Jin Taekyung intervened; Jongni Chu's feint injured his mental strength and shallowly cut his chest, after which Jeok Cheongang pulled him from the arena; at Mount Song, he initially freezes in fear before the Blood Lord but chooses to fight beside Taekyung, refuses to retreat despite severe injuries, smiles at the Blood Lord without fear, and hears a familiar voice say that he has broken free of his shell; the voice is revealed as Mae Jonghak, who protects him from the Blood Lord and attacks with the divine Thirty-Six Plum Blossom Swords before Cheongpung loses consciousness.
- **Personality:** Affable, dreamy, hazy, and childlike in manner, with innocent curiosity, delight in novel public attention, a deep love of martial arts, and a martial artist's competitive pride; he becomes unsettled when someone copies his martial arts
- **Voice:** Dreamy and hazy, with innocent, polite phrasing
- **Relationships:** Mae Jonghak, the Sword Saint, is his grandfather and martial instructor; Cheongpung came to Huashan at about age three or four rather than being born there, lived with Mae Jonghak at a hidden residence, and secretly left Huashan without his grandfather's knowledge to challenge the Ten Dragons and Phoenixes; Baek Museong is his Martial Nephew through the current Huashan Sect Leader, met him ten years ago, and is now leading the effort to return him to Huashan; the current Huashan Sect Leader, the Heavenly Sword True Person, is his eldest Senior Brother by generation, has repeatedly tried to seize him and drag him back to Huashan, and has ordered him to return; Cheongpung never underwent Huashan's initiation ceremony and is technically an outsider; Li Feng is his Martial Nephew within Huashan's hierarchy; calls Jin Taekyung and Hyuk Mujin Benefactors after they feed him and is now accompanying Taekyung, Jeok Cheongang, and Hyuk Mujin to Sichuan to find the Divine Physician

### Gung Gibang.md

# Gung Gibang (궁기방)

- **Safe through:** Chapter 312
- **Aliases:** Successor Beggar, Beggar Prince, pure-blooded beggar, ultimate beggar
- **Role:** Beggars' Sect martial artist and Successor Beggar, a position held by the person who will later lead the sect; advanced to the Star-Array Grand Banquet semifinals, where Jin Taekyung defeated him in fifteen minutes after he revealed that he had learned only five stages each of the Eighteen Dragon-Subduing Palms and Dog-Beating Staff Technique; now accompanies Taekyung to Sichuan as the final member of the small search party for the Divine Physician
- **Personality:** Vulgar, aggressive, and quick-tempered.
- **Voice:** Blunt, profane, and vividly threatening.
- **Relationships:** Rival finalist alongside Baek Woo and Zhuge Gyun; trades insults with Taekyung, then agrees to remain silent, use polite speech, and call him Jin hyung after being intimidated aboard the carriage.

### Hong Dao.md

# Hong Dao (굉도)

- **Safe through:** Chapter 269
- **Aliases:** Dharma King
- **Role:** Abbot of Shaolin and the Murim's Dharma King; master of Unnamed and the only friend to whom Jeok Cheongang had opened his heart; after leaving the Star-Array Grand Banquet, he was found in a massive pit with both legs severed and catastrophic internal injuries, whispered final words to Jeok Cheongang, and died.
- **Personality:** Calm, responsible, quietly playful, and still regarded by Jeok as lazy for sleeping whenever possible.
- **Voice:** Quiet, deep, weighty, and resonant, with casual familiarity when speaking to Jeok Cheongang.
- **Relationships:** Old friend of Jeok Cheongang; master of Unnamed; before his death, entrusted the Green Jade Buddha Staff to Unnamed and used his final words to warn Jeok about Jongni Chu, Dark Heaven, Unnamed, and the Buddhist Staff; sends Unnamed to bring the Master of Morning Star to Shaolin.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 311
- **Aliases:** Fire King
- **Role:** Over-one-hundred-year-old wandering martial master and the Fire King; he visits Jang Taebo’s home, can detect Qi Sense, can cross more than ten jang in an instant, plans to reach Taiyuan and visit the Lower District Sect while concealing his identity, and once fought Sword Saint Mae Jonghak for seven days and seven nights to a draw at Mount Jiuhua before emerging from seclusion and annihilating one thousand Demonic Cultists there; after striking Jin Taekyung with the Flame Divine Palm, he deduces that Taekyung took the Blazing Flame Divine Pill and confronts him when he tries to flee the inn; he reaches the Jin Family of Taiyuan, falsely identifies the Unnamed Sword in public as the Fire Gate Clan’s sacred treasure entrusted to Taekyung, later reveals that it is actually the Fire Heaven Sword, the beloved sword of the Fire Gate Clan’s tenth Sect Leader, uses Six-Harmonies Voice Transmission to stop Song Il, publicly humiliates him, then follows the departing Zhongnan group, incapacitates the Three Hands, breaks Song Il’s wrist, strikes him with the Flame Divine Palm, and threatens to destroy the Zhongnan Sect and Mount Zhongnan if Taekyung or the Jin Family is harmed; two days later, he severely beats Taekyung with his bare fists over the partly burned Flame Divine Palm manual, performs an abbreviated cleansing treatment on Taekyung, discovers his exceptionally balanced body, and suspects he may possess the legendary Heavenly Martial Physique; at the Jin Family banquet, after Ak Bulgun questions their relationship, he publicly declares himself the eighteenth Sect Leader of the Fire Gate Clan, accepts Taekyung as his Disciple, and declares that Taekyung will inherit the clan’s orthodox lineage; he identifies Taekyung as possessing the Heavenly Martial Physique, agrees to personally oversee Taekyung’s martial-arts training until Taekyung reaches a certain level, and permits Taekyung to address him as Master publicly and Old Master in private while continuing to deny that they are truly master and Disciple; after accepting Taekyung’s challenge to defend only, he is forced five steps backward by Taekyung’s One Annihilation and admits defeat, then supports Taekyung with internal energy as he collapses; impressed by the strike, he now desires to guide Taekyung toward becoming a Heavenly Dragon; he successfully forces open Taekyung’s Conception and Governor Vessels, then carries the unconscious Taekyung away to rest after the ordeal; he waits through Taekyung’s seven-day unconscious recovery, explains that removing accumulated turbid qi caused the adjustment period, discusses the Star-Array Grand Banquet invitation, and asks Taekyung to visit his quarters at dawn after hearing Taekyung’s desire to pursue greater strength; he now takes Taekyung away immediately for a year of martial-arts training in Anhui; after the seven-day journey from Taiyuan to Luoyang, he effortlessly defeats Heukgeol and compels the Dongcheon Sect’s fighters to withdraw without killing them; after leaving Hong Dao’s residence, he reaches Mount Jiuhua in Anhui with Taekyung after a fifteen-day forced march and plans to impose six months of extreme training; he uses Seizing an Object Through Empty Space to pull Taekyung back, strikes his Sleep Acupoint with Pressure-Point Strike to force him to sleep for two shichen, then suffers a sudden bout of weakness after expending too much strength and acknowledges that he has little time while carrying Taekyung toward Mount Jiuhua; after more than two months of extreme training, his increasing sleep and memory lapses lead Taekyung to recognize dementia; he brings Taekyung into the Fire Gate Cavern, explains the Fire Gate Clan’s history, and prepares to transmit its martial arts, including the Fire Gate Divine Technique, after Taekyung agrees to learn from him; at Mount Song, he exhausts himself using the Dance of the Fire God and Demon against the Blood Lord, collapses unconscious after the Blood Lord regenerates, and can no longer participate in the fight; the Luoyang Strange Physician later determines that Jeok is neither poisoned nor affected by demonic qi, but that his qi acupoints are slowly becoming blocked, giving him roughly six months unless a Divine Physician can treat the unknown illness.
- **Personality:** Secretive, cryptic, sharp-eyed, amused by unusual young martial artists, casually violent when dissatisfied with an answer, and newly determined to extend his life after meeting Taekyung rekindled his will to live.
- **Voice:** Sharp and ringing when calling out, then gruff, dryly teasing, and threatening during interrogation.
- **Relationships:** Visits Jang Taebo and tells him to check on the worried child living nearby; regards Jin Taekyung as an interesting fellow after detecting Qi Sense and interrogates him about the System; fought Mae Jonghak more than forty years ago and was close enough to be considered his kindred spirit; recognizes Cheongpung as Mae’s grandson and calls him a dependable grandson and Mae’s successor; rescued an orphan named Jangcheon during an Anhui epidemic, eventually accepted him as his Disciple, and later learned that Jangcheon became Jopil; regards Jangcheon as an only son and grandson despite their lack of blood relation, secretly followed him for four months after learning of his murders, confronted him in a red-light district, and could not bring himself to kill him before Jangcheon held a vial of Bone-Melting Powder between his lips and declared his departure; after learning that Taekyung killed Jopil, acknowledges a debt to Taekyung and apologizes to him and the others for his rash actions; at the Jin Family banquet, accepts gifts from visitors and offers the accumulated treasures, elixirs, and bank drafts to Taekyung; now publicly recognizes Taekyung as his Disciple and intended heir to the Fire Gate Clan’s orthodox lineage; begins genuinely training Taekyung by selecting Scorching Yang Qi elixirs and using his internal energy to open Taekyung’s acupoints; after Taekyung consents to the dangerous attempt, successfully opens both vessels, recognizes Taekyung’s exceptional mental strength, and believes the Heavenly Martial Physique chose its master well; is a friend of Hong Dao, the Abbot of Shaolin and Dharma King; after taking Taekyung to Henan, he takes Taekyung’s coin purse and goes alone to Shaolin, ordering Taekyung not to follow until the preliminary competition in Kaifeng; is a long-standing rival of Peng Cheolhu, the Thunderbolt Saber King, and trades insults with him at the Star-Array Grand Banquet; after finding Hong Dao mortally wounded, hearing his final whispered words, and witnessing his death, declares that he will go to Shaolin.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 312
- **Aliases:** Sleeping Dragon of Shanxi
- **Role:** Modern-world protagonist; recently fired after seven years at his job; A-rank Hunter who defeated eight B-rank Minotaurs and killed a Level 70 B-rank Minotaur Warrior in one blow; Peak Master with forty-five years of internal energy and the Scorching Yang Qi attribute after fully absorbing the Blazing Flame Divine Pill; possesses Jopil’s Flame Divine Palm manual, whose cover Jeok Cheongang partly burned after Taekyung threw it during his escape, and the Fire Heaven Sword, formerly the Unnamed Sword, made from Ten-Thousand-Year Cold Iron; Jeok Cheongang falsely identified the sword in public as the Fire Gate Clan’s sacred treasure, then revealed that it is a former Fire Gate Clan Sect Leader’s beloved sword whose true power requires inheriting the Fire Gate Clan’s legacy; youngest son of the Jin Family of Taiyuan; new owner of a two-story detached house in Goyang intended for his family; Qi Sense reaches a seventy-meter radius; possesses one Temporary Strength Pill in his Inventory and has reserved it for a worst-case, life-threatening contingency; was Level 75 after completing the There Is a Man Who Loved You So Much Quest and One Step Back and receiving large EXP and Fame rewards, with 20 unallocated Bonus Points after the latter Quest; has since gained additional Levels while defeating more than ten B-rank ogres, including a Lv.85 Ogre, at the Gate, and has now received another level-up, 20 Bonus Points, and a major Fame increase from the A-Rank Hunter Achievement; has allocated all seventy remaining stat points, twenty to Strength and fifty to Agility; completed the Find the Master Artisan Quest after securing Jang Taebo’s agreement to forge his Ten-Thousand-Year Cold Iron into a spear; can roughly copy observed martial forms and copied the Plum Blossom Fist after three days of sparring with Cheongpung; killed Jin Baekyang, the Blade of Flowers, and was rendered unconscious with an Internal Injury by Jeok Cheongang’s Flame Divine Palm; narrowly evaded Song Il’s Heavenly River Thirty-Six Swords before Jeok stopped Song and publicly revealed that Taekyung holds the entrusted Fire Gate Clan sacred treasure; spent two days bedridden with severe bruising after Jeok Cheongang beat him with his bare fists over the partly burned manual, then underwent an abbreviated cleansing treatment while unconscious that increased his Muscles and Bones and Sinews and Meridians by 5 each and his Strength, Stamina, and Agility by 1 each; has practiced martial arts for only three months, advancing from Third Rate to the beginning of the Peak realm during that period; was publicly accepted by Jeok Cheongang as his Disciple and declared heir to the Fire Gate Clan’s orthodox lineage, a status that ended his path to Heaven’s Gate Temple and other masters; Jeok Cheongang identifies him as possessing the Heavenly Martial Physique and agrees to personally oversee Taekyung’s martial-arts training until he reaches a certain level, while Taekyung addresses him as Master and, when they are alone, Old Master; completed the Peak-Grade One Step Back Quest after Jeok agreed to defend only and Taekyung used One Annihilation to force him five steps backward, then collapsed from exhausting all his strength and internal energy while Jeok supported him with internal energy; consumed Fire Spirit Grass, Red Flower Grass, and Flame Red Grass, completed the forced Acupoint Opening Quest, and successfully opened both his Conception and Governor Vessels before losing consciousness from exhaustion; blocked an arriving military Hunter team from taking the remaining ogres and personally butchered and collected their valuable parts; is now publicly famous as the Tollgate Hero after appearing on KPS’s Nine O’Clock News; his family’s personal information has been exposed by intrusive media, including a disguised delivery reporter and hired Familiar mages; has received Jinho’s advice not to pursue an impossible ideal of saving everyone; encountered an unidentified high-level Hunter who stepped in front of the sedan carrying him and Team Leader Choi; declined Won Myunghoon’s Star Guild and entertainment-agency proposals, plans to choose only a few commercials before refocusing on Guild work, and accidentally turned his live broadcast profanity into a viral hit; completed the Manifestation of Qi Achievement, unlocking Spear Energy and gaining Unaffected by a Hundred Poisons, two levels, and 100 Bonus Points; defeated and killed the Level 115 Named Monster Carus after resisting his strengthened magic, spent 100 Bonus Points to raise Strength and Stamina by 50 each, earned the Named Monster Defeated Achievement, and perfectly cleared The Black Wyvern’s Nest while receiving enormous EXP and Fame and two displayed level-ups; received approximately 530 billion won after Prince Cheonsur bought Carus’s processed remains at Christie’s for approximately 500 billion won before fees; is directing hundreds of billions through a Peace Guild support foundation for Gate-victim families, Great Cataclysm veterans, and single-parent families; defeated Gung Gibang in the Star-Array Grand Banquet semifinals and advanced to the finals; after Jeok Cheongang became incapacitated at Mount Song, confronted the Blood Lord with Cheongpung, used One Annihilation as his final attack, learned that the Blood Lord caused the Eight Spring Gorge war, and collapsed after continuing the fight until his body could no longer respond; possesses Martial Arts Manual Creation, which requires Great Completion in the martial art and physical materials; created a Peak-grade manual for the Jin Family’s Cultivation Technique after investing Intelligence points to reach the required threshold of 100 and brought it to the Peace Guild, where Team Leader Choi and Butler Kim identified it as a Mana Cultivation Method; falsely claimed that his late father taught the technique as a family health regimen and that the original manual was lost.
- **Personality:** Hungry, self-aware, dryly observant, and willing to take a questionable opportunity when desperate; treats the impossible as a game until the danger becomes undeniable
- **Voice:** First-person, conversational, dryly self-mocking; uses vivid trap-and-prey imagery, game jargon, and occasional profanity
- **Relationships:** Jin Mukyung’s younger brother and current student; son of a deceased father; supports his mother and younger sibling; loves Song Song and confessed his feelings to her during the Named Monster standoff, but she rejected him without changing her attitude for money or fame and accepted a same-age friendship and guildmate relationship; has a strained relationship with Lee Seowol, the current Sect Leader of the Mount Heng Sword Sect, whose marriage proposal he has decided to reject; had formed a friendly hyung-and-younger-brother relationship with Won Myunghoon, but during the raid crisis ordered Won to take the Star Guild members and leave, withdrew the hyung address, warned him not to bare his teeth again, and then broke Won's arm and punched him when Won ambushed the returning Peace Guild survivors; after Won surrendered and attempted another attack, Taekyung killed him; is publicly recognized as Jeok Cheongang’s Disciple and heir to the Fire Gate Clan’s orthodox lineage, and has begun undergoing Jeok’s deliberate training after consenting to the dangerous attempt to open his Conception and Governor Vessels; he has now decided to leave with Jeok Cheongang for a year of training in Anhui and told Jin Mukyung that he and Cheongpung will attend the Star-Array Grand Banquet in one year.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 312
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Mae Jonghak.md

# Mae Jonghak (매종학)

- **Safe through:** Chapter 312
- **Aliases:** Sword Saint
- **Role:** Sword Saint and Cheongpung's grandfather; more than forty years ago he sought Jeok Cheongang's help against the Demonic Cult, fought Jeok at Mount Jiuhua for seven days and seven nights, and drew with him; after the Great Faction War ended, he devoted himself to martial arts, reached Great Completion, attained higher enlightenment after encountering another wall, unexpectedly Returned to Youth, and traveled the world for a year under the name Jongni Chu while concealing his identity; at Mount Song he protected Cheongpung and attacked the Blood Lord with the divine Thirty-Six Plum Blossom Swords; after the Blood Lord escaped, he confirmed his identity to Jin Taekyung and Song Ho, and Song Ho identified Mae as the Great Hero who had saved his life.
- **Personality:** Not established in this chapter.
- **Voice:** Not established in this chapter.
- **Relationships:** Cheongpung's grandfather and martial instructor; taught him the Taeeul Miri Palm; secretly entered Huashan while its Sect Leader slept, left a dagger and handwritten note, and then went into hiding, prompting Huashan's search; fought Jeok Cheongang at Mount Jiuhua more than forty years ago and left after their draw; his old friend Hong Dao left him a letter identifying Jin Taekyung as the Morning Star who would drive away darkness.

## Korean source

```text
＃313화



화산일학 백무성.

섬서 땅에, 아니 무림에서 그 이름을 모르는 사람은 없었다.

천검진인의 적전 제자이자 어린 시절부터 화산파의 미래라 불려왔던 백무성이다.

귀가 밝고 말 많은 호사가(好事家)들 사이에서는 검성의 막내 제자에 관한 소문이 돌았지만, 그런 그들조차 백무성이 훗날 화산파의 장문인이 되리라는 것을 믿어 의심치 않았다.

“듣자 하니 화산신룡의 무위가 이미 구파일방의 장로들을 뛰어넘었다더군. 역시 백 년에 한 번 나올까 말까 한 천재다워.”

“그래도 차기 장문인은 누가 뭐라 해도 화산일학이지. 백무성은 그릇이 달라. 장문인으로서 갖춰야 할 모든 것을 타고났다고.”

“그건 그렇지. 무공이 부족해, 아니면 사람이 부족해? 그가 아니라면 누가 장문인이 된단 말인가?”

서안루의 일 층에서 술잔을 기울이며 대화를 나누고 있던 사람들은 알지 못했다.

대화의 주인공이 자신들의 등 뒤로 지나가고 있음을.

“백 대협의 위명은 익히 들었습니다. 이렇게 만나 뵙게 되어 영광입니다.”

“대협이라니, 과분한 말씀 거둬 주십시오.”

“아닙니다. 대협을 대협이라고 부르는 것뿐인데 무엇이 과분하다는 말씀이십니까.”

호위장의 뜨거운 눈빛에 백무성은 멋쩍게 웃는 것으로 대답을 대신했다.

사람들의 관심은 그에게 하루 이틀의 일이 아니다.

검성 매종학의 은거 이후 주춤했던 화산파의 입지가 올라갈수록 백무성의 부담감도 더해 갔다.

‘장문인이라니.’

삼십 대 초반에 불과한 백무성에게는 멀고도 무거운 이름이었다.

내심 고개를 내젓던 그때 호위장의 발걸음이 멈췄다.

“이곳입니다.”

“여기는…….”

“섬서 제일이라 자부하는 저희 서안루에서도 단 한 곳밖에 없는 별채지요.”

옥석(玉石)으로 장식한 정원, 온갖 고급스러운 집기로 가득 찬 내부를 둘러본 백무성이 난색을 표했다.

“죄송합니다만, 별채를 이용할 만큼의 돈이 수중에 없습니다. 대신 조용한 방 하나만 내어주시겠습니까?”

“하하, 역시 듣던 대로 검소하시군요.”

호위장이 껄껄 웃으며 말을 이었다.

“걱정하지 마십시오. 루주(樓主)께서 누누이 말씀하시길, 화산파에서 손님이 오시거든 일체의 비용도 받지 말고 극진히 모시라 하셨습니다.”

“루주께서 말입니까?”

“예, 작년 가을에 종남파와 모종의 문제가 있었는데, 화산파의 도움으로 잘 해결되었지요. 매화삼절(梅花三絶)의 다른 두 사제분께서 큰 활약을 해 주셨습니다.”

“아, 그렇군요. 제가 폐관 수련 도중에 벌어진 일이라 잘 몰랐습니다.”

“사실 저도 이야기로만 들었습니다. 근무하게 된 지 이게 겨우 달포밖에 되지 않았거든요, 하하.”

백무성은 그제야 이해했다는 듯 고개를 끄덕였다.

지난 일 년간 그도 놀고만 있었던 것은 아니다.

천고의 기재라 할 수 있는 청풍, 그리고 진태경과의 만남은 백무성에게 있어 큰 충격인 동시에 새로운 자극이 되었다. 일 년간의 폐관 수련을 결정한 것은 그 때문이었다.

‘의미 있는 시간이었지.’

수련 도중 얻은 깨달음은 백무성을 전보다 더 강하고 깊이 있는 사람으로 만들어 주었다.

변한 것은 그뿐만이 아니다. 화산파의 위치 또한 일 년 전에 비할 바가 아니었다.

종남의 속가제자들이 대거 포진해 있는 관부조차 문제가 생기면 화산을 먼저 찾을 정도였다.

‘만약 사부님께서 보낸 서신이 사실이라면 그럴 수밖에.’

지금으로부터 닷새 전, 스승인 천검진인이 보낸 전서응에는 놀라운 소식이 적혀 있었다.

소림에서 벌어진 혈겁, 법왕 굉도의 죽음. 그리고 수십 년만에 부활하는 신(新) 무림맹의 맹주로 검성 매종학이 물망에 오르내린다는 소식이 바로 그것이었다.

“여하간 주위에서 온통 난리입니다. 제 벗들도 물어보더군요. 자식이 무공에 재능이 있는 것 같은데 화산파 속가제자로라도 들어갈 수 없겠느냐고요.”

호위장의 은근한 눈빛에 담긴 뜻을 알아차린 백무성이 쓰게 웃었다.

얼핏 봐도 불혹은 넘어 보이는 나이. 자식을 화산파에 입문시키고 싶은 부모의 마음은 그 또한 마찬가지이리라.

하지만 백무성은 모르는 척 대답했다.

“글쎄요, 인연이 닿으면 그리될 수 있겠지요. 허나 굳이 무공을 배울 필요가 있겠습니까. 그 나이에는 건강하게 자라는 것으로 족한 것을.”

“……그렇습니까.”

호위장의 실망한 표정에 백무성은 마음속으로 중얼거렸다.

‘귀하가 곧 불어닥칠 혈풍(血風)을 알고 있다면 그런 표정은 짓지 않았을 겁니다.’

소림의 혈겁에 관한 소문은 이미 알음알음 새어 나갔다.

그러나 암천의 존재는 여전히 극소수만이 아는 특급 기밀. 그 몇 안 되는 이들에 속한 백무성은 직감했다.

곧 무림에 피바람이 불어온다. 먹구름이 하늘을 가리고 수천, 수만의 병장기가 주인과 함께 땅을 뒹굴 것이다.

부모 잃은 자식의, 자식 잃은 부모의 통곡이 사방에서 울려 퍼질 것이다.

‘그런 일이 벌어지지 않도록 막을 겁니다. 내가, 화산이.’

무림에 속한 모두가 백무성과 같은 마음일 터.

갑자기 무거워진 그의 분위기에 호위장이 고개를 갸웃거리던 그때였다.

“총관은 어디 있느냐! 총관!”

“소협, 총관께서는 지금 잠시 자리를 비우셨습니다. 그러니 이제 고정하시고…….”

“고정? 내가 이따위 홀대를 받았거늘, 지금 고정하게 생겼느냐!”

“마, 말씀드렸다시피 별채는 이미 찼습니다. 특실로 안내해 드릴 테니 노여움을 가라앉히십시오.”

“시끄럽다! 내 오늘은 반드시 별채를 써야겠으니 당장 비켜라!”

“아이고, 소협!”

쾅! 우지끈!

소란스러운 소리와 함께 점점 가까워지는 고함. 호위장이 미간을 좁히며 말했다.

“좋지 않은 모습을 보여 드려 송구스럽습니다. 제 수하들이 일을 제대로 하지 못한 모양입니다.”

“별말씀을. 충분히 이해합니다.”

아무리 손님을 까다롭게 가려 받더라도 서안루 또한 기루다. 꽃밭에 온갖 벌레가 끼어드는 것은 당연한 일이 아닌가.

“그나저나 정오밖에 안 되었는데, 꽤 취한 것 같군요.”

“종종 있는 일이지요. 어느 대갓집 자제인 것 같은데, 잘 수습해서 돌려보낼 터이니 백 대협께서는 신경 쓰지 않으셔도 됩니다.”

백무성이 너털웃음을 지으며 고개를 저었다.

“하하, 글쎄요. 여기 계시는 게 좋겠습니다.”

“네?”

“평범한 대갓집 자제는 아닌 것 같아서 말입니다.”

“그게 무슨…….”

의문을 표하던 호위장이 멈칫했다. 멈추지 않는 소란과 더불어 빠르게 가까워지는 인기척을 느꼈기 때문이었다.

‘무림인!’

점점 심상치 않게 돌아가는 상황 속, 다급한 발걸음과 함께 내원을 지키던 호위 무사들의 외침이 들렸다.

“멈추십시오!”

“이곳부터는 지나갈 수 없습니다!”

서안루는 고관대작들도 드나드는 만큼 호위의 수준도 높았다. 그러나 실전 경험이 풍부한 일류 무인들인 그들조차 취객의 난동을 막기에는 역부족이었다.

“낭인 출신 밑바닥 삼류들이 어딜 감히…….”

“헛!”

쉬쉭, 퍼버버벅!

무사들의 짧은 경호성, 빠르고 강한 타격음이 울려 퍼지자 별채 밖이 삽시간에 조용해졌다.

비틀비틀, 거친 걸음걸이가 침묵을 몰아내며 가까워지기 시작한다.

‘저 정도로 취한 상태에서 순식간에 일류 무사 여섯을 쓰러트리다니.’

고수, 그것도 절정 고수다.

호위장이 굳은 얼굴로 검파에 손을 가져가려던 그때, 백무성이 작게 고개를 저어 보였다.

“제가 나서야 할 것 같군요.”

“백 대협, 그건…….”

“괜찮습니다. 몇 차례 면식이 있는 사이니, 제 체면을 봐서라도 물러나 주겠지요.”

“그 말씀은…….”

“선대부터 내려온 인연이 있습니다. 아, 물론…….”

백무성이 볼을 긁적이며 한마디를 덧붙였다.

“그리 썩, 화목한 인연은 아니지만 말입니다.”

“……!”

그때 호위장의 뇌리에 번개처럼 스치는 생각이 있었다.

하나는 종남파라는 세 글자. 그리고 그 뒤를 이어 떠오른 것은 한 사람의 이름이었다.

“호, 혹시?”

서안루의 호위장이 된 지 이제 겨우 보름 남짓. 하지만 그 사람에 관한 소문은 귀에 못이 박히도록 들었다.

종남파라는 출신만큼이나 대단한 성미의 소유자.

표정을 일그러트린 호위장이 한 사람의 이름을 말하려던 순간이었다.

꽈앙!

단단한 흑목(黑木)으로 만들어진 별채의 문이 박살 나며 나뭇조각이 사방으로 튀었다.

비틀거리는 걸음걸이, 불콰하게 달아오른 얼굴의 청년을 향해 백무성이 싱긋 웃어 보였다.

“오랜만이군. 잘 지냈나?”

그와 동시에.

“당신이 왜 여기 있지?”

종남일룡(綜南一龍) 혁소평의 얼굴이 악귀처럼 일그러졌다.



* * *



“와아! 와아아!”

“제발 소리 지르지 마. 사람들이 다 쳐다보잖아.”

“은인! 저기 당과!”

“그놈의 당과는 시부럴 거. 당과 안 질려?”

“네!”

“그럼 그냥 아예 가게를 차려!”

“그럼 당과 장수 아저씨랑 사천까지 같이 가도 돼요?”

“아니, 미친…….”

“저기 소면 팔아요! 소고기로 육수를 냈대요!”

청풍 너란 새끼. 어디로 튈지 모르는 탱탱볼 같은 새끼…….

나는 길거리 좌판을 향해 쪼르르 달려가던 청풍의 뒷덜미를 재빨리 낚아챘다.

“제발 더도 말고 덜도 말고 사람답게만 살자. 사람답게!”

“당과, 소면…….”

“아, 조금만 참으면 배 터지게 먹여 준다고!”

“정말요?”

“몇 번을 말했잖아. 그러니까 제발 입 다물고, 조용히 따라와라. 응?”

물론 내 돈으로 먹이는 게 아니라 화산파 돈이지만, 엎어치나 메치나 거기서 거기지 뭐.

‘원래는 여기도 그냥 지나갔어야 했는데.’

본래 일정대로라면 서안에 들를 필요조차 없었다.

하지만 떠나기 전 화산파 장문인인 천검진인으로부터 서안에 들러 달라는 부탁도 받았고, 청풍의 고향이니 겸사겸사 지나가게 되었을 뿐이다.

칠주야 가까이 제대로 먹지도, 씻지도 않은 채 강행군을 했으니 하루만이라도 대접받으며 푹 쉬고 싶기도 했다.

‘화산일학 백무성이 기다리고 있다고 했었는데.’

그를 마지막으로 본 것이 벌써 일 년도 넘었다.

적천강을 따라 안휘로 떠나기 전, 백무성이 내게 그런 말을 했었다.



‘언제든지 섬서에 오면 연락 주십시오. 제가 제대로 대접하지요. 하하.’



풀 코스로 모신다는 말에 이놈 혹시 부산 사람인가 싶었지만 아주 허언(虛言)은 아니었던 모양이다.

오늘 이렇게 만나게 되는 것을 보면.

“그나저나 서안루가 어디야.”

지나가던 행인을 붙잡고 물어본 바에 의하면 대로를 따라 쭉 걸으면 된다고 했는데, 뭔 놈의 거리가 이렇게 붐비는지 도무지 끝이 안 보인다.

내가 주위를 두리번거리던 그때, 때가 시커멓게 낀 손가락이 저 멀리 보이는 한 건물을 가리켰다.

“저곳이 서안루다.”

“어디? 어, 진짜네. 어떻게 알았냐?”

미래의 왕초 거지 궁기방이 자부심 넘치는 얼굴로 대답했다.

“최고의 구걸 장소거든. 남아서 버리는 음식도 산해진미 수준이고, 지위가 높은 사람들이 드나들다 보니 적선도 많이 한다. 거지라면 모를 수 없는 곳이지.”

“…….”

알고 보니 개방의 핫 플레이스였군.

나는 고개를 절레절레 흔들며 서안루를 향해 걸음을 옮겼다.

사람 열 명이 동시에 드나들어도 될 만큼 커다란 정문에 도착하자, 서안루 소속으로 보이는 호위 무사가 고개를 숙였다.

“죄송합니다. 오늘은 영업을 하지 않습니다.”

“……뭐야. 쉬는 날이에요?”

“그게 아니라. 영업 도중 약간의 문제가 생겨서 그렇습니다.”

“아.”

이건 예상하지 못했는데.

슬쩍 고개를 돌려보니 통곡하기 직전의 청풍이 눈에 들어온다.

나는 머리를 긁적이며 호위 무사에게 말했다.

“어떻게 안 될까요? 오늘 약속이 잡혀 있었는데. 백무성이라고. 이름 대면 알 거랬어요.”

“다시 한번 말씀드리는 거지만 지금은…… 예? 지금 백무성 대협이라고 하셨습니까?”

“네. 화산일학 백무성이요.”

청풍이 간절한 목소리로 외쳤다.

“백 사질! 어디 있나요, 백 사질! 내 꼬르륵 소리 들리나요!”

그런 우리를 번갈아 보던 호위 무사가 굳게 닫혀 있던 정문을 잽싸게 열어젖혔다.

“지금 즉시 별채로 모시겠습니다!”

뭐야 이거.

갑자기 반응 왜 이래.

‘백무성이 노쇼라도 했나?’

내 예상은 틀렸다. 거의 날 듯이 달려가는 호위 무사를 따라간 그곳에는, 거의 초토화 된 별채와 검을 빼 든 백무성이 우리를 기다리고 있었다.

이야, 이거 완전.

‘진짜 풀코스네.’

드러워서 무림인 못 해 먹겠다.
```

## Final English reading copy

```markdown
# Chapter 313

Huashan’s Lone Crane, Baek Museong.

There was no one in Shaanxi—or in the entire Murim—who didn’t know that name.

Baek Museong was the direct Disciple of Heavenly Sword True Person, and he had been called Huashan’s future since childhood.

Among the sharp-eared, gossip-loving busybodies, rumors circulated about the Sword Saint’s youngest Disciple. Even they never doubted that Baek Museong would one day become the Sect Leader of Huashan.

“I hear the Huashan Divine Dragon’s martial prowess has already surpassed that of the Elders of the Nine Sects and One Gang. He’s truly a genius who appears once in a century, if that.”

“Even so, no matter what anyone says, the next Sect Leader is obviously Huashan’s Lone Crane. Baek Museong is made of different stuff. He was born with everything a Sect Leader needs.”

“That’s true. Is he lacking in martial arts? Or as a person? If not him, then who could possibly become Sect Leader?”

The people drinking and chatting on the first floor of Xi’an Tower did not know that the subject of their conversation was passing behind them.

“I’ve heard plenty about your renown, Great Hero Baek. It’s an honor to meet you.”

“Great Hero? You flatter me.”

“Not at all. I’m merely calling a Great Hero a Great Hero. What could possibly be excessive about that?”

In response to the head guard’s fervent gaze, Baek Museong merely gave an awkward smile.

The attention people paid him was nothing new.

As Huashan’s standing rose after having faltered following the Sword Saint Mae Jonghak’s withdrawal from the world, so too did the burden on Baek Museong’s shoulders grow heavier.

*The Sect Leader.*

For Baek Museong, who was barely into his thirties, it was a distant and weighty title.

He was inwardly shaking his head at the thought when the head guard stopped walking.

“This is the place.”

“This is…?”

“Even in our Xi’an Tower, which proudly calls itself the finest in Shaanxi, this is the only private annex.”

Baek Museong looked around at the garden decorated with jade and the interior filled with all kinds of luxurious furnishings. His expression grew troubled.

“I’m sorry, but I don’t have enough money on hand to use a private annex. Could you provide me with a quiet room instead?”

“Haha, you’re as frugal as I heard.”

The head guard continued with a hearty laugh.

“Please don’t worry. The owner has repeatedly instructed us that whenever a guest from Huashan arrives, we are to provide the utmost hospitality and charge nothing at all.”

“The owner said that?”

“Yes. There was some sort of trouble with the Zhongnan Sect last autumn, but it was resolved thanks to Huashan’s assistance. The other two members of the Three Plum Blossom Elites—your Junior Brothers—played a major role.”

“Ah, I see. It happened while I was in secluded training, so I didn’t know much about it.”

“Actually, I only heard about it myself. I’ve only been working here for barely a month. Haha.”

Only then did Baek Museong nod as if he understood.

It wasn’t as though he had spent the past year doing nothing.

Meeting Cheongpung, a peerless prodigy, and Jin Taekyung had been a tremendous shock to Baek Museong, as well as a fresh source of stimulation. That was why he had decided to enter secluded training for a year.

*It was a meaningful time.*

The enlightenment he gained during his training had made Baek Museong stronger and more profound than before.

And that wasn’t the only thing that had changed. Huashan’s position was incomparable to what it had been a year ago.

Even the government offices heavily staffed by Zhongnan’s lay disciples had begun seeking Huashan first whenever trouble arose.

*If Master’s letter is true, they have no choice.*

Five days earlier, a messenger eagle sent by his Master, Heavenly Sword True Person, had brought astonishing news.

The blood calamity at Shaolin. The death of Dharma King Hong Dao. And the report that Sword Saint Mae Jonghak was being considered as a candidate for the Alliance Leader of the new Murim Alliance, which was being revived after decades.

“In any case, everyone around me is in an uproar. Even my friends have been asking me about it. They say their children seem to have a talent for martial arts, and they wonder if they might be able to enter Huashan as lay Disciples, at least.”

Baek Museong recognized the meaning concealed in the head guard’s pointed gaze and gave a bitter smile.

The man looked well past forty. He, too, must have been a parent who wanted to send his child into Huashan.

But Baek Museong pretended not to notice and answered.

“Well, if fate brings them together, it may happen. But is there really any need for a child to learn martial arts? At that age, growing up healthy is enough.”

“……I see.”

As the head guard’s face fell, Baek Museong murmured inwardly.

*If you knew about the bloody storm that will soon blow in, you wouldn’t be making that expression.*

Rumors about the blood calamity at Shaolin had already begun to leak out here and there.

But the existence of Dark Heaven remained a top-secret known only to a very small number of people. As one of those few, Baek Museong had a premonition.

A bloody wind would soon sweep through the Murim. Dark clouds would cover the sky, and thousands upon tens of thousands of weapons would tumble across the ground alongside their owners.

The wails of children who had lost their parents and parents who had lost their children would echo from every direction.

*I’ll stop that from happening. I will—and Huashan will.*

Everyone in the Murim must have felt the same way as Baek Museong.

The head guard was tilting his head at the sudden heaviness of Baek Museong’s mood when—

“Where’s the chief manager? Chief Manager!”

“Young Hero, the chief manager has stepped away for a moment. So please calm down—”

“Calm down? After I’ve been treated this poorly, do I look like I’m in any state to calm down?”

“A-as I said, the private annexes are already full. We’ll show you to a special room, so please calm down.”

“Shut up! I absolutely must use a private annex today, so get out of my way!”

“Oh, Young Hero!”

Bang! Crack!

Shouts drew closer amid the clamor. The head guard knitted his brows and spoke.

“I apologize for showing you such an unpleasant scene. It seems my subordinates have failed to handle the matter properly.”

“Please, think nothing of it. I understand completely.”

No matter how carefully Xi’an Tower chose its guests, it was still a pleasure house. Wasn’t it only natural for every kind of bug to swarm a flower garden?

“Still, it’s barely noon, and he seems quite drunk.”

“It happens from time to time. He appears to be the son of some powerful family, but we’ll settle the matter and send him home. Great Hero Baek, you needn’t concern yourself with it.”

Baek Museong let out a hearty laugh and shook his head.

“Haha, I’m not so sure. You’d better stay here.”

“Pardon?”

“He doesn’t seem like an ordinary scion of a powerful family.”

“What does that—”

The head guard faltered. He had sensed the approaching footsteps amid the ceaseless uproar.

*A martial artist!*

As the situation grew more serious by the second, the cries of the guards protecting the inner courtyard rang out alongside hurried footsteps.

“Stop!”

“You can’t pass beyond this point!”

Xi’an Tower was frequented even by high officials and powerful nobles, so the quality of its guards was high as well. But even those First Rate martial artists, rich in practical experience, were no match for the drunkard’s rampage.

“You bottom-of-the-barrel Third Rate trash from wandering martial artist backgrounds dare…”

“Gah!”

Whoosh! Thud-thud-thud!

Short cries of alarm from the guards and the fast, powerful sounds of impacts rang out. In an instant, the area outside the private annex fell silent.

Then rough, unsteady footsteps began to approach, driving the silence away.

*He took down six First Rate martial artists in an instant while that drunk?*

*A master—and not just any master. A Peak master.*

Just as the head guard’s face hardened and his hand moved toward his sword hilt, Baek Museong gave a small shake of his head.

“I think I should handle this.”

“Great Hero Baek, that’s—”

“It’s all right. We know each other from several past encounters. He’ll back down for my sake, if nothing else.”

“What do you mean?”

“Our elders have a connection that has been passed down to us. Ah, of course…”

Baek Museong scratched his cheek and added one more thing.

“It isn’t exactly a harmonious relationship.”

“……!”

At that moment, a thought flashed through the head guard’s mind like lightning.

First came the words *Zhongnan Sect*. Then a man’s name followed.

“C-could it be?”

He had only been the head guard of Xi’an Tower for a little over two weeks. But he had heard so many rumors about that man that his ears ached.

A man whose temperament was as extraordinary as the sect he came from.

The head guard twisted his expression and was just about to say the man’s name when—

Boom!

The private annex’s door, made of sturdy blackwood, exploded. Splinters flew in every direction.

Baek Museong smiled faintly at the young man approaching with a staggering gait and a face flushed red with alcohol.

“It’s been a long time. Have you been well?”

At the same time, the young man snarled.

“Why are you here?”

The face of Hyuk Sopyung, the Zhongnan One Dragon,[^1] twisted like that of an evil spirit.

* * *

“Wow! Wowww!”

“Please stop shouting. Everyone’s staring.”

“Benefactor! Candied fruit over there!”

“That damn candied fruit. Aren’t you sick of it yet?”

“No!”

“Then just open a shop!”

“Can the candied-fruit vendor come with us all the way to Sichuan?”

“No, you lunatic…”

“They sell thin noodles over there! They say the broth is made with beef!”

Cheongpung, you little bastard. You were like a rubber ball that could bounce anywhere without warning.

I quickly grabbed Cheongpung by the back of his neck as he scampered toward a roadside food stall.

“Please, let’s just live like human beings—no more, no less. Like human beings!”

“Candied fruit… thin noodles…”

“Just wait a little longer, and I’ll feed you until your belly bursts!”

“Really?”

“How many times do I have to say it? So please shut your mouth and follow quietly, okay?”

Of course, I wasn’t feeding him with my money. It was Huashan’s money. But either way, same difference.

*We should have passed straight through here, too.*

According to our original schedule, there hadn’t even been any need to stop in Xi’an.

But before we left, the Sect Leader of Huashan, Heavenly Sword True Person, had asked us to stop by Xi’an. Since it was Cheongpung’s hometown, we decided to pass through while we were at it.

We had been pushing ourselves for nearly seven days and nights without eating or washing properly. I also wanted to be hosted properly and rest for at least one day.

*I was told Huashan’s Lone Crane, Baek Museong, would be waiting for us.*

It had already been more than a year since I’d last seen him.

Before leaving for Anhui with Jeok Cheongang, Baek Museong had said this to me.



*“Contact me whenever you come to Shaanxi. I’ll treat you properly. Haha.”*



When he said he would treat me to a full course, I wondered if the guy was from Busan, but apparently it hadn’t been empty talk.

At least, judging by the fact that we were meeting like this today.

“By the way, where’s Xi’an Tower?”

According to a passerby I’d stopped to ask, we just had to follow the main road straight ahead. But why was this street so crowded? I couldn’t see an end to it.

I was looking around when a finger covered in black grime pointed toward a building in the distance.

“That is Xi’an Tower.”

“Where? Oh, you’re right. How did you know?”

Gung Gibang, the future beggar boss, answered with a proud expression.

“It is the finest place to beg. The food they leave behind and throw out is on the level of a sumptuous feast, and because people of high status come and go, they give plenty of alms. No beggar could fail to know this place.”

“……”

So it was a Beggars’ Sect hotspot.

I shook my head and walked toward Xi’an Tower.

When we reached its enormous main entrance, wide enough for ten people to pass through at once, a guard who appeared to belong to Xi’an Tower bowed his head.

“I’m sorry, but we’re closed today.”

“……What? Is it a day off?”

“Not exactly. There was a slight problem during business hours.”

“Oh.”

I hadn’t expected that.

I turned my head slightly and saw Cheongpung looking as though he was about to burst into tears.

Scratching my head, I spoke to the guard.

“Isn’t there any way around it? We had an appointment today. His name is Baek Museong. I was told you’d know him if I gave you his name.”

“Again, I’m sorry, but at the moment— Excuse me? Did you say Great Hero Baek Museong?”

“Yes. Baek Museong, Huashan’s Lone Crane.”

Cheongpung called out in an earnest voice.

“Martial Nephew Baek! Where are you, Martial Nephew Baek? Can you hear my stomach growling?”

The guard looked back and forth between us before flinging open the tightly closed main gate.

“I’ll escort you to the private annex immediately!”

*What the hell?*

*Why the sudden change in attitude?*

*Did Baek Museong stand us up?*

My guess was wrong. Following the guard as he raced ahead almost as if he were flying, we arrived at a nearly devastated private annex.

Baek Museong was waiting for us there, sword drawn.

*Wow. This is really the full course.*

*This kind of shit makes me sick of being a martial artist.*

[^1]: A sobriquet for a leading young martial artist of the Zhongnan Sect.
```
