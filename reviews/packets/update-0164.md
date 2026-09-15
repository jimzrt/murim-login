<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0164.txt",
      "sha256": "db91f4e84528a57d5e7b54d50ef137debef0f359f2f5e12d47bec823d2d28739",
      "bytes": 15196
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "4d25c0e4864eb0b57b12477c5213ef37e32990fb0370abc52be0debac04ef74c",
      "bytes": 1674
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "fcd18dd40779b02a6a2cfa7517e1d4c760cef47a20918c27cd48a3b09e4495dc",
      "bytes": 40001
    },
    {
      "path": "characters/Cheongpung.md",
      "sha256": "5645e6847806dc98b95412bf13d56a7101fb5ce2f1635d57fa6ab959fa5808d6",
      "bytes": 1690
    },
    {
      "path": "characters/Gwak Jun.md",
      "sha256": "2d27f3468fb418c752b87587690d9254a2b7909d2923530f6497d1ce4f685253",
      "bytes": 1451
    },
    {
      "path": "characters/Hyuk Mujin.md",
      "sha256": "e64e038512f6315a2bb7a2636b098e9fc63ab87d083060b31855b7f44c8813f6",
      "bytes": 5558
    },
    {
      "path": "characters/Jin Mukyung.md",
      "sha256": "c5bc88826213ecd3db8ddecff1af6b3291be27b2f7340602cdb5ef67b08431d7",
      "bytes": 1826
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "a19bb68992f1be9814b3729ad3c0576328f82f1c927fcfae584df26be1c1a4a1",
      "bytes": 24770
    },
    {
      "path": "characters/Jin Wikyung.md",
      "sha256": "c0fc110d0d2f461e3465aaca9b67e1cf14fed4426fd69d8f5a889c9ae927ee37",
      "bytes": 8179
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "5c9c0a75b2d16367bacd658985a0ac4452f12527cf9234a2dbe6d7bc5167af5d",
      "bytes": 622
    },
    {
      "path": "characters/Wipeng.md",
      "sha256": "1def987f674eaadb7c0ec87b781d68993e49a68da9ef843267112ac939c9187c",
      "bytes": 4701
    },
    {
      "path": "characters/Wolhwa.md",
      "sha256": "dd7fa82da6ed3b5c980f06c5de05b74c92d888c85dd2e8359cdd815b29d6fd73",
      "bytes": 2374
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "b9d25c88967039263d2de132f453cb87d8fe5ee57815c6fd40bade55ab6533ea",
      "bytes": 31523
    }
  ],
  "estimated_tokens": 30195
}
-->

# Durable State Update — Chapter 164

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 164. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 20 concise items, `open_questions` to at most 8
items, and `temporary_decisions` to at most 8 items. Keep the serialized context
under 16384 UTF-8 bytes. Use only chapter
numbers through 164. `profile_updates` may replace one exact, uniquely occurring
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
  "chapter": 164,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 164,
    "continuity_sources": [164],
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
    "The unnamed old man is a Supreme Peak master nearing one hundred years old whose old age causes increasingly long periods of unconsciousness; he delayed its effects for roughly twenty years with two jiazi of internal energy.",
    "The old man can use Samadhi True Fire and possesses overwhelmingly potent Scorching Yang Qi, along with extraordinary physical strength.",
    "The old man is searching for an unidentified Peak master who mainly uses a sword and palm techniques; he carries a portrait and sought information from the Northern Gaoyuan's local powers.",
    "Black Sand attempted to manipulate the old man's senility through a plan to locate the sought-after master and obtain the old man's martial arts.",
    "The old man killed Black Sand with a single palm after overhearing the plan; Chinggen and Temur survived.",
    "The old man left the Northern Gaoyuan for Datong on the Shanxi–Gaoyuan border and said he would return in about a month."
  ],
  "continuity_sources": [
    163
  ],
  "open_questions": [
    "Who is the unnamed Supreme Peak master, and what is his relationship to the Peak master he seeks?",
    "Who is the unidentified Peak master being sought, and where is that person?"
  ],
  "safe_through": 163,
  "temporary_decisions": [
    "Render 삼매진화 as “Samadhi True Fire.”",
    "Render 정기신 as “essence, qi, and spirit,” 백염 as “white flames,” and 입신지경 as “a transcendent realm.”",
    "Render 어르신 as “elder” and 형님 as “big brother” when Black Sand addresses the old man, preserving the old man's rejection of both forms."
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

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 진위경    | **Jin Wikyung**    |
| 진무경    | **Jin Mukyung**    |
| 위팽     | **Wipeng**         |
| 혁무진    | **Hyuk Mujin**     |
| 청풍     | **Cheongpung**     |
| 월화     | **Wolhwa**         |
| 산서잠룡   | **Sleeping Dragon of Shanxi** | Jin Taekyung   |
| 화왕     | **Fire King**                 | Jeok Cheongang |
| 태원진가   | **Jin Family of Taiyuan**        |
| 항산검문   | **Mount Heng Sword Sect**        |
| 하오문    | **Lower District Sect**          |
| 일류     | **First Rate**    |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 절정고수                | **Peak master** / **Peak martial artist** |
| 무인     | **martial artist**                               | Default term                                          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 경지     | **realm** / **realm stage**                      | Especially power level                                |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 심법     | **cultivation technique**                        | Especially internal cultivation                       |
| 창법     | **spear technique**                              |                                                       |
| 검법     | **sword technique**                              |                                                       |
| 비급     | **martial arts manual**                          | “martial scroll” where object/context warrants        |
| 가주     | **Family Head**                              |
| 소가주    | **Lesser Family Head**                       |
| 진가심법   | **Jin Family's Cultivation Technique** |
| 시스템              | **System**                     |
| 상태창              | **Status Window**              |
| 상태               | **Status**                     |
| 레벨               | **Level**                      |
| 명성               | **Fame**                       |
| 퀘스트              | **Quest**                      |
| 보상               | **Reward**                     |
| 칭호               | **Title**                      |
| 등급               | **Grade**                      | System/UI field for quest, item, and martial-art classifications; do not use “Rank” here |
| 장비               | **Equipment**                  |
| 아이템              | **Item**                       |
| 체력               | **Stamina**                    |
| 민첩               | **Agility**                    |
| 매력               | **Charm**                      |
| 헌터      | **Hunter**            |
| 산서     | **Shanxi**             |
| 태원     | **Taiyuan**            |
| 항산     | **Mount Heng**         |
| 팔천협    | **Eight Spring Gorge** |
| 본가      | **our family / this family**                                    |
| 공자      | **Young Master**                                                |
| 곽준 | **Gwak Jun** |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 수문각주 | **Master of the Gatekeeper Pavilion** | Office Hyuk Mujin is rumored to receive. |
| 화염신장 | **Flame Divine Palm** | Jopil's deadly palm technique, noted when Taekyung compares Jopil with Mukyung. |
| 기감 | **Qi Sense** | Taekyung's sensory technique; its range reaches seventy meters in this chapter. |
| 패밀리어 | **Familiar** | System classification for the flies detected in Taekyung's home. |
| 만년한철 | **Ten-Thousand-Year Cold Iron** | Material that destroys Pung Yang's Body-Protecting Qi when the Unnamed Sword satisfies a specific condition. |
| 산서성 | **Shanxi Province** | Province containing the Lower District Sect branches. |
| 조장 | **Captain** | Hyuk Mujin's address for Taekyung as squad leader. |
| 아이템창 | **Item Window** | System window displaying an item's details. |
| 구파일방 | **Nine Sects and One Gang** | Major Murim grouping. |
| 삼도문 | **Samdo Sect** | One of the five former Five Gates sects annihilated at Eight Spring Gorge. |
| 주표 | **Zhu Bao** | Personal name of Prince Shangshan. |

## Listed compact profiles

### Cheongpung.md

# Cheongpung (청풍)

- **Safe through:** Chapter 160
- **Aliases:** None
- **Role:** Mysterious young man encountered at Honghwa Inn; an exceptionally young Peak master whose Level Jin Taekyung cannot determine through Qi Sense; the grandson and disciple of Sword Saint Mae Jonghak, who secretly descended from Huashan to seek out and defeat the Ten Dragons and Phoenixes, beginning with Jin Mukyung; he has no martial title yet, naturally opened his Governor Vessel through enlightenment two years ago, has begun teaching Jin Taekyung and Hyuk Mujin using Mae Jonghak's training method, has now used Sword Energy and the Zaha Divine Technique during his spar with Taekyung, and Prince Shangshan will only accept his autograph after he gains one
- **Personality:** Affable, dreamy, hazy, and childlike in manner, with innocent curiosity, delight in novel public attention, a deep love of martial arts, and a martial artist's competitive pride; he becomes unsettled when someone copies his martial arts
- **Voice:** Dreamy and hazy, with innocent, polite phrasing
- **Relationships:** Mae Jonghak, the Sword Saint, is his grandfather and martial instructor; Cheongpung came to Huashan at about age three or four rather than being born there, lived with Mae Jonghak at a hidden residence, and secretly left Huashan without his grandfather's knowledge to challenge the Ten Dragons and Phoenixes; Baek Museong met him ten years ago and is now traveling with the Three Plum Blossom Elites to meet him; Li Feng is his Martial Nephew within Huashan's hierarchy; calls Jin Taekyung and Hyuk Mujin Benefactors after they feed him

### Gwak Jun.md

# Gwak Jun (곽준)

- **Safe through:** Chapter 38
- **Aliases:** None revealed
- **Role:** Level 40 martial artist of the Three Paths Sect
- **Personality:** Friendly and cheerful as a cover for cold, fanatical violence; fearless, intensely confident, and eager for battle
- **Voice:** Cheerful and casual, with blunt conviction beneath his jokes
- **Relationships:** Leads martial artists of the Three Paths Sect; serves alongside Jin Taekyung’s rear guard

### Hyuk Mujin.md

# Hyuk Mujin (혁무진)

- **Safe through:** Chapter 160
- **Aliases:** None revealed
- **Role:** Level 50 First Rate martial artist from a wealthy Taiyuan textile-merchant family; Captain of the Gatekeepers at the Jin Family of Taiyuan; deputy squad leader of White Tiger Hall’s reconnaissance squad; candidate to become the next Master of the Gatekeeper Pavilion; has accepted Jin Taekyung’s invitation to train alongside Taekyung and Cheongpung in Taekyung’s private training ground
- **Personality:** Young, disciplined, persistent, and possessed of clear martial talent; suspicious of Jin Taekyung, and openly contemptuous of the family’s disgraced third son; believes loyalty and respectable conduct matter, but is also proud, hungry for glory, and an avid wuxia-novel reader who sometimes mistakes fictional Murim conventions for reality
- **Voice:** Formal and clipped when performing his duties; blunt and moralizing when addressing Taekyung
- **Relationships:** Gatekeeper under the Jin Family; deputy subordinate to Jin Taekyung in the reconnaissance squad; son of the Hyuk Family Textile Shop’s owners, with a younger sibling who removed the need for him to inherit the family business

### Jin Mukyung.md

# Jin Mukyung (진무경)

- **Safe through:** Chapter 159
- **Aliases:** Heaven Shaking Sword; Jin Family Second Young Master
- **Role:** Second son of the Jin Family of Taiyuan; twenty-three-year-old cadet at Heaven’s Gate Temple; a young Peak-level genius swordsman who won the visible exchange with Pung Yang, was then incapacitated by five concealed throwing knives, and survived the battle to recover after Taekyung's intervention; recovered enough from his Internal Injuries to return to the Jin Family of Taiyuan, though he is not yet fully recovered; four days before this chapter, he lost his duel with Cheongpung after roughly three hundred exchanges, secluded himself to train, and sharpened his Sword Energy while resolving to surpass Cheongpung and the other geniuses
- **Personality:** Reserved, terse, and easily irritated by exaggerated praise; glares coldly when Taekyung identifies him
- **Voice:** Quiet and resonant; clipped and blunt in direct speech
- **Relationships:** Taekyung’s older brother and current martial arts instructor; returned to the Jin Family after several years away; three years earlier, he flatly refused seven-year-old Zhu Bao’s request for an autograph

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 158
- **Aliases:** Sleeping Dragon of Shanxi
- **Role:** Modern-world protagonist; recently fired after seven years at his job; C-rank Hunter who defeated eight B-rank Minotaurs and killed a Level 70 B-rank Minotaur Warrior in one blow; First Rate martial artist standing before the Peak realm who now possesses forty-five years of internal energy with the Scorching Yang Qi attribute after fully absorbing the Blazing Flame Divine Pill; youngest son of the Jin Family of Taiyuan; new owner of a two-story detached house in Goyang intended for his family; Qi Sense reaches a seventy-meter radius; possesses one Temporary Strength Pill in his Inventory and has reserved it for a worst-case, life-threatening contingency; Level 64 with 2,400 Fame (+250); the Status Window showed 100 remaining stat points, 50 of which he assigned to Agility, and the Sleeping Dragon of Shanxi Title now grants all stats +15 and Fame +200; can roughly copy observed martial forms and copied the Plum Blossom Fist after three days of sparring with Cheongpung
- **Personality:** Hungry, self-aware, dryly observant, and willing to take a questionable opportunity when desperate; treats the impossible as a game until the danger becomes undeniable
- **Voice:** First-person, conversational, dryly self-mocking; uses vivid trap-and-prey imagery, game jargon, and occasional profanity
- **Relationships:** Jin Mukyung’s younger brother and current student; son of a deceased father; supports his mother and younger sibling; loves Song Song; has a strained relationship with Lee Seowol, the current Sect Leader of the Mount Heng Sword Sect, whose marriage proposal he has decided to reject

### Jin Wikyung.md

# Jin Wikyung (진위경)

- **Safe through:** Chapter 155
- **Aliases:** Junzi Sword
- **Role:** Thirty-five-year-old Lesser Family Head and future Family Head of the Jin Family of Taiyuan; directing the family's expansion across Shanxi and seeking to establish it as a great family
- **Personality:** Calm and authoritative in public; affectionate and protective toward Taekyung beneath a stern mask; accepts responsibility from his subordinates and shows immediate concern for family
- **Voice:** Restrained, formal, and commanding with subordinates; openly affectionate with Taekyung
- **Relationships:** Taekyung’s eldest brother and future Family Head; head of Wipeng; member of the Jin Family

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 158
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Wipeng.md

# Wipeng (위팽)

- **Safe through:** Chapter 161
- **Aliases:** Ghost Sword; God of Drinking
- **Role:** Jin Wikyung’s personal guard and commander of the thirty-elite pursuit team sent south under an assassin-hunt pretext
- **Personality:** Loyal, observant, teasing, and resigned to his master’s impulsive departures
- **Voice:** Weary and knowing; jokes with Jin Wikyung and uses Sound Transmission
- **Relationships:** Trusted guard and retainer of Jin Wikyung; the Human Butcher has claimed him as his personal target in the planned attack

### Wolhwa.md

# Wolhwa (월화)

- **Safe through:** Chapter 136
- **Aliases:** Eun Sowol (은소월); Wolhwa is the name used at Honghwaru
- **Role:** Shanxi’s foremost information merchant and Level 50 martial artist; Branch Leader of the Lower District Sect’s Shanxi branch with authority to mobilize more than thirty Shanxi branches; formerly posing as a high-ranking courtesan at Honghwaru, a pleasure house in central Taiyuan
- **Personality:** Striking, composed, observant, direct, quietly amused, and capable of ruthless, decisive violence when extracting information; comfortable teasing Taekyung while conducting serious information and negotiation work
- **Voice:** Polite and lightly playful; addresses Taekyung as Young Master Jin and delivers embarrassing observations without raising her voice
- **Relationships:** Knows Taekyung as a Honghwaru regular and the youngest son of the Jin Family; says she likes him, though her sincerity is unclear

## Korean source

```text
＃164화



상태창



[Lv.71 진태경]

직업 : 절정 고수

명성 : 2400 (+250)

칭호 : 5개 (칭호 효과 적용 중)

- 귀환자 (모든 능력치 +10)

- 산서잠룡 (모든 능력치 +15, 명성 +200)

- 명가의 자제 (모든 능력치 +5, 명성 +50)

- 승부사 (일대일 전투 시 전투 관련 능력치 +10%)

- 중급 수련자 (수련 속도 +20%)

근력 : 255 (+30)체력 : 207 (+30)

민첩 : 250 (+30)지력 : 40 (+30)

매력 : 40 (+30)공력 : 45년

맷집 : 200 (+30)

잔여 포인트 : 70

- 잔여 포인트를 분배하십시오.





하루에 열 번도 넘게 보는 상태창이지만 볼 때마다 입이 찢어진다.

절정 고수, 저 네 글자에 이렇게 행복질 수 있다니.

‘나보고 고수래. 절정 고수.’

불과 몇 시간 전만 하더라도 직업 칸에 적혀 있던 것은 [일류 무인]이었다. 하지만 이제는 절정 고수다. 무인이 아니라 고수.

시스템도 인정하는 진짜 고수가 된 것이다.

‘레벨도 벌써 71이 넘었고.’

보상은 끝내줬다.

일곱 번의 레벨 업, 진가심법과 기감의 경지가 한 단계씩 올랐고…….

‘돈 주고도 못 구할 물건도 얻었지.’

인벤토리 오픈.

머릿속으로 명령어를 입력하자 익숙한 시스템 알림과 함께 반투명한 홀로그램 창이 떴다.

지금까지 무림에서 모아 온 온갖 잡동사니가 가득했지만 내 시선은 올곧게 한곳에 고정되었다.

‘만년한철 소환.’

슈욱.

순간 묵직한 구체(球體) 하나가 허공에서 툭 튀어나왔다. 크기는 볼링공 정도에, 다듬어지지 않은 표면은 울퉁불퉁 제멋대로 튀어나와 있다.

얼핏 보면 별 쓸모없는 쇳덩어리나 바위 같지만, 조금만 주의를 기울인다면 이 물건의 진짜 가치를 알아챌 수 있다.

‘아이템 확인.’

띠링.



아이템창



[가공되지 않은 만년한철]

종류 : 재료

등급 : 초절정

제한 : 명장(名匠)

설명 : 만 년 묵은 한철은 천하에 현존하는 어떤 광물보다 단단하고 예리하며, 또 희귀합니다. 오직 명장의 반열에 오른 장인만이 이 귀물을 다룰 수 있을 것입니다.





“크으, 이게 진짜지.”

개인적으로 레벨 업보다 만년한철을 얻은 것이 더 기쁘다. 나도 헌터고, 무인이니까. 이 바닥에 있는 사람이라면 누구나 장비에 대한 로망이 있다.

지금까지는 그 로망을 현실로 만들 여건이 안 됐을 뿐이다.

‘현실에서는 돈이 없었고, 무림에서는 쓸 만한 창이 없었지.’

태원진가의 뿌리는 창법이 아니라 검법이다.

공급은 수요를 따라가는 법. 하급 무인들부터 가문의 수뇌부들도 검수들이 대부분이다 보니 무공도, 병기고에 보유한 무기의 품질도 창에 비해 검이 훨씬 앞섰다.

그나마 진위경이 신경 써 주지 않았다면 싸구려 목창이나 죽창을 들고 싸워야 했을지도 모른다.

만년한철로 만들어진 [이름 없는 검]을 두고 철창을 휘두를 때마다 얼마나 속이 쓰렸던가?

‘하지만 그런 설움도 이젠 끝이다.’

만년한철. 천하제일의 광물을 얻었으니 나만의 애병(愛兵)을 만들 수 있다. 물론 그러기 위해서는 전제 조건이 필요하다.

이번에 받은 퀘스트는 그와 연관이 있었다.

‘퀘스트 확인.’

띠링.



퀘스트



[장인을 찾아라]

만년한철을 제련하기 위해서는 엄청난 경험과 실력이 뒷받침되어야 합니다. 극히 뛰어난 장인만이 이 귀물의 모든 힘을 끌어낼 수 있을 것입니다.



등급 : 절정

제한 : 진태경

임무 : 명장에게 병기 제작 의뢰(미완료)

보상 : ???

실패 : ???





나는 흐뭇하게 웃으며 퀘스트 창을 껐다.

‘그렇지. 만년한철씩이나 되는 물건을 아무한테나 맡길 수는 없지.’

굳이 퀘스트가 아니더라도 내가 직접 알아봤을 일이었다.

명검이 고수의 손에 들려야만 비로소 빛을 발하듯, 만년한철 같은 귀한 재료도 마찬가지다.

비록 퀘스트 등급은 절정이지만 임무 자체도 딱히 어렵게 느껴지지 않았다.

‘찾는 거야 금방이지, 뭐.’

이 넓은 땅덩어리에 명장이 한 명 없겠나.

태원진가의 지부는 산서 전역에 퍼져 있다. 진위경에게 부탁해서 연락을 돌리면 곧 위치를 알 수 있을 것이다.

‘정 안 되면 하오문에 부탁하는 방법도 있고.’

심지어 내게는 월화라는 든든한 인맥이 있다. 산서성 곳곳에 눈과 귀를 심어 둔 그녀에게 이 정도는 누워서 떡 먹기나 다름없다.

‘무슨 수를 써서라도 이 퀘스트는 깨고 간다.’

무림에서의 한 달은 현대로 치면 고작 세 시간.

아직 시간은 넉넉하다.

“으헤헤, 만년한철로 창을 만든다. 만년한철로 창을…….”

입이 찢어져라 웃고 있던 그때.

쾅!

굉음과 함께 문이 터져 나갔다. 그리고 번개처럼 들이닥친 한 사람이 나를 향해 두 팔을 벌렸다.

“막내야!”

응. 당신일 줄 알았어.

나는 한숨을 푹 내쉬며 진위경에게 물었다.

“무슨 일이세요?”

“무슨 일이냐니! 네가 벽을 깼다는 경사스러운 소식을 듣고 한달음에 달려왔다!”

“……그건 또 어떻게 아시고.”

고작해야 한두 시간 전의 일인데 정보의 속도가 장난이 아니다. 이 인간 설마 나한테 패밀리어라도 붙여 놨나?

당황해하며 그를 보는데, 순간 뻥 뚫린 문 앞에서 흐뭇하게 웃고 있는 혁무진이 눈에 들어왔다. 녀석은 코밑을 쓱 문지르며 말했다.

“이런 경사는 최측근이 가장 먼저 전해야 하는 것 아니겠습니까.”

“…….”

패밀리어가 아니라 혁밀리어였구나.

저 자식 분명히 내 이름 팔아서 진위경에게 점수 좀 땄을 거다.

“흐어엉! 우리 막내가 벽을 깨다니! 절정의 경지에 오르다니!”

아니나 다를까, 혁무진이 잽싸게 끼어들었다.

“소가주님. 제가 호법을 섰습니다!”

“고맙네, 정말 고마워. 자네의 공이 매우 크네!”

“아닙니다. 오른팔로서 마땅히 해야 할 일을 한 것뿐, 단 한 치의 사심도 없었습니다. 한데 아직 수문각주 자리가 공석이던데…….”

“무조건 자네일세! 아니, 자네가 태원진가의 차기 가주일세!”

“허, 허억! 그것이 정말입니까?”

“…….”

당연히 아니지, 병신아.

호법 좀 섰다고 가주 시켜 주는 게 말이나 되니? 심지어 저 자식이 한 거라고는 코골이밖에 없다.

하지만 기쁨과 권력에 눈이 먼 두 사람은 이미 제정신이 아니었다.

“혁무진, 혁무진이라고 했지?”

“맞습니다, 소가주님!”

“우리 무진이 하고 싶은 거 다 해! 태원진가 가주 해! 구파일방 뿌셔! 천하 뿌셔!”

“뿌셔!”

“……뭘 뿌셔. 미친놈들아.”

태원진가의 앞날이 어둡다.



* * *



한바탕 소란이 지나간 후, 간신히 마음을 진정시킨 진위경이 촉촉하게 젖은 눈동자로 나를 바라봤다.

“형은 네가 자랑스럽구나.”

“저도 조장이 자랑스럽습니다. 하지만 제가 호법을 서지 않았다면…….”

“무진이는 입 닥치자. 뚝배기 깨지고 싶지 않으면. 참고로 뚝배기는 머리란다.”

“옙.”

어느새 이마에 혹이 솟은 혁무진이 냉큼 대답했다. 역시 맞아야 말을 듣는 녀석이다.

“못난 형이 제대로 챙겨 주지도 못했는데 혼자서 이렇게, 크흐흑.”

“…….”

인간 흉기의 감수성 보소.

진위경이 이럴 때마다 이 세계에 SNS가 없다는 사실에 감사하게 된다. 만약 있었다면 아웃스타그램에 태원진가 식솔들을 전부 태그한 게시글이 올라왔을 테니까.

눈물 셀카와 해시태그는 덤이다.



#태원진가 #못난형 #우리막내도절정고수 #오늘도힘내자



월화 : 어머! 진 공자가? 축하해요!

청풍 : 와, 저 좋아요 처음 눌러 봐요!

위팽 : 거짓말 치지 마십쇼.

혁무진 : 제가 호법을 섰습니다.

진무경 : 이게 나라냐.

주표 : 서명 좀.



수많은 산서성 샐럽들의 반응을 상상하자 눈앞이 아찔하다.

황급히 끔찍한 생각을 털어 낸 나는 진위경을 다독였다.

“울지 좀 마세요. 나이가 몇 갠데.”

“크흐윽. 그 철부지 어린 막내가 어찌 이리 훌륭히 장성했을꼬.”

감격과 대견함이 섞인 눈빛으로 나를 바라보던 진위경이 소매로 눈가를 훔쳤다.

“아니다, 내 이럴 게 아니라 지금 당장…….”

“혹시 지난번처럼 엄청 큰 천에다가 제가 절정 고수 됐다고 써 놓으려는 건 아니죠?”

“헛.”

“…….”

내 이럴 줄 알았지. 지금까지의 진위경을 보건대 이대로 넘어갈 위인이 아니다. 이참에 확실히 못 박아야 한다.

“그런 거 하지 마세요. 쪽팔리니까.”

“쪽팔리다? 그게 무슨 뜻이냐?”

“창피하다고요.”

진위경이 충격받은 얼굴로 물었다.

“형이, 이 형이 창피한 게냐?”

“아니, 그게 아니라…….”

미치겠네.

그런데 내가 미처 대답하기도 전에 조용히 찌그러져 있던 혁무진이 영문을 모르겠단 얼굴로 불쑥 끼어들었다.

“엥? 조장 원래 관심받는 거 좋아하시잖아요?”

“야, 내가 언제!”

“아니에요? 제 기억으로는 엄청 좋아하셨던 것 같은데. 항산검문에서 돌아올 때도 맨 앞에서 손 엄청 흔드시고.”

“……크흠.”

저 녀석이 없는 말 지어내는 거면 한 대 쥐어박기라도 했을 텐데, 사실이라 뭐라 할 말이 없다.

나는 슬며시 혁무진의 시선을 피하며 대꾸했다.

“그때는 인마, 사정이 있었어.”

“무슨 사정이요?”

“그런 게 있어. 넌 몰라도 돼.”

“헐, 또 저러시네.”

뭐라 구시렁거리는 혁무진을 무시하고 진위경에게로 시선을 돌렸다.

“아무튼 그런 일은 안 하는 걸로. 관심은 지금으로도 충분합니다.”

“으음. 네 뜻이 정 그렇다면야.”

진위경은 아쉬움을 감추지 못했지만 내가 워낙 단호하게 말하니 마지못해 고개를 끄덕였다. 이걸로 나도 한숨 돌렸다.

‘절정 고수 됐다고 광고 때려 봤자 뭐하냐. 날파리만 잔뜩 꼬이지.’

한때는 명성에 목숨 걸었던 적이 있었지만 이제는 아니다.

아니, 오히려 불길하다.

‘어째 명성이 높아질수록 강한 놈들만 꼬이는 기분이란 말이지.’

내 인생 모토가 가늘고 길게다. 물론 굵고 길게 간다면 더할 나위 없겠지만, 그런 사람들치고 인생이 평탄한 경우가 거의 없더라.

그리고 매번 생사가 오가는 싸움을 하다 보니 심신이 지친 것도 큰 이유였다.

‘최소한의 대비 정도는 해 둬야지.’

만년한철로 끝내주는 창도 한 자루 만들고, 무공도 가다듬을 생각이었다. 그러기 위해서는 진위경의 도움이 꼭 필요하다.

“부탁 하나만 들어주실 수 있으세요?”

마다할 진위경이 아니다. 그가 자신 있게 고개를 끄덕였다.

“뭐든지 말만 하거라.”

“정보가 필요해요.”

“정보? 정확히 무엇에 관한 것이냐?”

“총 두 가진데, 첫 번째는 만년한철도 주무를 수 있을 만큼 대단한 명장의 소재. 두 번째는 화왕(火王)에 관한 소식이요.”

“첫 번째는 그렇다 치고, 화왕이라면…… 설마 ‘그것’을 익힐 생각이냐?”

그것. 화염신장을 일컬음이다.

진위경에게 직접 말한 적은 없지만 이미 그는 모든 것을 알고 있었다.

하긴, 화염신장은 화왕의 독문무공이고 잘못 건드렸다가는 가문 전체가 위험해지는 폭탄이나 다름없다. 진무경이 소가주인 그에게 진작 말했을 거라는 사실쯤은 충분히 예상했던 바다.

“태경아.”

우려 섞인 목소리에 나는 손을 내저었다.

“당장 익힐 생각은 없어요. 다만 최소한 화왕의 생사를 확인한 후에 결정하고 싶은 거예요.”

“음.”

잠시 침묵하던 진위경이 입을 열었다.

“하나만 약속해 주겠느냐? 그 전에 반드시 나와 한번 상의하는 것으로.”

“예.”

“그럼 되었다.”

시원하게 고개를 끄덕인 진위경이 자리에서 일어났다.

“화왕에 관한 것은 시일이 걸리겠지만 첫 번째 정보는 지금 당장이라도 알려 줄 수 있다.”

벌써? 역시 태원진가라고 해야 할지. 어지간한 것은 전부 파악하고 있는 모양이다.

생각보다 빠른 진행 속도에, 당장에라도 찾아가고 싶어서 엉덩이가 다 근질거렸다.

“가까이에 있는 사람인가 봐요?”

“그래. 아무도 모르게 은거하고 계시더구나. 본가에서도 그분의 존재를 안 지 얼마 되지 않았다.”

“혹시 실력은……?”

“내 장담컨대 천하를 바닥까지 훑어도 열 손가락 안에 들 것이다.”

진위경이 저렇게 자신 있게 말할 정도라면 실력 하나는 확실한 모양이다.

만년한철을 다룰 수 있을 만한 명장. 예상보다 훨씬 빨리 찾았다.

“내 돌아가서 다시 한번 확인하고 연통을 넣어 주마. 그럼 이만 쉬거라. 허허, 벽을 깨다니. 약관에 절정이라니!”

진위경이 싱글벙글 웃으며 사라지자 혁무진이 궁금해 죽겠다는 얼굴로 입을 열었다.

“뭡니까?”

“응? 뭐가?”

“화왕과 관련된 ‘그것’이 도대체 뭐냐고요?”

“아, 그거? 화염신장.”

“화염신장이요?”

어리둥절한 표정이다. 하긴, 진무경처럼 무공 박사도 아니니 모르는 것도 당연했다.

“응. 화염신장. 화왕의 독문무공이지.”

“……예?”

“뭘 그렇게 놀라?”

“도, 도대체 그걸 어떻게 얻으신 거예요? 아니, 그 전에 이런 중대한 사실을 저한테 말씀해 주셔도 되는 겁니까?”

경악과 당황이 뒤섞인 얼굴로 묻는 녀석에게, 나는 친절하게 대답해 주었다.

“응. 넌 직접 보기까지 했잖아.”

“예?”

“뭐가 예?야. 너 화염신장 비급 본 적 있어. 아니지. 보는 걸 넘어서 네가 가질 뻔했었지.”

“제가요?”

“어. 그때 기억 안 나? 팔천협 전투 있기 전에 우리 후발대로 남아 있었잖아. 곽준인가 하는 삼도문 애들이랑 같이.”

곰곰이 생각에 잠겨 있던 혁무진의 입이 천천히 벌어진다.

“설마 그때 그……?”

“그거 맞아. 너 가지라고 했더니 거절했던 그거.”

“……!”

“휴우, 그때 줬으면 큰일 날 뻔했네.”

혁무진의 얼굴이 참담하게 일그러졌다.
```

## Final English reading copy

```markdown
# Chapter 164

> **System**
>
> **Status Window**
>
> Lv. 71 Jin Taekyung
>
> **Class:** Peak Master
>
> **Fame:** 2,400 (+250)
>
> **Titles:** 5 (Title effects active)
>
> - Returnee (All stats +10)
>
> - Sleeping Dragon of Shanxi (All stats +15, Fame +200)
>
> - Scion of a Prestigious Family (All stats +5, Fame +50)
>
> - Gambler (Combat-related stats +10% in one-on-one combat)
>
> - Intermediate Trainee (Training speed +20%)
>
> **Strength:** 255 (+30)  
> **Stamina:** 207 (+30)
>
> **Agility:** 250 (+30)  
> **Intelligence:** 40 (+30)
>
> **Charm:** 40 (+30)  
> **Internal Energy:** 45 years
>
> **Toughness:** 200 (+30)
>
> **Remaining Points:** 70
>
> - Distribute your remaining points.

It was a Status Window I looked at more than ten times a day, but my mouth still split into a grin every time I saw it.

Who knew the four characters meaning “Peak Master” could make me this happy?

*The System calls me a master. A Peak Master.*

Only a few hours ago, the Class field had read [First Rate Martial Artist]. But now I was a Peak Master. Not a martial artist, but a master.

I had become a genuine master, recognized even by the System.

*I’m already Level 71, too.*

The rewards had been incredible.

Seven level-ups, a one-stage increase in both the Jin Family’s Cultivation Technique and Qi Sense, and…

*I even got something you couldn’t buy with money.*

Open Inventory.

As soon as I entered the command in my mind, a familiar System notification chimed, and a translucent holographic window appeared.

My Inventory was packed with all kinds of junk I had collected in the Murim, but my eyes fixed squarely on one item.

*Summon Ten-Thousand-Year Cold Iron.*

Whoosh.

A heavy sphere suddenly popped into existence in midair. It was about the size of a bowling ball, its unpolished surface uneven and jagged, bulging out in every direction.

At first glance, it looked like a useless lump of metal or a rock. But with even a little attention, one could recognize its true value.

*Inspect Item.*

Ding.



> **System**
>
> **Item Window**
>
> **Unprocessed Ten-Thousand-Year Cold Iron**
>
> **Type:** Material
>
> **Grade:** Supreme Peak
>
> **Restriction:** Master Artisan
>
> **Description:** Ten-thousand-year-old cold iron is harder, sharper, and rarer than any mineral currently existing in the world. Only a craftsman who has reached the ranks of a master artisan will be able to handle this precious material.

“Now, this is the real deal.”

Personally, I was happier about obtaining the Ten-Thousand-Year Cold Iron than I was about leveling up. I was a Hunter, and I was a martial artist. Anyone in this line of work had dreams about their equipment.

I simply hadn’t had the means to turn those dreams into reality.

*I had no money in the real world, and in the Murim, I didn’t have a decent spear.*

The Jin Family of Taiyuan’s roots lay in sword techniques, not spear techniques.

Supply followed demand. From the lowest-ranking martial artists to the heads of the family, most of them were sword users. As a result, both their martial arts and the quality of the weapons in the armory were far superior for swords than for spears.

If Jin Wikyung hadn’t looked out for me, I might have had to fight with a cheap wooden spear or bamboo spear.

How many times had my guts twisted whenever I swung an iron spear while leaving the [Unnamed Sword], made from Ten-Thousand-Year Cold Iron, at my side?

*But that humiliation is over now.*

I had obtained the finest mineral in the world. I could have a beloved weapon of my own made.

Of course, there was one prerequisite.

The Quest I had received this time was related to it.

*Inspect Quest.*

Ding.



> **System**
>
> **Quest**
>
> **Find the Master Artisan**
>
> Forging Ten-Thousand-Year Cold Iron requires tremendous experience and skill. Only an exceptionally skilled artisan will be able to draw out all the power of this precious material.
>
> **Grade:** Peak
>
> **Restriction:** Jin Taekyung
>
> **Mission:** Commission a Master Artisan to make a weapon (Incomplete)
>
> **Reward:** ???
>
> **Failure:** ???

I smiled contentedly and closed the Quest Window.

*Of course. I can’t entrust something as valuable as Ten-Thousand-Year Cold Iron to just anyone.*

Even without the Quest, I would have looked into it myself.

Just as a famed sword only truly revealed its brilliance in the hands of a master, precious materials like Ten-Thousand-Year Cold Iron were no different.

Although the Quest was graded Peak, the mission itself didn’t seem particularly difficult.

*Finding someone shouldn’t take long.*

Surely there had to be at least one master artisan in this enormous land.

The Jin Family of Taiyuan had branches spread throughout Shanxi. If I asked Jin Wikyung to send out word, we would soon know where to find one.

*And if that doesn’t work, I can ask the Lower District Sect.*

I even had a powerful connection in Wolhwa. With eyes and ears planted throughout Shanxi Province, something like this would be a piece of cake for her.

*Whatever it takes, I’m completing this Quest before I leave.*

A month in the Murim was only three hours in the modern world.

I still had plenty of time.

“Hehehe. A spear made from Ten-Thousand-Year Cold Iron. A spear made from Ten-Thousand-Year Cold Iron…”

Just as I was grinning from ear to ear—

Bang!

The door burst apart with a deafening roar. A person rushed in like lightning and threw both arms wide toward me.

“Youngest!”

Yep. I knew it would be you.

I let out a deep sigh and asked Jin Wikyung,

“What’s going on?”

“What do you mean, what’s going on? I heard the wonderful news that you broke through the wall and rushed here at once!”

“…How did you hear about that?”

It had only happened an hour or two ago, but the speed of the information network was no joke. Had this guy attached a Familiar to me or something?

As I stared at him in bewilderment, I suddenly noticed Hyuk Mujin standing in front of the blown-open doorway, smiling proudly. He casually rubbed beneath his nose and said,

“Shouldn’t such wonderful news be delivered first by the closest aide?”

“…”

Not a Familiar. It was a Hyuk-miliar.

That bastard had definitely used my name to score some points with Jin Wikyung.

“Our youngest broke through the wall! He reached the Peak realm!”

As expected, Hyuk Mujin quickly cut in.

“Lesser Family Head, I served as his guard!”

“Thank you. Truly, thank you. Your contribution was enormous!”

“Not at all. As your right arm, I merely did what I was supposed to do. I had not a shred of selfish intent. However, I noticed that the position of Master of the Gatekeeper Pavilion is still vacant…”

“It’s yours without question! No, you’ll be the next Family Head of the Jin Family of Taiyuan!”

“W-Whaaaat? Is that really true?”

“…”

Of course it wasn’t, you dumbass.

Did it make any sense to appoint someone Family Head just because he had stood guard? And all that bastard had actually done was snore.

But the two men, blinded by joy and power, were already out of their minds.

“Hyuk Mujin. You said your name was Hyuk Mujin, right?”

“Yes, Lesser Family Head!”

“Our Mujin can do whatever he wants! Become Family Head! Smash the Nine Sects and One Gang! Smash the world!”

“Smash!”

“…What are you smashing, you lunatics?”

The future of the Jin Family of Taiyuan looked bleak.



* * *

After the commotion finally passed, Jin Wikyung managed to calm himself and looked at me with moist eyes.

“Your brother is proud of you.”

“I’m proud of you too, Captain. But if I hadn’t served as your guard…”

“Mujin, let’s keep quiet unless you want your pot cracked. And by ‘pot,’ I mean your head.”

“Yes, sir.”

Hyuk Mujin, now sporting a lump on his forehead, answered at once. As expected, he only listened after getting hit.

“Your useless older brother couldn’t even look after you properly, and yet you grew up this well all on your own. Sniff.”

“…”

Look at the sensitivity on this human weapon.

Whenever Jin Wikyung acted like this, I was grateful that this world had no social media. If it did, a post tagging every member of the Jin Family of Taiyuan would have gone up on Outstagram.

A teary-eyed selfie and hashtags would have been included for free.



#JinFamilyofTaiyuan #UselessOlderBrother #OurYoungestIsAPeakMaster #KeepYourChinUpToday



Wolhwa: Oh my! Young Master Jin? Congratulations!

Cheongpung: Wow, this is my first time pressing Like!

Wipeng: Don’t lie.

Hyuk Mujin: I served as his guard.

Jin Mukyung: Is this a country?

Zhu Bao: An autograph, please.



The thought of countless Shanxi Province celebrities reacting like that made my vision swim.

I hurriedly pushed the horrifying image from my mind and comforted Jin Wikyung.

“Please stop crying. How old are you?”

“Sniff. How did that immature little youngest grow up to be such a fine man?”

Jin Wikyung gazed at me with a mixture of emotion and pride, then wiped the corners of his eyes with his sleeve.

“No, this won’t do. I need to go right now and…”

“You’re not planning to write ‘Jin Taekyung has become a Peak Master’ on a gigantic banner like last time, are you?”

“Huh.”

“…”

I knew it. Judging by everything Jin Wikyung had done until now, there was no way he would let this opportunity pass. I had to make myself perfectly clear.

“Don’t do anything like that. It’s cringe.”

“Cringe? What does that mean?”

“It means embarrassing.”

Jin Wikyung asked with a shocked expression,

“Are you saying you’re embarrassed by me? By your own brother?”

“No, that’s not what I…”

This was driving me insane.

Before I could answer, Hyuk Mujin, who had been sitting there quietly with his shoulders hunched, suddenly cut in with a baffled expression.

“Huh? Captain, you usually like getting attention.”

“When have I ever?”

“You don’t? If I remember correctly, you seemed to like it a lot. When we returned from the Mount Heng Sword Sect, you waved your hand like crazy from the very front.”

“…Ahem.”

If he had been making that up, I would have punched him. But it was true, so I had nothing to say.

I quietly avoided Hyuk Mujin’s gaze and replied,

“That was different. I had my reasons.”

“What reasons?”

“There were reasons. You don’t need to know.”

“Wow, there he goes again.”

I ignored Hyuk Mujin’s muttering and turned my gaze back to Jin Wikyung.

“Anyway, we’re not doing anything like that. The attention I’m getting now is more than enough.”

“Hm. If that’s truly what you want…”

Jin Wikyung couldn’t hide his disappointment, but I was so firm that he reluctantly nodded. That let me breathe a sigh of relief.

*What’s the point of advertising that I became a Peak Master? I’ll only attract a whole swarm of flies.*

There had been a time when I was willing to risk my life for Fame, but not anymore.

No, if anything, it felt ominous.

*Why does it feel like the higher my Fame gets, the stronger the people it attracts become?*

My life motto was to live thin and long. Of course, living thick and long would be even better, but people who lived that way rarely had peaceful lives.

And after constantly fighting battles where my life hung in the balance, I was exhausted in both body and mind.

*I need to make at least the bare minimum of preparations.*

I planned to make one hell of a spear from the Ten-Thousand-Year Cold Iron and hone my martial arts. To do that, I absolutely needed Jin Wikyung’s help.

“Could you do me one favor?”

Jin Wikyung was not the sort of person to refuse. He confidently nodded.

“Say the word.”

“I need information.”

“Information? About what, exactly?”

“Two things. First, the whereabouts of a master artisan skilled enough to work with Ten-Thousand-Year Cold Iron. Second, news about the Fire King.”

“The first is understandable, but the Fire King… Surely you aren’t thinking of learning *that*?”

*That* referred to the Flame Divine Palm.

I had never told Jin Wikyung directly, but he already knew everything.

It made sense. The Flame Divine Palm was the Fire King’s signature martial art, and touching it carelessly was no different from holding a bomb that could put the entire family at risk. I had already guessed that Jin Mukyung would have told his Lesser Family Head brother about it long ago.

“Taekyung.”

At the concern in his voice, I waved my hand.

“I’m not planning to learn it right away. I just want to confirm whether the Fire King is alive or dead before I decide.”

“Hmm.”

After a brief silence, Jin Wikyung spoke.

“Will you promise me one thing? Before you do that, you’ll consult with me first.”

“Yes.”

“Then that’s settled.”

Jin Wikyung nodded decisively and rose from his seat.

“Information about the Fire King may take some time, but I can tell you about the first matter right now.”

Already? That was the Jin Family of Taiyuan for you. They seemed to have a handle on almost everything.

The progress was much faster than I had expected. My butt practically itched with impatience to go find the man immediately.

“He must be someone nearby?”

“Yes. He has apparently been living in seclusion without anyone knowing. Even our family only learned of his existence recently.”

“Could you tell me about his skill?”

“I guarantee that even if you searched the entire world from top to bottom, he would be among the top ten.”

If Jin Wikyung could speak that confidently, then the man’s skill was beyond question.

A master artisan capable of handling Ten-Thousand-Year Cold Iron. I had found him much faster than expected.

“I’ll go back and confirm it once more, then send word. Now, get some rest. Ho ho, you broke through the wall. A Peak Master at twenty!”

Jin Wikyung disappeared with a broad grin. Hyuk Mujin opened his mouth, looking as though his curiosity might kill him.

“What is it?”

“Hm? What is what?”

“What on earth is that ‘thing’ related to the Fire King?”

“Oh, that? The Flame Divine Palm.”

“The Flame Divine Palm?”

He looked utterly bewildered. Of course. He wasn’t a martial arts expert like Jin Mukyung, so it was only natural that he didn’t know.

“Yeah. The Flame Divine Palm. It’s the Fire King’s signature martial art.”

“…What?”

“Why are you so surprised?”

“H-How did you get it? No, before that, is it really all right to tell me something this important?”

I answered him kindly despite the expression of shock and confusion on his face.

“Yeah. You even saw it yourself.”

“…What?”

“What do you mean, ‘what’? You’ve seen the Flame Divine Palm martial arts manual before. No, you didn’t just see it—you almost ended up owning it.”

“I did?”

“Yeah. Don’t you remember? Before the battle at Eight Spring Gorge, we stayed behind as the rear party. With those Samdo Sect guys—Gwak Jun or whatever his name was, and the others.”

Hyuk Mujin sank into thought, and his mouth slowly fell open.

“Don’t tell me it was that thing back then…”

“That’s the one. The thing you refused when I told you to take it.”

“…”

“Whew. Good thing I didn’t give it to you back then.”

Hyuk Mujin’s face twisted miserably.
```
