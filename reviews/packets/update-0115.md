<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0115.txt",
      "sha256": "6ffb388b4636cc7dce95aae7a07826ea89e6897f206475a5df157d6c4eccd3a7",
      "bytes": 13518
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "70320973b93de43b9a5cd0d14d8144d4d29846bac87b4ce808534e555159be2c",
      "bytes": 1815
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "c29974913d41ef3960ce507db68c5f06346ec9d42cfd5f6f24dc344dbffd4df7",
      "bytes": 17011
    },
    {
      "path": "characters/Cheol Mubaek.md",
      "sha256": "a1b7c173f5106d12bb9f7f44b8a2a637b7d5de1aa3c82e8aea2c82ffece1323a",
      "bytes": 724
    },
    {
      "path": "characters/Hyuk Mujin.md",
      "sha256": "3bcf8c83bf78a212b58deb8bc6a2640e9d04b2ec8b1a36b3ef4d33e902507bda",
      "bytes": 5130
    },
    {
      "path": "characters/Jin Mukyung.md",
      "sha256": "e3cf359e97e5026da2876abc2f23360334afbe6e80ce709f879ad5ed1bbded76",
      "bytes": 1221
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "abc77d4f93a714f5784a30cdd2f715e994905223378d037178a6705a5fffa589",
      "bytes": 24117
    },
    {
      "path": "characters/Lee Cheonbaek.md",
      "sha256": "37e7bef4256c09dc79cb4cd7c67208ad7a4429b870b02601b5f8669dd534be9c",
      "bytes": 3231
    },
    {
      "path": "characters/Lee Seowol.md",
      "sha256": "62b4cb4eb493a3d674a0ede7a79bbf2be117eecc8cbab5845a6ad671679c0e2d",
      "bytes": 749
    },
    {
      "path": "characters/Pung Yang.md",
      "sha256": "a39f3437776ed17729440a096d2590aa572b793c43f8dd530210c0a16f176ea8",
      "bytes": 684
    },
    {
      "path": "characters/Wolhwa.md",
      "sha256": "0fe3252b748df66e3c79b7124e859dff90536a57ab8c3ab114ff30d9fa644c89",
      "bytes": 2314
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "d00f0a7e93c1ca338f95f66dac4eb4bb145f6024abc83f71c2cd236a4c63da05",
      "bytes": 16159
    }
  ],
  "estimated_tokens": 18668
}
-->

# Durable State Update — Chapter 115

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 115. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 20 concise items, `open_questions` to at most 8
items, and `temporary_decisions` to at most 8 items. Keep the serialized context
under 16384 UTF-8 bytes. Use only chapter
numbers through 115. `profile_updates` may replace one exact, uniquely occurring
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
  "chapter": 115,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 115,
    "continuity_sources": [115],
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
    "Pung Yang personally led the Red Wind Band's assault on the Mount Heng Sword Sect after the envoy's death.",
    "Pung Yang swallowed an unidentified red pill from a hard wooden case and gained overwhelming power.",
    "Pung Yang defeated Cheol Mubaek, breaking all four of his limbs and inflicting severe internal injuries.",
    "Cheol Mubaek would rather die than surrender the single-successor Shura Annihilating Fist's formula to Pung Yang, but worries about Lee Seowol.",
    "The Mount Heng Sword Sect's fortress wall has been overrun; more than one hundred mounted bandits surround Lee Seowol and the surviving defenders at the watchtower.",
    "Lee Seowol continued fighting despite exhaustion and signaled Cheol Mubaek with a fire arrow.",
    "Pung Yang appeared before Lee Seowol and demanded that she marry him.",
    "Jin Taekyung and his companions arrived at the fortress, and Cheol recognized Taekyung's Taiyuan Jin Family affiliation."
  ],
  "continuity_sources": [
    114
  ],
  "open_questions": [
    "What is the nature or origin of the red pill that empowered Pung Yang?",
    "How will Lee Seowol respond to Pung Yang's marriage demand?",
    "Can Jin Taekyung and his companions reach or rescue Lee Seowol and Cheol Mubaek?",
    "Whether the Mount Heng Sword Sect will survive the continuing assault remains unresolved."
  ],
  "safe_through": 114,
  "temporary_decisions": [
    "Render 일류 초입 as early First Rate.",
    "Retain shichen and explain three shichen as six hours in context.",
    "Render 화시 as fire arrow, 쇠뇌 as crossbow, and 충차 as battering ram.",
    "Render 수라멸권 as Shura Annihilating Fist.",
    "Render 항산권문 as Mount Heng Fist Sect.",
    "Render 벽곡단 as fasting pills."
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

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 진무경    | **Jin Mukyung**    |
| 혁무진    | **Hyuk Mujin**     |
| 이천백    | **Lee Cheonbaek**  |
| 이소월    | **Lee Seowol**     |
| 철무백    | **Cheol Mubaek**   |
| 월화     | **Wolhwa**         |
| 산서잠룡   | **Sleeping Dragon of Shanxi** | Jin Taekyung   |
| 진천검    | **Heaven Shaking Sword**      | Jin Mukyung    |
| 혈랑검    | **Blood Wolf Sword**          | Lee Cheonbaek  |
| 항산호    | **Tiger of Mount Heng**       | Cheol Mubaek   |
| 태원진가   | **Jin Family of Taiyuan**        |
| 항산검문   | **Mount Heng Sword Sect**        |
| 절정     | **Peak**          |
| 무인     | **martial artist**                               | Default term                                          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 경지     | **realm** / **realm stage**                      | Especially power level                                |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 단전     | **dantian**                                      | Preserve the wuxia term                               |
| 구결     | **formula**                                      | Mnemonic/oral formula for a martial art               |
| 검기     | **Sword Energy**                                 | When functioning as projected weapon qi               |
| 정파     | **orthodox faction**                             |                                                       |
| 마적     | **mounted bandits**                              |                                                       |
| 문주     | **Sect Leader**                              |
| 은인     | **Benefactor**                               |
| 일격     | **One Strike**                         |
| 상태               | **Status**                     |
| 명성               | **Fame**                       |
| 산서     | **Shanxi**             |
| 태원     | **Taiyuan**            |
| 항산     | **Mount Heng**         |
| 팔천협    | **Eight Spring Gorge** |
| 대협      | **Great Hero** or **Sir** depending tone                        |
| 공자      | **Young Master**                                                |
| 소저      | **Young Lady**                                                  |
| 풍양 | **Pung Yang** | Personal name of the Red Wind Band Leader. |
| 이공자 | **Second Young Master** | Title used for Jin Mukyung. |
| 항산검문주 | **Sect Leader of the Mount Heng Sword Sect** | Title for Lee Seowol, the sect's current leader. |
| 적풍단 | **Red Wind Band** | Rising mounted-bandit power from the northern plateau. |
| 적풍단주 | **Red Wind Band Leader** | Unnamed leader of the Red Wind Band; commands two hundred followers. |
| 소월 | **Seowol** | Short form of Lee Seowol used by Cheol Mubaek. |

## Listed compact profiles

### Cheol Mubaek.md

# Cheol Mubaek (철무백)

- **Safe through:** Chapter 114
- **Aliases:** Tiger of Mount Heng
- **Role:** Peak master known as the Tiger of Mount Heng; longtime close friend and peer of Lee Cheonbaek; protector of Lee Seowol
- **Personality:** Fierce, short-tempered, intimidating, and fiercely protective; becomes gentle and attentive toward Seowol
- **Voice:** Roaring and confrontational when rebuking the Mount Heng senior figures; gentle and affectionate when speaking to Seowol
- **Relationships:** Close friend and peer of Lee Cheonbaek; paternal uncle and protector of Lee Seowol; feared and respected by the Mount Heng Sword Sect's senior figures

### Hyuk Mujin.md

# Hyuk Mujin (혁무진)

- **Safe through:** Chapter 113
- **Aliases:** None revealed
- **Role:** First Rate martial artist from a tenant-farmer family; Captain of the Gatekeepers at the Jin Family of Taiyuan; deputy squad leader of White Tiger Hall’s reconnaissance squad; candidate to become the next Master of the Gatekeeper Pavilion
- **Personality:** Young, disciplined, suspicious of Jin Taekyung, and openly contemptuous of the family’s disgraced third son; believes loyalty and respectable conduct matter, but is also proud and hungry for glory
- **Voice:** Formal and clipped when performing his duties; blunt and moralizing when addressing Taekyung
- **Relationships:** Gatekeeper under the Jin Family; deputy subordinate to Jin Taekyung in the reconnaissance squad

### Jin Mukyung.md

# Jin Mukyung (진무경)

- **Safe through:** Chapter 113
- **Aliases:** Heaven Shaking Sword; Jin Family Second Young Master
- **Role:** Second son of the Jin Family of Taiyuan; twenty-three-year-old cadet at Heaven’s Gate Temple; a young Peak-level genius swordsman
- **Personality:** Reserved, terse, and easily irritated by exaggerated praise; glares coldly when Taekyung identifies him
- **Voice:** Quiet and resonant; clipped and blunt in direct speech
- **Relationships:** Taekyung’s older brother and current martial arts instructor; returned to the Jin Family after several years away

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 114
- **Aliases:** Sleeping Dragon of Shanxi
- **Role:** Modern-world protagonist; recently fired after seven years at his job; C-rank Hunter who defeated eight B-rank Minotaurs and killed a Level 70 B-rank Minotaur Warrior in one blow; First Rate martial artist standing before the Peak realm; youngest son of the Jin Family of Taiyuan; new owner of a two-story detached house in Goyang intended for his family; Qi Sense reaches a seventy-meter radius
- **Personality:** Hungry, self-aware, dryly observant, and willing to take a questionable opportunity when desperate; treats the impossible as a game until the danger becomes undeniable
- **Voice:** First-person, conversational, dryly self-mocking; uses vivid trap-and-prey imagery, game jargon, and occasional profanity
- **Relationships:** Jin Mukyung’s younger brother and current student; son of a deceased father; supports his mother and younger sibling; has a strained relationship with Lee Seowol, the current Sect Leader of the Mount Heng Sword Sect

### Lee Cheonbaek.md

# Lee Cheonbaek (이천백)

- **Safe through:** Chapter 113
- **Aliases:** Blood Wolf Sword
- **Role:** Former Sect Leader of the Mount Heng Sword Sect, killed during the Red Wind Band’s assault; father of Lee Seogeun and Lee Seowol
- **Personality:** Grief-stricken, resolute, and fiercely vengeful
- **Voice:** Quietly mournful when addressing his son; firm and uncompromising when declaring revenge
- **Relationships:** Deceased father of Lee Seogeun and Lee Seowol; also father of a deceased Young Sect Leader; former leader of the Mount Heng Sword Sect; longtime close friend and peer of Cheol Mubaek

### Lee Seowol.md

# Lee Seowol (이소월)

- **Safe through:** Chapter 114
- **Aliases:** None
- **Role:** Current Sect Leader of the Mount Heng Sword Sect; third child of Lee Cheonbaek and his last surviving descendant; publicly insists on being addressed as Sect Leader rather than Young Lady
- **Personality:** Cold, commanding, and composed; capable of stopping a fierce confrontation with a calm request
- **Voice:** Clear and cool, gentle with Cheol Mubaek but frost-cold and firm when asserting her authority
- **Relationships:** Daughter of the deceased Lee Cheonbaek; younger sister of the deceased Young Sect Leader, Lee Seogeun, and Lee Seogwang; Cheol Mubaek's niece and protected charge

### Pung Yang.md

# Pung Yang (풍양)

- **Safe through:** Chapter 114
- **Aliases:** Red Wind Band Leader
- **Role:** Leader of the Red Wind Band, commanding at least two hundred mounted bandits; became a mounted bandit at thirteen, reached First Rate by age thirty, and rose from squad leader to band leader three years ago
- **Personality:** Foxlike, ruthless, observant, controlled, and willing to kill subordinates who disobey his orders
- **Voice:** Calm, concise, and authoritative when issuing orders
- **Relationships:** Leads the Red Wind Band and controls former members of other mounted-bandit groups who joined his force

### Wolhwa.md

# Wolhwa (월화)

- **Safe through:** Chapter 113
- **Aliases:** Eun Sowol (은소월); Wolhwa is the name used at Honghwaru
- **Role:** Shanxi’s foremost information merchant and Level 50 martial artist; Branch Leader of the Lower District Sect’s Shanxi branch; formerly posing as a high-ranking courtesan at Honghwaru, a pleasure house in central Taiyuan
- **Personality:** Striking, composed, observant, direct, quietly amused, and capable of ruthless, decisive violence when extracting information; comfortable teasing Taekyung while conducting serious information and negotiation work
- **Voice:** Polite and lightly playful; addresses Taekyung as Young Master Jin and delivers embarrassing observations without raising her voice
- **Relationships:** Knows Taekyung as a Honghwaru regular and the youngest son of the Jin Family; says she likes him, though her sincerity is unclear

## Korean source

```text
＃115화



항산호 철무백.

이미 몇 번 들어 본 이름이다. 월화는 그가 없었다면 항산검문은 진작 적풍단에게 멸문당했을 거라고 했다.



‘혈랑검 이천백과 비견되거나 그 이상이라고 평가받는 절정 고수예요.’



분명히 그랬었는데.

‘그 대단한 절정 고수가 왜 이 꼴이 되어 있나.’

기이한 방향으로 꺾여 있는 사지, 상의를 흠뻑 적신 검은 핏물은 심각한 내상의 증거다. 철무백이 흐릿한 눈빛으로 우리를 바라보았다.

“태원……진가?”

“어, 알아보시네?”

나는 억지로 입꼬리를 끌어 올렸다. 위중한 상태인 철무백을 조금이라도 안심시키기 위해서다.

지금 내 눈앞에 있는 그는 쟁쟁한 위명의 절정 고수가 아닌, 마지막 희망을 발견한 노인에 지나지 않았다.

“적풍단, 안에, 소월이가 위험…….”

힘겹게 이어 가는 철무백의 말을 듣지 않았어도 이 자리의 모두는 사태의 심각성을 알고 있다. 시선이 닿는 곳마다 시체와 핏물이 넘쳐 났으니까.

‘하지만 아직 늦지는 않았어.’



제한 시간 : 00:05:12



아슬아슬하게 시간을 맞췄다. 문제는 항산호 철무백을 이 꼴로 만들어 놓은 놈이 저 안에 있다는 사실이지.

월화도 나와 같은 생각을 한 모양이다. 그녀가 철무백을 진정시키며 물었다.

“철 대협, 풍양이 다른 고수와 합공을 했나요?”

철무백이 미약하게 고개를 저었다.

“풍양이 단신으로 철 대협을 꺾었다는 말씀이세요?”

“부, 붉은 단환. 놈을 조심…….”

붉은 단환?

더 물어보고 싶었지만 철무백의 한계는 거기까지였다. 소리 없이 입을 벙긋거리던 그의 고개가 푹 꺾이자 혁무진이 헛숨을 들이켰다.

“주, 죽었다.”

“……아직 살아 있어.”

“아, 그러네요. 숨결이 너무 미약해서 그만.”

산 사람마저 죽이는 혁무진 이 새끼는 도대체…….

그러나 녀석의 말도 아주 틀린 것은 아니다. 철무백의 가느다란 숨결은 언제 끊길지 모를 정도로 위태로웠다.

월화가 품 안에서 조그마한 자기병을 꺼낸 것은 그때였다.

“거기 목 좀 들어 주시겠어요?”

그녀가 기절한 철무백의 입으로 병을 기울였다.

정체 모를 녹색 액체가 흘러 들어가자 창백했던 안색에 조금씩 핏기가 도는 것이, 상당히 효과가 좋은 약물인 것 같았다.

“이걸로 한숨 돌릴 순 있겠지만 말 그대로 임시방편이에요. 지금의 철 대협의 상태로는 어린아이도 감당 못 해요, 아시죠?”

요컨대 누군가는 남아서 만약의 사태로부터 철무백을 지켜야 한다는 뜻이다. 나는 망설임 없이 고개를 끄덕였다.

“그럼 무진이가…….”

“두 사람이 남으시오.”

“응? 두 사람?”

이게 무슨 소리야. 나와 시선이 마주친 진무경이 뭐 잘못됐냐는 얼굴로 되물었다.

“왜?”

“아니, 우리 둘이 가자고?”

“문제 있나?”

“…….”

당연히 있지.

‘한가락 하는 절정 고수인 철무백을 반송장으로 만든 풍양에, 그 휘하 마적 놈들까지.’

고양이 손이라도 빌려야 할 판국인데, 뭐?

아직 불안한 수준인 혁무진은 몰라도 월화는 데려가야 한다는 게 내 생각이다.

“두 분이서 가능하시겠어요?”

월화의 물음에 내가 재빨리 입을 열었다.

“그거야 당연히…….”

“할 수 있소.”

불가능하다고 말하려던 찰나, 진무경의 깊고 검은 눈동자가 나를 응시했다.

“할 수 있다고 했다. 날 믿어라.”

그 담담하면서도 확신에 찬 한마디에 말문이 막혔다.

순간 치기 어린 젊은이의 객기인가 하는 생각도 들었지만, 내심 고개를 가로젓고 있는 스스로를 발견했다.

‘진천검. 무공의 천재.’

눈앞의 이 녀석은 노력과 재능이 결합해 탄생한 괴물이다. 지금까지 지켜본 바로는 스스로 개죽음을 자처할 만큼 어리석지도 않다.

그리고…….



제한 시간 : 00:02:21



젠장, 더 이상 망설일 시간도 없다.

나는 한숨을 푹 내쉬고 진무경을 향해 물었다.

“자신 있어?”

“이게 최선이다. 어중간한 수준으로는 오히려 짐만 될 뿐이야.”

진무경의 대답에 월화가 피식 웃었다.

“어머, 너무 솔직하신데요?”

“……그 부분은 미안하게 생각하오.”

“뭐, 괜찮아요. 틀린 말은 아니니까.”

저놈이 누구한테 사과하는 건 처음 보네.

다시 보기 힘든 이 희귀한 광경에 혁무진이 끼어들었다.

“이공자님, 저도 무인입니다!”

“그럼 따라오거라. 단, 살아남는 건 알아서 하고.”

“알아서…… 말입니까?”

“장담하건대, 싸움이 시작되면 적들은 너부터 노릴 것이다. 무인답게 장렬히 싸우다 죽는 것도 나쁘지 않겠지.”

잠깐 침묵하던 혁무진이 결의에 찬 얼굴로 대답했다.

“무인으로서, 같은 무도(武道)를 걷는 철 대협을 안전하게 모시고 있겠습니다.”

“…….”

가끔 보면 저게 사람인가 싶다.

‘시간만 있으면 두들겨 패는 건데.’

하지만 이 와중에도 시간은 계속해서 흐르고 있었다.



제한 시간 : 00:01:09



“후우.”

미리 꺼내어 둔 창을 단단히 말아 쥐며 진무경에게 말을 건넸다.

“내가 조무래기들을 맡을게.”

“보통 이런 시점에서는 스스로 우두머리를 맡겠다고 하지 않나?”

“응, 그런 고정 관념을 버려.”

“웃기는 놈이군.”

“분수를 안다고 해 두자.”

“투지와 호승심은 무인을 성장시킨다.”

“그리고 죽음을 촉진시키겠지. 상대를 봐 가면서 덤비는 건 배웠으니까 그 넘치는 투지와 호승심으로 풍양 좀 처리해 줘.”

“말은 청산유수로구나.”

“아, 그리고 들어가면 최대한 은밀히 접근한 다음 내가 신호하면 기습하고. 알았지?”

“기습?”

“기습의 묘리를 살려서 초반에 최대한 큰 피해를 입히고 시작하는 거지. 적들이 우왕좌왕하는 사이에 항산검문주를…….”

“그렇군.”

“좋아, 오랜만에 말이 통하네.”

이걸로 모든 준비는 끝났다. 40초, 39초, 38초.

떨어지는 숫자를 보며 문을 향해 걸음을 떼려던 찰나였다.

저벅.

말리고 자시고 할 시간도 없었다.

성큼 안으로 걸어 들어간 진무경이 공력을 실은 외침을 토해 냈다.

“풍양-!”

띠링.



- [제한 시간]이 사라집니다.



“…….”

진무경 이 개새끼야.



* * *



“혼인? 차라리 죽음을 택하겠다.”

자기 자신의 목에 은장도를 뽑아 겨눈 이소월을 보며 풍양은 혀를 찼다.

“어지간히 애먹이는군. 혈랑검의 여식다워.”

뛰어난 비도술의 소유자인 풍양이지만 현재로서는 그의 장기를 십분 발휘할 수 없었다.

‘망할 노인네…… 결국 잠력단(暫力丹)을 쓰게 만들다니.’

풍양에게도 고작 세 개밖에 없는 귀물이다. 그중 하나를 쓴 덕분에 철무백을 쓰러트릴 수 있었지만 후유증이 제법 컸다.

그는 사시나무처럼 떨리는 손을 소매 아래로 감추며 말했다.

“숨이 붙어 있는 놈들을 모두 끌고 와.”

“옛.”

명령이 떨어지고 얼마 되지 않아 곧장 포박당한 채 끌려오는 항산검문의 무인들. 이소월의 얼굴에 어둠이 내려앉았다.

“무슨 짓을 할 셈이냐?”

풍양이 빙긋 웃었다.

“대충 짐작하고 있을 텐데? 우선 소저가 보는 앞에서 저들의 사지를 하나씩 자를 거요. 팔, 다리, 뭐 이것저것. 썩 유쾌한 광경은 아니니 눈을 감고 있는 걸 추천하지.”

“그런 짓을 했다간…….”

“자결하겠다면 말리지는 않겠소. 충성심 깊은 수하들은 그 대가로 도륙을 당하겠지만.”

이소월이 이를 악물었다.

“당신이 원하는 게 그건 아닐 텐데?”

“혼인 상대가 죽어 버리겠다는데 어쩔 수 없지. 그래도 혈랑검의 독문무공과 항산호의 무공 구결 정도면 충분히, 아. 돌아가는 길에 철무백 그 노인네도 데려가야겠군.”

“……철 숙부가, 아직 살아 계신다고?”

“당연한 소리를. 귀한 무공 구결을 넘겨줄 은인을 그렇게 쉽게 죽일 수야 있나.”

“…….”

“내 목을 걸고 하나 약속하지. 지금이라도 늦지 않았으니 나와 혼인하시오. 하면 단전을 폐하는 선에서 모두 살려 주리다.”

그게 결정타였다. 한동안 속눈썹을 파르르 떨던 이소월이 천천히 손을 내렸다.

“약속은 지켜라.”

“좋은 선택이오.”

풍양의 얼굴에 득의양양한 웃음이 어렸다.

오늘부로 그는 세 번째 인생을 살게 됐다.

거지 소년에서 마적. 마적에서 비로소 정파의 탈을 뒤집어쓰고 항산검문의 실질적인 주인이 됐다.

비록 큰 피해를 입었지만 상관없다. 새 술은 새 부대에 담는 법. 항산검문의 이름으로 무인들을 모집하고 세력을 키워 나갈 것이다.

‘삼십여 년 전 혈랑검도 했던 일을 내가 못 하랴.’

넘치는 희열에 입꼬리가 솟구친 그 순간이었다.

“풍양-!”

공력이 담긴 외침이 천지를 뒤흔들었다.

이소월과 풍양. 그리고 살아남은 모든 이들이 약속이라도 한 듯이 고개를 틀었다.

밤처럼 새카만 흑의(黑衣)를 걸친 청년이 오십여 장 밖에서 걸어오고 있었다.

‘고수.’

풍양은 청년의 송곳 같은 눈빛에 가슴 한구석이 서늘해졌다.

고수다. 그것도 자신과 비교해 결코 떨어지지 않는 절정 고수. 검파를 잡아 가는 손놀림만 봐도 알 수 있었다.

‘이 정도로 젊은 절정 고수는 산서성에 둘뿐이지. 특히 검수(劍手)라면…….’

답은 바로 나왔다. 진천검 진무경. 불과 약관의 나이에 절정의 경지에 오른 천재.

무엇보다 그의 뒤에는 산서제일가로 우뚝 선 태원진가가 버티고 있다.

‘그나마 혼자 왔으니 다행이군.’

그러나 다음 순간, 진무경이 들어온 성문에서 또 다른 한 사람이 슬쩍 고개를 내밀었다.

청년은 남색 무복을 입고 있었다. 복식, 손에 든 묵색 철창, 무엇보다 진무경과 빼다 박은 얼굴이 그가 누구인지를 알려 주었다.

“산서잠룡?”

누군가의 입에서 튀어나온 별호에 진태경이 움찔하더니 중얼거렸다.

“시발, 내 이렇게 될 줄 알았다.”

명문가 자제답지 않은 걸쭉한 욕설과 함께 휘적휘적 걸어오는 진태경, 느긋한 걸음걸이의 진무경.

두 형제의 발걸음이 향하는 쪽에 풍양이 있었다.

‘하필 이럴 때 태원진가라…… 매우 좋지 않아.’

오랜 세월 가문이 쌓아 올린 평판과 팔천협 전투로 얻은 명성. 현재 태원진가의 위상은 독보적이었다.

그 덕분에 산서성 전역에서 수많은 젊은이가 무인을 꿈꾸며 앞다투어 태원진가로 몰려드는 중이다.

그것이 당장 풍양이 항산검문을 삼키더라도 넙죽 엎드린 채 발톱을 숨겨야 하는 이유였다.

‘이번 고비만 넘기면 기회는 온다.’

이미 항산검문은 무너졌다. 무림은 약육강식의 세계고 풍양은 새로운 강자다. 그는 상대가 태원진가라 해도 자신이 충분히 존중받을 만한 자격을 갖췄다고 생각했다.

저벅, 저벅, 저벅.

진무경, 진태경 형제가 발걸음을 옮길 때마다 적풍단의 마적들이 분분히 물러섰다.

풍양은 어느새 코앞까지 다가온 두 사람을 향해 포권을 취했다.

“적풍단주, 풍양이라 하오.”

풍양이 그 어느 때라도 경계심을 늦추지 않는 노련한 무림인이 아니었다면, 아직 잠력단의 효능이 미약하게 남아 있지 않았더라면 그 일격을 피하지 못했을 것이다.

쉬이이잉-!

그는 황급히 몸을 뒤집었다. 목을 스쳐 간 눈부신 검기(劍氣) 한 줄기가 뒤에 있던 마적 셋을 베어 냈다.

“이게 태원진가의 뜻이냐!”

풍양의 노호성에 이미 가까이 있는 마적들을 쓰러트린 진태경이 중얼거렸다.

“난 말로 하고 싶은데.”

“이런 개호로…….”

쉬이이익! 서걱!

말을 끝마치기도 전에 날아온 검기가 풍양의 등을 훑었다. 불에 덴 듯한 통증. 간신히 이어지는 공격을 피한 그는 진무경에 대한 평가를 수정해야 했다.

‘나보다 더 강하다.’

이 정도라면 철무백에게 비견될 만한 움직임이다. 거기에 더해 수하들을 학살하고 있는 진태경까지.

풍양은 자신에게 남은 선택지가 하나밖에 없음을 깨달았다.

‘잠력단.’

그는 품속에 감춰 뒀던 목곽을 꺼냈다. 진무경을 막기 위해 수하들이 죽어 나가는 사이, 단환을 입 안에 털어 넣었다.

쉬이이익!

어느새 핏빛으로 물든 풍양의 눈동자에 진무경의 푸른 검기가 비쳤다.

서걱!
```

## Final English reading copy

```markdown
# Chapter 115

Cheol Mubaek, the Tiger of Mount Heng.

I had heard that name several times already. Wolhwa had said that without him, the Mount Heng Sword Sect would have been wiped out by the Red Wind Band long ago.

*“He’s considered a Peak master comparable to or even stronger than the Blood Wolf Sword, Lee Cheonbaek.”*

She had definitely said that.

*Then why has that incredible Peak master ended up like this?*

His limbs were twisted at unnatural angles, and the black blood soaking his shirt was proof of severe internal injuries. Cheol Mubaek looked at us through hazy eyes.

“Taiyuan… Jin Family?”

“Oh, you recognize us?”

I forced the corners of my mouth upward. I wanted to reassure Cheol Mubaek, who was in critical condition, even if only a little.

The man before me was no longer the renowned Peak master known throughout the Murim. He was nothing more than an old man who had found his last hope.

“Red Wind Band… inside… Seowol’s in danger…”

Even without hearing Cheol Mubaek’s halting words, everyone here understood how serious the situation was. Everywhere we looked, there were corpses and pools of blood.

*But it’s not too late yet.*

> **System**  
> **Time Limit:** 00:05:12

We had made it just in time. The problem was that the bastard who had reduced the Tiger of Mount Heng to this state was still inside.

Wolhwa seemed to have reached the same conclusion. She calmed Cheol Mubaek and asked,

“Sir Cheol, did Pung Yang attack you together with another master?”

Cheol Mubaek gave a faint shake of his head.

“You’re saying Pung Yang defeated Sir Cheol by himself?”

“R-red pill. Be careful of that bastard…”

A red pill?

I wanted to ask more, but that was the limit of Cheol Mubaek’s strength. His lips moved soundlessly, then his head drooped. Hyuk Mujin sucked in a startled breath.

“H-he’s dead.”

“…He’s still alive.”

“Oh. So he is. His breathing was just so faint…”

Hyuk Mujin, you bastard. What kind of person kills even the living?

Still, he wasn’t entirely wrong. Cheol Mubaek’s thin breath was so precarious that it could stop at any moment.

That was when Wolhwa pulled a small porcelain bottle from inside her robes.

“Could you lift his head a little?”

She tilted the bottle into the unconscious Cheol Mubaek’s mouth.

As an unidentified green liquid trickled down his throat, color gradually returned to his pale face. It seemed to be a remarkably effective medicine.

“This will help him catch his breath, but it’s only a temporary measure. In his current condition, even a child would be too much for him to handle. You understand, right?”

In short, someone had to stay behind to protect Cheol Mubaek in case something happened. I nodded without hesitation.

“Then Mujin can—”

“Two people stay behind.”

“Huh? Two people?”

What was he talking about? Jin Mukyung met my gaze and looked back at me as if he couldn’t understand what the problem was.

“Why?”

“No, you mean the two of us should go?”

“Is there a problem?”

…

Of course there was.

*Pung Yang had turned a formidable Peak master like Cheol Mubaek into a half-dead man, and he still had all those mounted-bandit bastards under his command.*

We were at the point where we needed every hand we could get, and he was suggesting this?

I didn’t know about Hyuk Mujin, whose abilities were still questionable, but Wolhwa absolutely had to come with us.

“Can the two of you manage?” Wolhwa asked.

I hurriedly opened my mouth.

“Obviously, that’s—”

“We can.”

Just as I was about to say it was impossible, Jin Mukyung’s deep, dark eyes fixed on me.

“I said we can. Trust me.”

His calm yet confident words left me speechless.

For a moment, I wondered if this was merely the reckless bravado of an immature young man. But then I realized I was shaking my head inwardly.

*The Heaven Shaking Sword. A martial arts genius.*

The guy standing before me was a monster born from the combination of effort and talent. From everything I had seen, he wasn’t foolish enough to throw his life away for nothing.

And then…

> **System**  
> **Time Limit:** 00:02:21

Damn it. There was no time left to hesitate.

I let out a deep sigh and asked Jin Mukyung,

“Are you confident?”

“This is the best option. Someone of middling skill would only become a burden.”

Wolhwa let out a quiet laugh.

“My, you’re awfully honest.”

“…I apologize for that.”

“Well, that’s all right. You’re not wrong.”

That was the first time I had ever seen him apologize to anyone.

Hyuk Mujin interrupted this rare spectacle.

“Second Young Master, I’m a martial artist too!”

“Then follow us. But staying alive is your responsibility.”

“On my own…?”

“I guarantee that once the fighting begins, the enemy will target you first. There’s nothing wrong with fighting bravely as a martial artist and dying.”

After a brief silence, Hyuk Mujin answered with a resolute expression.

“As a martial artist, I will safely protect Sir Cheol, who walks the same path of martial arts as I do.”

…

Sometimes, I wondered if that guy was even human.

*If I had the time, I’d beat the hell out of him.*

But even now, time continued to pass.

> **System**  
> **Time Limit:** 00:01:09

“Whew.”

I gripped the spear I had already taken out and spoke to Jin Mukyung.

“I’ll handle the small fry.”

“Usually, at a time like this, shouldn’t you say that you’ll take the leader?”

“Yeah. Throw away that stereotype.”

“You’re ridiculous.”

“Let’s just say I know my place.”

“Fighting spirit and competitive pride help a martial artist grow.”

“And hasten his death. I’ve learned to choose my opponents carefully, so deal with Pung Yang using all that overflowing fighting spirit and competitive pride.”

“You certainly have a way with words.”

“Oh, and when we get inside, approach as quietly as possible. Then ambush them when I give the signal. Got it?”

“Ambush?”

“Use the essence of an ambush to inflict as much damage as possible at the beginning. While the enemies are thrown into confusion, we’ll get to the Sect Leader of the Mount Heng Sword Sect…”

“I see.”

“Good. It’s nice to be understood for once.”

That took care of every preparation. Forty seconds. Thirty-nine. Thirty-eight.

I watched the numbers fall and was just about to walk toward the door when—

Clomp.

There wasn’t even time to stop him.

Jin Mukyung strode inside and let out a shout infused with internal energy.

“Pung Yang!”

> **System**  
> **Time Limit** has disappeared.

…

Jin Mukyung, you fucking asshole.

* * *

“Marriage? I’d choose death instead.”

Pung Yang clicked his tongue as he watched Lee Seowol draw a silver dagger and hold it to her own throat.

“You’re making this awfully difficult. You really are the Blood Wolf Sword’s daughter.”

Though Pung Yang was a master of throwing knives, he couldn’t fully display his specialty in his current condition.

*Damn old man… He actually forced me to use the Temporary Strength Pill.[^1]*

Even Pung Yang possessed only three of these precious pills. Using one had allowed him to defeat Cheol Mubaek, but the aftereffects were considerable.

He hid his hands, trembling like aspen leaves, beneath his sleeves and said,

“Bring everyone who’s still breathing.”

“Yes, Leader.”

Not long after the order was given, martial artists from the Mount Heng Sword Sect were dragged over, bound hand and foot. Darkness settled over Lee Seowol’s face.

“What are you planning to do?”

Pung Yang smiled.

“You can probably guess. First, I’ll cut off their limbs one by one in front of you. Arms, legs, this and that. It won’t be a pleasant sight, so I recommend closing your eyes.”

“If you do that…”

“If you’re going to kill yourself, I won’t stop you. But your loyal subordinates will be slaughtered for it.”

Lee Seowol clenched her teeth.

“That isn’t what you want, is it?”

“If my bride-to-be says she’s going to die, what else can I do? Still, the Blood Wolf Sword’s secret martial art and the Tiger of Mount Heng’s martial arts formula would be enough. Ah, I should take that old man Cheol with me on the way back, too.”

“…Uncle Cheol is still alive?”

“Of course. How could I kill a Benefactor who is going to hand over such a precious martial arts formula?”

“…”

“I’ll stake my life on this promise. It’s not too late even now, so marry me. If you do, I’ll let everyone live. I’ll stop at destroying their dantians.”

That was the decisive blow.

Lee Seowol’s eyelashes trembled for a while before she slowly lowered her hand.

“Keep your promise.”

“A wise choice.”

A triumphant smile spread across Pung Yang’s face.

From this day forward, he would begin his third life.

He had gone from a beggar boy to a mounted bandit. Now, he would finally don the mask of an orthodox faction and become the true master of the Mount Heng Sword Sect.

Though there had been heavy losses, it didn’t matter. New wine belonged in new wineskins. Under the name of the Mount Heng Sword Sect, he would recruit martial artists and expand his power.

*If the Blood Wolf Sword could do the same thing over thirty years ago, why couldn’t I?*

Just as the corners of his mouth lifted with overflowing delight—

“Pung Yang!”

A shout infused with internal energy shook the heavens and earth.

Lee Seowol, Pung Yang, and every surviving person turned their heads as if they had made a pact.

A young man dressed in black as dark as night was walking toward them from some fifty jang away.[^2]

*A master.*

A chill ran through some corner of Pung Yang’s chest beneath the young man’s needle-sharp gaze.

He was a master. And not merely a master—he was a Peak master who was in no way inferior to Pung Yang himself. Pung Yang could tell just from the way the young man’s hand moved as it gripped his sword hilt.

*There are only two Peak masters this young in Shanxi. And if one of them is a swordsman…*

The answer came immediately.

Jin Mukyung, the Heaven Shaking Sword. A genius who had reached the Peak realm while still in his early twenties.

More importantly, behind him stood the Jin Family of Taiyuan, which had risen to become the foremost family in Shanxi.

*At least he came alone.*

But the next moment, another person cautiously stuck his head out through the fortress gate Jin Mukyung had entered.

The young man wore a navy martial robe. His clothing, the dark iron spear in his hand, and above all, his nearly identical face told Pung Yang who he was.

“The Sleeping Dragon of Shanxi?”

At the nickname that escaped someone’s mouth, Jin Taekyung flinched and muttered,

“Fuck. I knew this would happen.”

Jin Taekyung came sauntering forward, cursing crudely in a manner unbecoming a scion of a prestigious family, while Jin Mukyung followed at an easy pace.

The two brothers were heading straight toward Pung Yang.

*The Taiyuan Jin Family, at a time like this… This is very bad.*

The family’s reputation, built over many years, and the fame it had gained through the battle at Eight Spring Gorge had made the Jin Family’s current standing unrivaled.

Because of that, countless young people across Shanxi who dreamed of becoming martial artists were flocking to the Jin Family.

That was why, even if Pung Yang swallowed the Mount Heng Sword Sect right now, he would still have to bow flat and hide his claws.

*Once I get past this hurdle, my opportunity will come.*

The Mount Heng Sword Sect had already collapsed. The Murim was a world where the strong preyed on the weak, and Pung Yang was a new power in that world. Even if his opponent was the Taiyuan Jin Family, he believed he had earned the right to be treated with respect.

Clomp. Clomp. Clomp.

Each time Jin Mukyung and Jin Taekyung took a step, the mounted bandits of the Red Wind Band retreated in confusion.

By the time the two men reached him, Pung Yang raised his hands in a formal salute.

“I am Pung Yang, Red Wind Band Leader.”

If Pung Yang had not been a seasoned martial artist who never lowered his guard, or if the effects of the Temporary Strength Pill had not still lingered faintly, he would never have avoided that strike.

Shiiiiing!

He hurriedly twisted his body.

A dazzling streak of Sword Energy skimmed past his neck and sliced through three mounted bandits behind him.

“Is this the will of the Taiyuan Jin Family?”

Jin Taekyung, who had already felled the mounted bandits nearby, muttered,

“I’d rather talk it out.”

“You fucking bast—”

Before Pung Yang could finish speaking, another streak of Sword Energy flew in and grazed his back.

The pain felt like being burned by fire.

He barely avoided the continuing attack, and his assessment of Jin Mukyung had to change.

*He’s stronger than me.*

At this level, Jin Mukyung’s movements were comparable to Cheol Mubaek’s. On top of that, Jin Taekyung was slaughtering Pung Yang’s subordinates.

Pung Yang realized that he had only one option left.

*The Temporary Strength Pill.*

While his subordinates died one after another trying to stop Jin Mukyung, Pung Yang pulled the wooden case hidden inside his robes and tipped the pill into his mouth.

Shiiiiing!

Jin Mukyung’s blue Sword Energy was reflected in Pung Yang’s eyes, which had turned blood-red.

Slice!

[^1]: The pill’s name literally means “Temporary Strength Pill.”

[^2]: A jang is a traditional unit of distance, roughly three meters.
```
