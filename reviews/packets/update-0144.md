<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0144.txt",
      "sha256": "0d55287d3914320f22ed3a8236148efefdc42aae415f406a3401717343981d58",
      "bytes": 13851
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "bee9ae73e1a141c1145e8f4dee688c19773741ea887382f79f6a06f0ecc776ad",
      "bytes": 3800
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "c4e5c39b3b79dcabd3b0511c68a665aea9c16c22d9222dec686b5f2bf3ce400b",
      "bytes": 30599
    },
    {
      "path": "characters/Cheongpung.md",
      "sha256": "45c5d5a27cf4399a4cabf35f6cfa7c6d1fd1d33eea581fcc635c426cf12701e3",
      "bytes": 934
    },
    {
      "path": "characters/Hong Jin.md",
      "sha256": "9515e16617929fc1ed065120dba351f4944b61b363ae644ed6da51f12ae680ce",
      "bytes": 809
    },
    {
      "path": "characters/Jin Mukyung.md",
      "sha256": "e90390bac103b86e36a43f9cce8cdf8af81ebe3b44c0cc874d4b89badfa6fed6",
      "bytes": 1511
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "1da8657da4207b811268144b5497b70825fd6559e39081e943aa8f5c0e0f8433",
      "bytes": 24583
    },
    {
      "path": "characters/Jin Wikyung.md",
      "sha256": "2f4e04480a536fe239292b5dfbbcd73b75c85c37eb1179133a4cf861231603f2",
      "bytes": 8154
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "a6d5fa38f487c5daf72774b6f79896f62d261878bb12f0cd54f2630fa97ebd62",
      "bytes": 622
    },
    {
      "path": "characters/Jopil.md",
      "sha256": "f69b3a46b5583688813904892f7bc63af31e943be58f909dade6aef1ae8ad848",
      "bytes": 2893
    },
    {
      "path": "characters/Li Feng.md",
      "sha256": "86d3d7c65981a6d09a29a566fbea5e2d0451a53ea3629f2fcbe2d0f6b8a3daf8",
      "bytes": 888
    },
    {
      "path": "characters/Mae Jonghak.md",
      "sha256": "490550e67ff1f6ac30f98d0f50d576a42ed7904c045cf13b6e192781e9722cb7",
      "bytes": 468
    },
    {
      "path": "characters/Prince Shangshan.md",
      "sha256": "c4fdadbca4ad621544594e36d309d583af15f29ccb02a7ef2f24c3f50ea1a88c",
      "bytes": 701
    },
    {
      "path": "characters/Pung Yang.md",
      "sha256": "263d8d6f9410e71788849e9515e80f7e0eb95d33a72052d1f432a6462812ab52",
      "bytes": 1356
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "df86d4b49c63a4a69838b16eeb632b9dc43ff51f923caa62efca8f9b1080161e",
      "bytes": 26068
    }
  ],
  "estimated_tokens": 26382
}
-->

# Durable State Update — Chapter 144

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 144. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 20 concise items, `open_questions` to at most 8
items, and `temporary_decisions` to at most 8 items. Keep the serialized context
under 16384 UTF-8 bytes. Use only chapter
numbers through 144. `profile_updates` may replace one exact, uniquely occurring
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
  "chapter": 144,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 144,
    "continuity_sources": [144],
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
    "Taekyung encouraged Cheongpung to insult the Zhongnan disciples, and Cheongpung swore for the first time.",
    "Hong Jin and Li Feng escort Taekyung and Cheongpung to meet Prince Shangshan after the luncheon.",
    "Li Feng commands the military's respect, while Hong Jin holds influence over civil officials and servants through fear.",
    "Cheongpung wants to join the royal guard because he admires its black armor and agrees to call Li Feng Martial Nephew in exchange for royal-guard armor and weapons.",
    "Prince Shangshan is ten years old, has trained in martial arts daily for three years, is an exceptionally skilled young swordsman, and is personally named Zhu Bao.",
    "Zhu Bao recognizes Taekyung as the Sleeping Dragon of Shanxi and asks him for an autograph."
  ],
  "continuity_sources": [
    142,
    143
  ],
  "open_questions": [
    "What is Cheongpung's exact parentage, and what did Mae Jonghak mean by saying a crane delivered him?",
    "Why did Mae Jonghak remain hidden at Huashan despite the sect eventually finding his residence?",
    "What are the names and individual identities of the other two members of the Three Hands of Zhongnan?",
    "What is the full title of the wuxia novel beginning with 군림…… that Taekyung read through volume thirty-four?"
  ],
  "safe_through": 143,
  "temporary_decisions": [
    "Render 전하 as “His Highness” as the formal royal address and 왕 as “king” when Cheongpung uses it literally.",
    "Render 초일류 as “advanced First Rate” and 군문 as “military” when describing an affiliation.",
    "Render 풍운검군 as “Wind-and-Cloud Sword Lord” and 오촌 당숙 as “father's cousin.”",
    "Render 태을미리장 as “Taeeul Miri Palm.”",
    "Render 후배님 and 선배님 as “Junior” and “Senior” in the Gong Ilhyuk exchange.",
    "Render 태사부 as “Grandmaster” and 사숙 as “Martial Uncle” in the Huashan context.",
    "Render 자하신공 as “Zaha Divine Technique.”",
    "Render 근위대 as “royal guard,” 근위대 갑옷 세트 as “Royal Guard Armor Set,” and 주표 as “Zhu Bao.”"
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

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 진위경    | **Jin Wikyung**    |
| 진무경    | **Jin Mukyung**    |
| 진백양    | **Jin Baekyang**   |
| 조필     | **Jopil**          |
| 매종학    | **Mae Jonghak**    |
| 청풍     | **Cheongpung**     |
| 산서잠룡   | **Sleeping Dragon of Shanxi** | Jin Taekyung   |
| 화양검    | **Blade of Flowers**          | Jin Baekyang   |
| 검성     | **Sword Saint**               | Mae Jonghak    |
| 태원진가   | **Jin Family of Taiyuan**        |
| 화산파    | **Huashan**                      |
| 종남파    | **Zhongnan Sect**                |
| 산서오문   | **Five Gates of Shanxi**         |
| 일류     | **First Rate**    |
| 절정     | **Peak**          |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 영약     | **elixir**                                       |                                                       |
| 검기     | **Sword Energy**                                 | When functioning as projected weapon qi               |
| 후기지수   | **young prodigy** / **rising martial artist**    | Contextual, not a title                               |
| 중원     | **Central Plains**                               |                                                       |
| 가주     | **Family Head**                              |
| 소가주    | **Lesser Family Head**                       |
| 문주     | **Sect Leader**                              |
| 표국     | **Escort Bureau**                            |
| 소국주    | **Young Bureau Head**                        |
| 사숙     | **Martial Uncle**                            |
| 큰형     | **eldest brother**                           |
| 시스템              | **System**                     |
| 상태               | **Status**                     |
| 퀘스트              | **Quest**                      |
| 보상               | **Reward**                     |
| 산서     | **Shanxi**             |
| 태원     | **Taiyuan**            |
| 화산     | **Huashan**            |
| 본문      | **our sect / this sect**                                        |
| 소협      | **Young Hero**                                                  |
| 공자      | **Young Master**                                                |
| 홍진 | **Hong Jin** | Level 22 man at the City Lord's luncheon; delicate in appearance and voice. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 이풍 | **Li Feng** | Shanxi Province's Assistant Military Commissioner; former Huashan lay disciple |
| 상산왕 | **Prince Shangshan** | The City Lord and a member of the imperial family who orders the luncheon. |
| 풍양 | **Pung Yang** | Personal name of the Red Wind Band Leader. |
| 섬서 | **Shaanxi** | Province bordering Shanxi. |
| 일문일살 | **One Question, One Kill** | Jopil's alias. |
| 적풍단 | **Red Wind Band** | Rising mounted-bandit power from the northern plateau. |
| 적풍단주 | **Red Wind Band Leader** | Unnamed leader of the Red Wind Band; commands two hundred followers. |
| 만년한철 | **Ten-Thousand-Year Cold Iron** | Material that destroys Pung Yang's Body-Protecting Qi when the Unnamed Sword satisfies a specific condition. |
| 산서성 | **Shanxi Province** | Province containing the Lower District Sect branches. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 성주 | **City Lord** | Official who sends the invitation for a gathering with young prodigies. |
| 구파일방 | **Nine Sects and One Gang** | Major Murim grouping. |
| 태자 | **Crown Prince** | Title of the Emperor's older brother who was reportedly assassinated. |
| 성운표국 | **Seongun Escort Bureau** | Escort Bureau in southern Shanxi Province. |
| 홍화객잔 | **Honghwa Inn** | Inn where Taekyung, Mujin, and Cheongpung dine. |
| 산서성부 | **Shanxi Provincial Office** | Government office where the City Lord resides west of Taiyuan. |
| 도지휘동지 | **Deputy Military Commissioner** | Second-rank military office held by Eunuch Hong |
| 전하 | **His Highness** | Formal royal address for the resident prince; the official insists on this form instead of king. |
| 풍운검군 | **Wind-and-Cloud Sword Lord** | Epithet of Gong Iljung, the Zhongnan Sect's Sect Leader. |
| 주표 | **Zhu Bao** | Personal name of Prince Shangshan. |

## Listed compact profiles

### Cheongpung.md

# Cheongpung (청풍)

- **Safe through:** Chapter 143
- **Aliases:** None
- **Role:** Mysterious young man encountered at Honghwa Inn; an exceptionally young Peak master whose Level Jin Taekyung cannot determine through Qi Sense; descended from the mountains to test himself against the Ten Dragons and Phoenixes
- **Personality:** Affable, dreamy, hazy, and childlike in manner, with innocent curiosity, delight in novel public attention, and a martial artist's competitive pride
- **Voice:** Dreamy and hazy, with innocent, polite phrasing
- **Relationships:** Mae Jonghak, the Sword Saint, is his grandfather and martial instructor; Cheongpung was living with him at a hidden Huashan residence by age ten and learned Huashan martial arts; Li Feng is his Martial Nephew within Huashan's hierarchy; calls Jin Taekyung and Hyuk Mujin Benefactors after they feed him

### Hong Jin.md

# Hong Jin (홍진)

- **Safe through:** Chapter 143
- **Aliases:** None
- **Role:** Level 22 Deputy Military Commissioner of Shanxi Province and a eunuch who has served beside Prince Shangshan since infancy; the power behind the Shanxi Provincial Office and the military's second-ranking official, he manages the City Lord's luncheon and redirects a planned Shaanxi–Shanxi trade project toward Huashan.
- **Personality:** Composed, observant, and socially deft; eases tension by redirecting attention to the arriving guests and flattering Taekyung.
- **Voice:** Delicate, complimentary, and conversational.
- **Relationships:** No established relationship with Taekyung beyond recognizing him as a young hero of the Jin Family of Taiyuan.

### Jin Mukyung.md

# Jin Mukyung (진무경)

- **Safe through:** Chapter 141
- **Aliases:** Heaven Shaking Sword; Jin Family Second Young Master
- **Role:** Second son of the Jin Family of Taiyuan; twenty-three-year-old cadet at Heaven’s Gate Temple; a young Peak-level genius swordsman who won the visible exchange with Pung Yang, was then incapacitated by five concealed throwing knives, and survived the battle to recover after Taekyung's intervention; recovered enough from his Internal Injuries to return to the Jin Family of Taiyuan, though he is not yet fully recovered
- **Personality:** Reserved, terse, and easily irritated by exaggerated praise; glares coldly when Taekyung identifies him
- **Voice:** Quiet and resonant; clipped and blunt in direct speech
- **Relationships:** Taekyung’s older brother and current martial arts instructor; returned to the Jin Family after several years away

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 143
- **Aliases:** Sleeping Dragon of Shanxi
- **Role:** Modern-world protagonist; recently fired after seven years at his job; C-rank Hunter who defeated eight B-rank Minotaurs and killed a Level 70 B-rank Minotaur Warrior in one blow; First Rate martial artist standing before the Peak realm who now possesses forty-five years of internal energy with the Scorching Yang Qi attribute after fully absorbing the Blazing Flame Divine Pill; youngest son of the Jin Family of Taiyuan; new owner of a two-story detached house in Goyang intended for his family; Qi Sense reaches a seventy-meter radius; possesses one Temporary Strength Pill in his Inventory and has reserved it for a worst-case, life-threatening contingency; Level 61 with 2,100 Fame and 60 unspent stat points, and the Sleeping Dragon of Shanxi Title now grants all stats +15 and Fame +200
- **Personality:** Hungry, self-aware, dryly observant, and willing to take a questionable opportunity when desperate; treats the impossible as a game until the danger becomes undeniable
- **Voice:** First-person, conversational, dryly self-mocking; uses vivid trap-and-prey imagery, game jargon, and occasional profanity
- **Relationships:** Jin Mukyung’s younger brother and current student; son of a deceased father; supports his mother and younger sibling; loves Song Song; has a strained relationship with Lee Seowol, the current Sect Leader of the Mount Heng Sword Sect, whose marriage proposal he has decided to reject

### Jin Wikyung.md

# Jin Wikyung (진위경)

- **Safe through:** Chapter 139
- **Aliases:** Junzi Sword
- **Role:** Thirty-five-year-old Lesser Family Head and future Family Head of the Jin Family of Taiyuan; preparing to consolidate Shanxi Murim under the family's leadership
- **Personality:** Calm and authoritative in public; affectionate and protective toward Taekyung beneath a stern mask; accepts responsibility from his subordinates and shows immediate concern for family
- **Voice:** Restrained, formal, and commanding with subordinates; openly affectionate with Taekyung
- **Relationships:** Taekyung’s eldest brother and future Family Head; head of Wipeng; member of the Jin Family

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 143
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Jopil.md

# Jopil (조필)

- **Safe through:** Chapter 124
- **Aliases:** One Question, One Kill
- **Role:** Wandering martial artist and leader of a special detachment attacking the Jin Family of Taiyuan; dead by this chapter, having left behind the Supreme Peak martial art Flame Divine Palm
- **Personality:** Cruel, amused by violence, and motivated by both payment and the pleasure of hunting his targets
- **Voice:** Smoothly mocking and deceptively gentle when threatening victims
- **Relationships:** Leader of roughly fifty wandering martial artists; commands Black Mountain Blade

### Li Feng.md

# Li Feng (이풍)

- **Safe through:** Chapter 143
- **Aliases:** None
- **Role:** Assistant Military Commissioner of Shanxi Province; former Huashan lay disciple who left the sect nearly ten years ago
- **Personality:** Resolute, proud, blunt, and hostile toward political and martial rivals
- **Voice:** Formal and restrained in official settings; dry and cutting with opponents
- **Relationships:** Former lay disciple of Huashan; visited the hidden residence of his Grandmaster Mae Jonghak and saw ten-year-old Cheongpung there; recognizes Cheongpung as his Martial Uncle; direct subordinate and political rival of Hong Jin, the Deputy Military Commissioner; agrees to act as Hong Jin's intermediary with Huashan and send a messenger pigeon to his Master; bears a humiliating martial grievance involving Gong Ilhyuk

### Mae Jonghak.md

# Mae Jonghak (매종학)

- **Safe through:** Chapter 143
- **Aliases:** Sword Saint
- **Role:** Sword Saint and Cheongpung's grandfather; remained in deep seclusion at a hidden residence on Huashan
- **Personality:** Not established in this chapter.
- **Voice:** Not established in this chapter.
- **Relationships:** Cheongpung's grandfather and martial instructor; taught him the Taeeul Miri Palm.

### Prince Shangshan.md

# Prince Shangshan (상산왕)

- **Safe through:** Chapter 143
- **Aliases:** None
- **Role:** The City Lord and a member of the imperial family; ten-year-old Prince Shangshan, whose personal name is Zhu Bao, is an exceptionally skilled young swordsman who has trained daily for three years.
- **Personality:** His personal temperament is not established; his authority is treated as commanding and difficult to refuse.
- **Voice:** No direct speech appears in this chapter.
- **Relationships:** Commands the unnamed Third-Rank Assistant Military Commissioner to attend the luncheon and hosts the gathering of young Murim prodigies.

### Pung Yang.md

# Pung Yang (풍양)

- **Safe through:** Chapter 128
- **Aliases:** Red Wind Band Leader
- **Role:** Former leader of the Red Wind Band, commanding at least two hundred mounted bandits; became a mounted bandit at thirteen, reached First Rate by age thirty, and rose from squad leader to band leader three years ago; discovered the Crimson Blood martial arts and a case containing five Temporary Strength Pills in a hidden plateau tomb, reached the Peak realm in two years, and could temporarily manifest imperfect Sword Force and powerful Body-Protecting Qi by taking a pill; reached approximately seventy percent mastery of the Crimson Blood Twelve Sabers; after secretly incapacitating Jin Mukyung, resumed killing Mount Heng Sword Sect martial artists; was seriously injured by Taekyung's dagger, defeated One Annihilation, seized Taekyung, and was killed by Taekyung after the Unnamed Sword's Ten-Thousand-Year Cold Iron destroyed his Body-Protecting Qi and pierced his chest
- **Personality:** Foxlike, ruthless, observant, controlled, and willing to kill subordinates who disobey his orders
- **Voice:** Calm, concise, and authoritative when issuing orders
- **Relationships:** Leads the Red Wind Band and controls former members of other mounted-bandit groups who joined his force

## Korean source

```text
＃144화



나한테 사인을 해 달란다. 그것도 왕이.

‘뭐여, 이게.’

이런 시나리오는 내 예상에 없었는데?

황당함에 말을 잇지 못하는 나를 큼지막한 눈동자가 물끄러미 바라본다.

“과인이 너무 무리한 부탁을 한 것인가?”

“아뇨, 그건 아닌데…… 제 서명을 받아서 뭐 하시려고.”

“음, 싫으면 안 해도 되네.”

사극에서나 나올 법한 고풍스러운 말투 속에는 보이지 않는 간절함이 숨겨져 있다.

강아지처럼 연무장 바닥을 긁는 발끝과 연신 꼼지락거리는 양손이 그 증거다.

‘짜식, 귀엽기는.’

아직은 어린아이. 아무리 왕이라 해도 나이는 못 속인다.

위엄 어린 표정과는 달리 정직한 몸을 본 나는 피식 실소가 흘러나왔다.

“왜 웃는 거지?”

“아무것도 아닙니다. 그럼 이 목판에 제 이름을 새기면 되는 거죠?”

순간 어린 왕의 입가가 씰룩였다.

“가급적이면 별호도 함께.”

이게 뭐라고 또 진지하게 대답해 준다. 나는 터져 나오는 웃음을 참으며 단검을 들었다.

사각, 사각, 사각.

산서잠룡 진태경. 무릎에 목판을 대고 일곱 글자를 정성스럽게 새겨 나가던 그때 주표가 불쑥 물었다.

“검기를 사용하면 더 편하지 않겠나?”

“그렇죠.”

“그런데 왜 쓰지 않지?”

“안 쓰는 게 아니라 못 쓰는 겁니다.”

“검기를 못 쓴다니?”

“말 그대롭니다. 아직 절정 고수가 아니라서 검기를 못 써요.”

“절정 고수가…… 아니야?”

슬쩍 고개를 들어 보니 주표가 충격받은 얼굴로 나를 바라보고 있었다.

“그대는 산서잠룡이 아닌가.”

“네, 저 맞는데요.”

“한데 검기를 못 쓴다니, 절정 고수가 아니라니!”

“……그럴 수도 있죠.”

“아닐세, 그럴 수 없어!”

와, 살짝 상처받으려고 하네.

가뜩이나 근래 들어 자주 등장하는 검기 때문에 상대적 박탈감을 느끼고 있었는데, 난생처음 보는 꼬맹이가 속을 뒤집어 놓는다.

‘검기 못 쓰는 것도 죄냐.’

나는 나대로 상처받고, 주표의 어린 팬심에도 금이 갔다.

괜한 서러움에 코를 훔치던 그때였다.

“절정 고수도 아니면서 어찌 그리 강할 수 있단 말인가!”

“예?”

“일문일살 조필, 화양검 진백양, 마지막으로 얼마 전의 적풍단주 풍양까지. 지금까지 그대가 쓰러트린 적들은 모두 고강한 절정 고수들이었지 않은가?”

저 중에서 온전히 내 힘으로 쓰러트렸다고 할 만한 자는 조필밖에 없지만, 일단 고개를 끄덕였다.

“그렇죠.”

“도대체 어떻게 그런 일이 가능하지?”

“그야.”

인벤토리가 개꿀입니다. 그리고 다구리 앞에는 장사 없어요.

도저히 안 되겠다 싶을 때는 인벤토리를 뒤져 보세요. 반 갑자짜리 영약과 만년한철 무기가 나올 수도 있으니까요.

‘……이렇게 대답할 수는 없지.’

이미지는 스스로가 만들어 가는 법.

나는 잔잔한 미소와 함께 입을 열었다.

“제가 더 강했기 때문 아니겠습니까.”

“오오!”

“무림에는 이런 말이 있습니다. 강자가 살아남는 것이 아니다, 살아남는 자가 강자다.”

“오오오!”

“지금까지 세 명의 절정 고수와 싸웠습니다. 일류 고수 수십 명의 습격을 받은 적도 있지요.”

“그럴 수가!”

주표가 작은 주먹을 꼭 쥔 채 탄성을 내질렀다.

리액션이 혜자다 보니 말할 맛이 난다. 나는 지금까지 헤쳐 온 위기의 순간을 떠올리며 말을 이어 갔다.

“하지만 저는 매번 죽을힘을 다해 싸웠고, 살아남았습니다. 절정 고수? 검기? 그런 것은 중요하지 않습니다.”

“검기가 중요하지 않다니, 진심인가?”

“물론입니다.”

사실 존나게 중요하다. 만나는 놈들마다 검기를 가래떡마냥 줄줄 뽑아 대는데 나만 못 써.

한 번씩 싸울 때마다 이게 사람 목숨인지 파리 목숨인지 헷갈릴 정도다.

‘넌 영약 든든히 먹고 다녀라. 검기가 없으면 몸이 고생해.’

나는 무엄하게도 어린 왕의 어깨에 손을 올렸다. 그리고 속삭였다.

“이기고자 하는 마음. 끝까지 포기하지 않는 불굴의 의지가 지금의 산서잠룡을 만든 것이지요.”

“불굴의 의지……!”

주표의 작은 몸이 부르르 떨렸다. 이윽고 뜨거운 한숨을 내쉰 그가 입을 열었다.

“과인도 그대처럼 될 수 있을까?”

“할 수 있습니다. 방금 수련하시는 모습을 보니 금방 고수가 되실 것 같던데요.”

“그, 그 말이 정말인가?”

아니, 시스템 없으면 힘들걸.

‘하지만 자라나는 새싹에게는 물을 줘야지.’

반짝반짝 빛나는 큼지막한 눈동자를 향해 고개를 끄덕여 준 나는, 이미 완성된 목판에 몇 글자를 더 새긴 뒤 건네주었다.

“힘들 때마다 이걸 보면서 힘을 내십시오.”

“이건…….”

목판을 확인한 어린 왕이 활짝 웃었다.

“정말 고맙네. 내 이 목판을 크게 만들어 산서성부의 현판에 걸어 두지.”

“……저걸요?”

“아무렴. 이곳을 드나드는 모두가 그대의 명문(名文)을 읽게 될 걸세.”

나는 목판을 흐뭇하게 바라보는 주표를 보며 생각했다.

‘저걸 산서성부 현판에 걸어 둔다고?’



꿈☆은 이루어진다.

-산서잠룡 진태경-



……저걸?



* * *



다시 돌아온 대전은 언제 그랬냐는 듯 깔끔하게 원상 복구 된 상태였다.

하인들이 새로 들여놓은 탁자 위를 산해진미로 가득 채우자 상석에 앉아 있던 상산왕 주표가 입을 열었다.

“과인의 부름에 기꺼이 응해 준 그대들에게 감사를 표하네. 자, 이제 마음껏 드시게.”

띠링.



- 퀘스트 조건, [성주가 주최하는 오찬에 참석]을 충족시켰습니다!

- 퀘스트 보상은 오찬이 끝난 이후 지급됩니다.



이어지는 분위기는 화기애애했다. 아무래도 주최자이자 이 자리의 주인인 어린 왕이 싱글벙글 웃고 있으니 안 좋으려야 안 좋을 수가 없다.

“과인이 듣기로는 일문일살 조필은 아주 악독한 놈이라 들었는데, 어떤 자였는지 알려 줄 수 있겠나?”

“아, 그놈 아주 지독한 놈이었죠. 그러니까 그게…….”

“화양검 진백양은 중원에까지 이름이 알려진 절정 고수였다지? 얼마나 강하던가?”

“개쎕니다. 미쳤어요.”

“진 소협, 전하께서 듣고 계십니다. 부디 언행에 좀 주의를.”

“아, 죄송합니다. 아무튼, 그때 이야기를 해 보자면…….”

한참 썰을 풀고 나니 진이 빠졌다. 나는 계속해서 말을 거는 주표에게 청풍을 던져 주고 슬쩍 엉덩이를 뺐다.

“산서잠룡, 어딜 가는가?”

“검성 매종학 아시죠? 이 친구가 그분 제잡니다.”

“검성!”

“그리고 절정 고수예요. 검기 가르쳐 달라고 해 보세요.”

산타클로스를 만난 아이처럼 행복해하는 주표를 남겨 두고 옆으로 빠졌다.

말 한마디 못 꺼내 보고 꾸역꾸역 음식만 먹고 있는 산서오문의 후기지수들과 제법 진지한 분위기로 대화를 나누는 두 사람이 보였다.

전자와 후자, 둘 다 딱히 끼어들고 싶은 대화 상대는 아니다.

‘밥이나 먹자.’

하지만 고기를 몇 점 집어먹기도 전에 간드러진 목소리가 귓가를 파고들었다.

“진 소혀엽.”

“……왜요?”

저 목소리를 들으니까 갑자기 입맛이 뚝 떨어지네.

“거기서 혼자 뭐 해요? 우리 같이 이야기나 하죠.”

“싫습니다. 배고파요.”

“태원진가에 관련된 이야기인데?”

“저는 가문 일에는 관여 안 합니다. 우리 큰형님이랑 따로 얘기해 보세요.”

“아쉽네. 그럼 성운표국 쪽에 맡기는 수밖에.”

성운표국? 어디서 들어 본 이름이다 싶었는데, 어제 홍화객잔에서 흠씬 두들겨 패 준 녀석의 집안이다.

그놈이 아마 성운표국의 소국주인가 그랬지?

“성운표국이 왜요?”

홍진이 입꼬리를 말아 올렸다.

“아니에요. 식사마저 들어요. 개도 안 건드린다는데 산서잠룡을 건드리면 쓰나.”

“…….”

“호호, 농담인데 정색하기는, 어서 와서 앉아요.”

홍진이 옆자리 의자를 빼 주었고, 나는 못 이기는 척 자리에 앉았다. 물론 이풍의 옆자리에.

다시 한번 말하지만 내 엉덩이는 소중하니까.

“무슨 얘긴지 들어나 보죠. 이쪽은 영 문외한이라 별 소용없을 수도 있겠지만.”

섭섭한 척 입술을 삐죽 내밀고 있던 홍진이 입을 열었다.

“진 소협이 이 자리에서 결정하지 않아도 상관없어요. 소가주께 전달만 해 드리면 되니까. 그럼 이 첨사?”

이풍이 말을 받았다.

“이번 일에 태원진가의 힘을 빌리고 싶소.”

“이번 일이라면…….”

“섬서와 산서를 중점적으로 연결하는 것에 대해서는 알고 계실 거라 생각하오.”

“원래 종남파와 하려고 했던 그거요?”

지켜보고 있던 홍진이 고개를 끄덕였다.

“사실 종남파도 나쁘지 않은 상대예요. 구파일방에 속할 만큼 거대 문파인 데다 문주인 풍운검군을 포함한 수뇌부도 실리적인 성향이거든요. 비교적 폐쇄적인 다른 무림 문파들과는 다르죠.”

“그럼 굳이 바꿀 필요가 있었나요? 처음부터 화산파와 할 게 아니었다면 그냥 두는 게 더 나을 수도 있었을 텐데.”

“나름 심사숙고해서 내린 결정이에요. 오늘 뒤엎긴 했지만.”

홍진이 빙긋 웃으며 말을 이었다.

“나는 무림인은 아니지만 검성이 무림에서 어떤 위치를 차지하고 있는지는 잘 알고 있거든.”

“…….”

“하지만 검성이 모습을 감춘 지 삼십여 년이에요. 지금까지 화산에 남아 후인을 양성하고 있었다는 사실을 진작 알았다면 종남파를 선택하지 않았겠죠.”

말을 끝낸 홍진이 이풍을 향해 눈을 흘겼다.

보아하니 10년 전부터 검성과 청풍의 존재를 알고 있었으면서 입도 벙긋 안 한 모양이다.

“도지휘동지. 다시 말씀드리지만 그건 본문의 대외비였습니다. 청풍 사숙이 하산한 이상 감출 필요가 없어졌을 뿐.”

침착하게 대꾸한 이풍이 나를 향해 고개를 돌렸다.

“본론부터 말씀드리겠소. 표국, 섬서를 시작으로 중원까지 진출할 수 있을 만한 표국이 필요하오.”

아하, 대충 감이 잡힌다.

이들은 태원진가에 물적, 혹은 인적 자원을 지원해 달라고 부탁하고 있는 것이다.

“표국을 만들 생각이신 건가요?”

“비슷하오. 다만 우리는 태원진가의 이름을 빌리고 싶소. 대신 절반의 자금과 최대한의 편의를 제공하지.”

이건 대놓고 밀어주겠다는 소린데? 이럴 바에야 본인들 스스로 표국을 만드는 게 더 낫지 않나?

의아함을 느끼던 그때, 문득 며칠 전 진무경이 해 준 말이 떠올랐다.

‘지금의 황제도 형인 황태자를 암살하고 황위에 올랐다고 했지. 분명히.’

확인되지 않은 소문일 뿐이지만 두 사람이 몸을 사리는 걸 봐서는 영 근거 없는 말도 아닌 모양이다.

하나뿐인 아우를 굳이 변방 취급받는 산서성으로 보낸 이유도 황제의 경계심에서 비롯된 것이 아닐까?

‘음. 이것도 어째 쎄한데?’

잘못 얽힌 거 아닌지 고민하는 내게 두 사람이 말했다.

“이에 관해서는 일간 자리를 마련할 테니 진 소가주께 잘 말씀드려 주시오.”

“진 공자, 이거 좋은 제안인 거 알죠?”

“알죠, 아는데…….”

이것도 어떻게 보면 남의 집안싸움이다. 평범한 형제 사이라면 아이스크림 하나 더 먹겠다고 싸우다가 코피가 터지고 끝나겠지만, 이쪽은 아이스크림이 아니라 황위다.

코피 터지는 정도로 끝날 일이 아니라는 것이다.

“일단 큰형님께는 잘 전달해 드릴게요.”

일부러 말을 아꼈다. 어차피 결정은 진위경이 내릴 건데 내가 고민할 이유가 없다. 그가 먼저 내 의견을 물어본다면 모를까.

“그 정도면 충분해요. 진 공자가 말하는데 흘려듣진 않겠지. 진 소가주가 아우들 아끼는 거야 우리도 익히 들었으니까.”

아주 동네방네 소문이 다 났구나.

무안한 얼굴로 술잔을 쭉 들이켜는데, 한참 떨어진 탁자 끝자리에서 체할 것 같은 얼굴로 앉아 있는 사인방과 시선이 딱 마주쳤다.

아, 맞다. 하나 깜빡할 뻔했네.

“저기요. 위원장 동지. 아니 도지휘동지.”

“네?”

“표국 그거, 간판만 바꿔 달아도 충분하지 않아요?”

어리둥절한 이풍과는 달리 홍진은 씩 웃어 보였다.

“생각해 둔 곳 있어요?”

“아까 두 분이 얘기하시던 그곳.”

“성운표국? 거기 너무 만만하게 보지 마요. 명색이 산서 제일 표국이야. 한입에 소화하기 힘들어.”

“그러니까 꼭꼭 씹어 먹어야죠.”

소국주 보니까 견적이 딱 나온다. 지금의 태원진가에 홍진과 이풍이 도와준다면 뼈 채로 씹어 먹어도 소화할 수 있다.
```

## Final English reading copy

```markdown
# Chapter 144

He was asking me for an autograph. A king, no less.

*What the hell is this?*

I never saw this scenario coming.

As I struggled to continue speaking in my bewilderment, a pair of large eyes stared at me quietly.

“Have I asked too much of you?”

“No, it’s not that… What are you planning to do with my signature?”

“Hmm. If you don’t want to, you don’t have to.”

Hidden beneath his archaic, historical-drama way of speaking was a desperate eagerness he was trying to conceal.

The tips of his feet scraped at the training ground floor like a puppy, and both his hands kept fidgeting restlessly. Those were proof enough.

*The little guy is cute, though.*

He was still a child. No matter how much of a king he was, he couldn’t hide his age.

His expression was dignified, but his body language was honest. I let out a quiet laugh.

“Why are you laughing?”

“It’s nothing. So I just carve my name into this wooden tablet?”

The young king’s lips twitched.

“If possible, include your alias as well.”

Why was he answering so seriously over something like this? I held back my laughter and picked up the dagger.

Scritch, scritch, scritch.

Sleeping Dragon of Shanxi, Jin Taekyung. I rested the wooden tablet on my knee and carefully carved the seven characters into it.

That was when Zhu Bao suddenly asked,

“Wouldn’t it be easier if you used Sword Energy?”

“It would.”

“Then why aren’t you using it?”

“It’s not that I’m choosing not to. I can’t.”

“You can’t use Sword Energy?”

“I mean exactly what I said. I can’t use Sword Energy because I’m not a Peak master yet.”

“You’re… not a Peak master?”

I raised my head slightly. Zhu Bao was staring at me with a shocked expression.

“Aren’t you the Sleeping Dragon of Shanxi?”

“Yes, that’s me.”

“And yet you can’t use Sword Energy? You’re not a Peak master?”

“…That can happen.”

“No, it can’t!”

Wow. He almost sounded hurt.

I had already been feeling a sense of relative deprivation because Sword Energy had been appearing so often lately. Now a little kid I had never seen before was twisting the knife.

*Is being unable to use Sword Energy a crime?*

I was hurt in my own way, and the young prince’s fandom had taken a hit too.

I was wiping my nose in wounded frustration when he suddenly exclaimed,

“How can you be so strong if you aren’t even a Peak master?”

“What?”

“One Question, One Kill Jopil, Blade of Flowers Jin Baekyang, and finally Pung Yang, the Red Wind Band Leader, not long ago. Weren’t all the enemies you’ve defeated powerful Peak masters?”

Jopil was the only one I could honestly say I had defeated entirely with my own strength, but I nodded for the time being.

“That’s right.”

“How was such a thing possible?”

“Well…”

*The Inventory is unbelievably useful. And no one can beat a group attack.*

*When things seem impossible, try rummaging through your Inventory. You might find an elixir worth half a jiazi or a weapon made of Ten-Thousand-Year Cold Iron.*

*…I can’t exactly answer that way.*

An image was something you built for yourself.

I opened my mouth with a gentle smile.

“Isn’t it because I was stronger?”

“Wow!”

“There’s a saying in Murim. The strong do not survive. Those who survive are strong.”

“Wow!”

“I’ve fought three Peak masters so far. I’ve even been attacked by dozens of First Rate masters.”

“How could that be!”

Zhu Bao clenched his tiny fists and let out an admiring gasp.

He gave such great reactions that it made me want to keep talking. I continued, recalling the moments of crisis I had fought my way through.

“But every time, I fought with everything I had and survived. Peak masters? Sword Energy? Those things aren’t important.”

“Sword Energy isn’t important? Do you mean that?”

“Of course.”

*It’s fucking important.*

Every person I met kept drawing out Sword Energy like endless strings of rice cake, and I was the only one who couldn’t use it.

Every fight left me wondering whether I had a human life or a fly’s.

*Make sure you eat plenty of elixirs. Without Sword Energy, your body will suffer.*

I shamelessly placed a hand on the young king’s shoulder and whispered,

“The desire to win. The unbreakable will to never give up until the very end. That is what made the Sleeping Dragon of Shanxi who he is today.”

“An unbreakable will…!”

Zhu Bao’s small body trembled. Then, after letting out a heated sigh, he opened his mouth.

“Can I become like you?”

“You can. From what I just saw of your training, you look like you’ll become a master in no time.”

“D-Do you really mean that?”

*Without the System, it would be difficult.*

*But you have to water a growing sprout.*

I nodded at those enormous, sparkling eyes. Then I added a few more characters to the completed wooden tablet and handed it over.

“Look at this whenever things get difficult, and let it give you strength.”

“What is this…?”

The young king examined the tablet and broke into a radiant smile.

“Thank you very much. I shall have this tablet enlarged and hang it on the signboard of the Shanxi Provincial Office.”

“…That?”

“Of course. Everyone who enters and leaves this place will read your famous words.”

I looked at Zhu Bao, who was gazing fondly at the wooden tablet, and thought,

*He’s going to hang that on the signboard of the Shanxi Provincial Office?*

*Dreams☆come true.*

—Sleeping Dragon of Shanxi, Jin Taekyung—

*…That?*

* * *

When we returned to the grand hall, it had been restored to pristine condition as though nothing had ever happened.

Once the servants filled the newly placed tables with all kinds of delicacies, Prince Shangshan Zhu Bao, seated at the head of the table, spoke.

“I thank you all for willingly answering my summons. Now, please eat your fill.”

*Ding.*

> **System**
>
> Quest condition, **Attend the luncheon hosted by the City Lord**, has been fulfilled!
>
> The Quest Reward will be issued after the luncheon ends.

The atmosphere that followed was warm and cheerful. With the young king, the host and master of the gathering, grinning from ear to ear, it could hardly have been otherwise.

“I have heard that One Question, One Kill Jopil was an exceptionally vicious man. Could you tell me what he was like?”

“Oh, that bastard was absolutely brutal. Well, you see…”

“I’ve heard that Blade of Flowers Jin Baekyang was a Peak master whose name was known even in the Central Plains. How strong was he?”

“He was insanely strong. Completely crazy.”

“Young Hero Jin, His Highness is listening. Please be more mindful of your language.”

“Ah, sorry. Anyway, to tell you about what happened then…”

After telling stories for quite some time, I was exhausted. I handed Cheongpung over to Zhu Bao, who continued asking me questions, and quietly withdrew.

“Sleeping Dragon of Shanxi, where are you going?”

“You know the Sword Saint, Mae Jonghak, right? This guy is his disciple.”

“The Sword Saint!”

“And he’s a Peak master, too. Ask him to teach you Sword Energy.”

I left Zhu Bao behind, happy as a child who had met Santa Claus, and slipped away to the side.

I saw the young prodigies of the Five Gates of Shanxi forcing food down without managing to say a word, as well as two people engaged in a fairly serious conversation.

Neither the former nor the latter made for company I particularly wanted to join.

*I’ll just eat.*

But before I could take more than a few pieces of meat, a syrupy voice wormed into my ears.

“Young Hero Jiiin.”

“…What?”

The moment I heard that voice, my appetite vanished.

“What are you doing all by yourself over there? Come over and talk with us.”

“No, thank you. I’m hungry.”

“It’s about the Jin Family of Taiyuan.”

“I don’t get involved in family affairs. Talk to my eldest brother instead.”

“That’s unfortunate. In that case, I suppose we’ll have no choice but to entrust it to the Seongun Escort Bureau.”

Seongun Escort Bureau? The name sounded familiar. Then I remembered—it was the family of the man I had thoroughly beaten at Honghwa Inn yesterday.

That guy had been the Young Bureau Head of the Seongun Escort Bureau, hadn’t he?

“Why the Seongun Escort Bureau?”

Hong Jin curled up the corners of his mouth.

“Oh, nothing. Please eat your meal. They say even a dog is left alone while it’s eating, so how could I bother the Sleeping Dragon of Shanxi?”

“…”

“Hee-hee. I was joking. Don’t look so serious. Come over and sit down.”

Hong Jin pulled out the chair beside him. I sat down as though I had no choice.

Beside Li Feng, of course.

As I’ve said before, my backside is precious.

“Let’s hear what this is about. I’m not very knowledgeable in this area, so I may not be much help.”

Hong Jin, who had been pretending to sulk with his lips stuck out, spoke.

“It doesn’t matter if Young Hero Jin doesn’t make a decision here. You only need to pass the matter along to the Lesser Family Head. Now, Assistant Commissioner Li?”

Li Feng took over.

“We would like to borrow the strength of the Jin Family of Taiyuan for this matter.”

“This matter being…?”

“I believe you’re aware of our plan to establish a primary connection between Shaanxi and Shanxi.”

“The thing you originally intended to do with the Zhongnan Sect?”

Hong Jin, who had been watching us, nodded.

“To be honest, the Zhongnan Sect isn’t a bad partner. It’s a massive sect belonging to the Nine Sects and One Gang, and its leadership, including the Sect Leader, the Wind-and-Cloud Sword Lord, has a practical nature. They’re different from the other, relatively closed-off Murim sects.”

“Then was there really any need to change partners? If you weren’t going to work with Huashan from the beginning, it might have been better to leave things as they were.”

“It was a decision I reached after giving it a great deal of thought. Although we overturned it today.”

Hong Jin continued with a faint smile.

“I’m not a martial artist, but I know very well what position the Sword Saint occupies in Murim.”

“…”

“But it has been more than thirty years since the Sword Saint disappeared. If we had known from the beginning that he had remained in Huashan and was raising successors, we wouldn’t have chosen the Zhongnan Sect.”

When he finished speaking, Hong Jin shot Li Feng a reproachful look.

Apparently, Li Feng had known about the Sword Saint and Cheongpung for the past ten years and hadn’t said a word.

“Deputy Military Commissioner, I’ll say it again: that was classified information belonging to our sect. There was simply no longer any reason to conceal it once Martial Uncle Cheongpung descended the mountain.”

Li Feng answered calmly, then turned toward me.

“I’ll get straight to the point. We need an Escort Bureau capable of expanding into the Central Plains, beginning with Shaanxi.”

“Ah.”

I had a rough idea of what was going on.

They were asking the Jin Family of Taiyuan to provide material or human resources.

“Are you planning to create an Escort Bureau?”

“Something similar. However, we would like to borrow the name of the Jin Family of Taiyuan. In return, we’ll provide half the funding and every possible convenience.”

They were practically offering to back us outright. Wouldn’t it be better for them to create their own Escort Bureau at this point?

As I wondered about that, I suddenly remembered what Jin Mukyung had told me several days ago.

*He said that the current Emperor also assassinated his older brother, the Crown Prince, and ascended the throne. I’m sure of it.*

It was only an unconfirmed rumor, but judging by how cautiously these two were acting, it didn’t seem entirely baseless.

Could the Emperor’s wariness have been the reason he sent his only younger brother to Shanxi Province, a place regarded as a frontier region?

*Hmm. This feels suspicious too.*

As I wondered whether I had gotten myself entangled in something dangerous, the two men spoke to me.

“We’ll arrange a meeting soon regarding this matter, so please speak well of it to the Lesser Family Head.”

“Young Master Jin, you know this is a good offer, right?”

“I know. I do, but…”

In a way, this was someone else’s family feud. If they were ordinary brothers, they might fight over who got to eat one more ice cream, end up with a bloody nose, and leave it at that.

But this wasn’t ice cream. It was the imperial throne.

That meant it wouldn’t end with a bloody nose.

“I’ll make sure to pass it along to my eldest brother.”

I deliberately kept my answer vague. Jin Wikyung would be the one making the decision anyway, so there was no reason for me to worry about it. Unless he asked for my opinion first, that was.

“That’s enough. He won’t ignore what Young Master Jin says. We’ve heard plenty about how much the Lesser Family Head cares for his younger brothers.”

*So everyone in the neighborhood has heard about it.*

I drained my cup of liquor with an embarrassed expression, and my eyes met the four of them sitting at the far end of a table some distance away, all looking as though they were about to get indigestion.

Oh, right. I almost forgot something.

“Hey. Comrade Chairman—no, Deputy Military Commissioner.”

“Yes?”

“That Escort Bureau business. Wouldn’t it be enough to simply change the sign?”

Unlike the bewildered Li Feng, Hong Jin grinned.

“You have a place in mind?”

“The one the two of you were talking about earlier.”

“The Seongun Escort Bureau? Don’t take them too lightly. It’s the most prestigious Escort Bureau in Shanxi, after all. They’ll be difficult to swallow in one bite.”

“That’s why we have to chew thoroughly.”

I could tell exactly what we were dealing with from the Young Bureau Head. If Hong Jin and Li Feng helped the Jin Family of Taiyuan as it stood now, we could chew through the whole thing—bones and all—and still digest it.
```
