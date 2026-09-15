<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0145.txt",
      "sha256": "fe499a7c013b7064ddf08f9938a758409db066590898f10acb414e98363bd6d9",
      "bytes": 13806
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "9ab47761b14633d7c421b6204a348f48a33dd93073cf8c3cd7629501d71180ab",
      "bytes": 4217
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "94dcd51d9a97a620e7ca4c3d30e96e453f336cbeacc6dd362f3c2bddb71c8391",
      "bytes": 30690
    },
    {
      "path": "characters/Cheongpung.md",
      "sha256": "31c86591a01a3bba44ccd265c49d23fc38e01ec3b53ac9114d8e2203ac3b59a4",
      "bytes": 934
    },
    {
      "path": "characters/Hong Jin.md",
      "sha256": "2b85b7e7198231f6a4ae3209c0fec7335637b86b85421a875f28ee9bddc2bf9e",
      "bytes": 809
    },
    {
      "path": "characters/Jin Mukyung.md",
      "sha256": "2e0fbe67bb5c6cd28cf468101a5636215ef0df352d7fa7d2d0e9e94fd9304176",
      "bytes": 1511
    },
    {
      "path": "characters/Jin Wikyung.md",
      "sha256": "01d57024ffafd1f03d0a4286710de52cbe2395e3f7bf12044edde237c52c8927",
      "bytes": 8154
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "1c37ba9ba2dc7d849568442fd2943d2f346d729817c2df196a83c0ce41797db1",
      "bytes": 622
    },
    {
      "path": "characters/Li Feng.md",
      "sha256": "a12cbcc82d3dd9099785f0fe32526d28a7c6d2ca799f8ab0ec660b8eab53152a",
      "bytes": 888
    },
    {
      "path": "characters/Prince Shangshan.md",
      "sha256": "76e547748e4e5834813bd8f7477ee325b9f36c32a4aa8caa5dafcbf67c8c0c34",
      "bytes": 884
    },
    {
      "path": "characters/Woo Jintae.md",
      "sha256": "645dda68725ba3dacd31f6ba2daa86beabc28b212b2cba7084c8d4370661228a",
      "bytes": 805
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "26de8508df0d176c494bff03e623663a179e1507e31ba55fe0dbf9480d86fee2",
      "bytes": 26639
    }
  ],
  "estimated_tokens": 25661
}
-->

# Durable State Update — Chapter 145

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 145. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 20 concise items, `open_questions` to at most 8
items, and `temporary_decisions` to at most 8 items. Keep the serialized context
under 16384 UTF-8 bytes. Use only chapter
numbers through 145. `profile_updates` may replace one exact, uniquely occurring
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
  "chapter": 145,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 145,
    "continuity_sources": [145],
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
    "The City Lord's luncheon has concluded its attendance requirement; the associated Quest Reward is pending until the luncheon ends.",
    "Zhu Bao is an earnest young prince and enthusiastic admirer of Jin Taekyung who wants to emulate him and display his autograph at the Shanxi Provincial Office.",
    "Taekyung remains below the Peak realm and cannot use Sword Energy despite defeating Jopil, Jin Baekyang, and Pung Yang.",
    "Hong Jin and Li Feng seek the Jin Family of Taiyuan's support for an Escort Bureau expanding from Shaanxi into the Central Plains, offering half the funding and maximum convenience.",
    "The project shifted from the Zhongnan Sect to Huashan after Hong Jin learned that Mae Jonghak had remained there and raised successors.",
    "Taekyung will relay the proposal to Jin Wikyung without making the decision himself and has suggested using the Seongun Escort Bureau as the base.",
    "Cheongpung is a twenty-year-old Peak master raised by Mae Jonghak, the Sword Saint, and recognized by Li Feng as his Martial Uncle.",
    "Mae Jonghak remained in deep seclusion at a hidden Huashan residence and had been there at least ten years before the luncheon.",
    "Li Feng left Huashan after becoming discouraged by Cheongpung's extraordinary talent, not because of his defeat by Gong Ilhyuk.",
    "Cheongpung knows several Huashan martial arts and can use the Zaha Divine Technique with potent Extreme Yang internal energy.",
    "Cheongpung's exact parentage and the truth behind his claim that a crane delivered him to Mae Jonghak remain unclear.",
    "The identities of the other two members of the Three Hands of Zhongnan remain unknown.",
    "Hong Jin is a eunuch who has served Prince Shangshan since infancy and is the power behind the Shanxi Provincial Office as Deputy Military Commissioner.",
    "Gong Ilhyuk leaves the luncheon humiliated and vows revenge against those who rejected and insulted him.",
    "Taekyung encouraged Cheongpung to insult the Zhongnan disciples, and Cheongpung swore for the first time.",
    "Hong Jin and Li Feng are pursuing the Shaanxi–Shanxi trade project through Huashan, with Li Feng acting as intermediary.",
    "Li Feng commands the military's respect, while Hong Jin holds influence over civil officials and servants through fear.",
    "Cheongpung wants to join the royal guard because he admires its black armor and accepted Li Feng's Martial Nephew address in exchange for royal-guard equipment.",
    "Zhu Bao is ten years old, has trained in martial arts daily for three years, and is an exceptionally skilled young swordsman personally named Zhu Bao."
  ],
  "continuity_sources": [
    143,
    144
  ],
  "open_questions": [
    "What is Cheongpung's exact parentage, and what did Mae Jonghak mean by saying a crane delivered him?",
    "Why did Mae Jonghak remain hidden at Huashan despite the sect eventually finding his residence?",
    "What are the names and individual identities of the other two members of the Three Hands of Zhongnan?",
    "What is the full title of the wuxia novel beginning with 군림…… that Taekyung read through volume thirty-four?",
    "Was the Emperor's reported suspicion of his younger brother the reason Prince Shangshan was sent to Shanxi, and what danger does the imperial succession pose?"
  ],
  "safe_through": 144,
  "temporary_decisions": [
    "Render 전하 as “His Highness” as the formal royal address and 왕 as “king” when used literally.",
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
| 황태자 | **Crown Prince** | The Emperor's older brother in Taekyung's recollection. |

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

## Exact glossary matches

| 무림     | **Murim**          |
| 진위경    | **Jin Wikyung**    |
| 진무경    | **Jin Mukyung**    |
| 청풍     | **Cheongpung**     |
| 진천검    | **Heaven Shaking Sword**      | Jin Mukyung    |
| 검성     | **Sword Saint**               | Mae Jonghak    |
| 태원진가   | **Jin Family of Taiyuan**        |
| 화산파    | **Huashan**                      |
| 산서오문   | **Five Gates of Shanxi**         |
| 절정     | **Peak**          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 기세     | **aura** / **momentum**                          | Depends on scene                                      |
| 후기지수   | **young prodigy** / **rising martial artist**    | Contextual, not a title                               |
| 정파     | **orthodox faction**                             |                                                       |
| 마적     | **mounted bandits**                              |                                                       |
| 가주     | **Family Head**                              |
| 소가주    | **Lesser Family Head**                       |
| 문주     | **Sect Leader**                              |
| 소문주    | **Young Sect Leader**                        |
| 표국     | **Escort Bureau**                            |
| 소국주    | **Young Bureau Head**                        |
| 제자     | **Disciple**                                 |
| 사숙     | **Martial Uncle**                            |
| 산서     | **Shanxi**             |
| 태원     | **Taiyuan**            |
| 화산     | **Huashan**            |
| 본가      | **our family / this family**                                    |
| 대협      | **Great Hero** or **Sir** depending tone                        |
| 공자      | **Young Master**                                                |
| 홍진 | **Hong Jin** | Level 22 man at the City Lord's luncheon; delicate in appearance and voice. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 이풍 | **Li Feng** | Shanxi Province's Assistant Military Commissioner; former Huashan lay disciple |
| 상산왕 | **Prince Shangshan** | The City Lord and a member of the imperial family who orders the luncheon. |
| 우진태 | **Woo Jintae** | Heir of the Seongun Escort Bureau and host of the Five Gates scions. |
| 홍화루 | **Honghwaru** | Lower District Sect Shanxi branch; pleasure house in Taiyuan |
| 산서성 | **Shanxi Province** | Province containing the Lower District Sect branches. |
| 구파일방 | **Nine Sects and One Gang** | Major Murim grouping. |
| 성운표국 | **Seongun Escort Bureau** | Escort Bureau in southern Shanxi Province. |
| 도지휘첨사 | **Assistant Military Commissioner** | Military office held by the unnamed official responsible for training soldiers. |
| 도지휘동지 | **Deputy Military Commissioner** | Second-rank military office held by Eunuch Hong |
| 종남삼수 | **Three Hands of Zhongnan** | Three renowned Zhongnan Sect martial artists invited to the gathering |
| 전하 | **His Highness** | Formal royal address for the resident prince; the official insists on this form instead of king. |
| 주표 | **Zhu Bao** | Personal name of Prince Shangshan. |

## Listed compact profiles

### Cheongpung.md

# Cheongpung (청풍)

- **Safe through:** Chapter 144
- **Aliases:** None
- **Role:** Mysterious young man encountered at Honghwa Inn; an exceptionally young Peak master whose Level Jin Taekyung cannot determine through Qi Sense; descended from the mountains to test himself against the Ten Dragons and Phoenixes
- **Personality:** Affable, dreamy, hazy, and childlike in manner, with innocent curiosity, delight in novel public attention, and a martial artist's competitive pride
- **Voice:** Dreamy and hazy, with innocent, polite phrasing
- **Relationships:** Mae Jonghak, the Sword Saint, is his grandfather and martial instructor; Cheongpung was living with him at a hidden Huashan residence by age ten and learned Huashan martial arts; Li Feng is his Martial Nephew within Huashan's hierarchy; calls Jin Taekyung and Hyuk Mujin Benefactors after they feed him

### Hong Jin.md

# Hong Jin (홍진)

- **Safe through:** Chapter 144
- **Aliases:** None
- **Role:** Level 22 Deputy Military Commissioner of Shanxi Province and a eunuch who has served beside Prince Shangshan since infancy; the power behind the Shanxi Provincial Office and the military's second-ranking official, he manages the City Lord's luncheon and redirects a planned Shaanxi–Shanxi trade project toward Huashan.
- **Personality:** Composed, observant, and socially deft; eases tension by redirecting attention to the arriving guests and flattering Taekyung.
- **Voice:** Delicate, complimentary, and conversational.
- **Relationships:** No established relationship with Taekyung beyond recognizing him as a young hero of the Jin Family of Taiyuan.

### Jin Mukyung.md

# Jin Mukyung (진무경)

- **Safe through:** Chapter 144
- **Aliases:** Heaven Shaking Sword; Jin Family Second Young Master
- **Role:** Second son of the Jin Family of Taiyuan; twenty-three-year-old cadet at Heaven’s Gate Temple; a young Peak-level genius swordsman who won the visible exchange with Pung Yang, was then incapacitated by five concealed throwing knives, and survived the battle to recover after Taekyung's intervention; recovered enough from his Internal Injuries to return to the Jin Family of Taiyuan, though he is not yet fully recovered
- **Personality:** Reserved, terse, and easily irritated by exaggerated praise; glares coldly when Taekyung identifies him
- **Voice:** Quiet and resonant; clipped and blunt in direct speech
- **Relationships:** Taekyung’s older brother and current martial arts instructor; returned to the Jin Family after several years away

### Jin Wikyung.md

# Jin Wikyung (진위경)

- **Safe through:** Chapter 144
- **Aliases:** Junzi Sword
- **Role:** Thirty-five-year-old Lesser Family Head and future Family Head of the Jin Family of Taiyuan; preparing to consolidate Shanxi Murim under the family's leadership
- **Personality:** Calm and authoritative in public; affectionate and protective toward Taekyung beneath a stern mask; accepts responsibility from his subordinates and shows immediate concern for family
- **Voice:** Restrained, formal, and commanding with subordinates; openly affectionate with Taekyung
- **Relationships:** Taekyung’s eldest brother and future Family Head; head of Wipeng; member of the Jin Family

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 144
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Li Feng.md

# Li Feng (이풍)

- **Safe through:** Chapter 144
- **Aliases:** None
- **Role:** Assistant Military Commissioner of Shanxi Province; former Huashan lay disciple who left the sect nearly ten years ago
- **Personality:** Resolute, proud, blunt, and hostile toward political and martial rivals
- **Voice:** Formal and restrained in official settings; dry and cutting with opponents
- **Relationships:** Former lay disciple of Huashan; visited the hidden residence of his Grandmaster Mae Jonghak and saw ten-year-old Cheongpung there; recognizes Cheongpung as his Martial Uncle; direct subordinate and political rival of Hong Jin, the Deputy Military Commissioner; agrees to act as Hong Jin's intermediary with Huashan and send a messenger pigeon to his Master; bears a humiliating martial grievance involving Gong Ilhyuk

### Prince Shangshan.md

# Prince Shangshan (상산왕)

- **Safe through:** Chapter 144
- **Aliases:** None
- **Role:** The City Lord and a member of the imperial family; ten-year-old Prince Shangshan, whose personal name is Zhu Bao, is an exceptionally skilled young swordsman who has trained daily for three years.
- **Personality:** Earnest, admiring, and eager to emulate Jin Taekyung; despite his royal dignity, he shows openly childlike enthusiasm for martial arts and Taekyung's reputation.
- **Voice:** Archaic and formal in the manner of a historical drama, with openly eager and childlike reactions beneath his royal diction.
- **Relationships:** Commands the unnamed Third-Rank Assistant Military Commissioner to attend the luncheon and hosts the gathering of young Murim prodigies; admires Jin Taekyung and seeks to emulate him.

### Woo Jintae.md

# Woo Jintae (우진태)

- **Safe through:** Chapter 138
- **Aliases:** None
- **Role:** Heir of the Seongun Escort Bureau and a leading scion of the current Five Gates of Shanxi; hosts its young members at Honghwa Inn and prepares for the City Lord's luncheon.
- **Personality:** Boastful, calculating, status-conscious, and manipulative; treats lavish gifts and money as tools for creating obligations, but becomes enraged and desperate when publicly humiliated.
- **Voice:** Charming and lavish in public, with polished courtesy that turns dry and contemptuous when he judges someone beneath him.
- **Relationships:** Heir to the Seongun Escort Bureau; cultivates the current Five Gates scions through hospitality, gifts, and bribes.

## Korean source

```text
＃145화



홍진이 피식 웃으며 술잔을 기울였다.

“우리 진 공자, 생각보다 욕심이 많으시구나?”

“남들만큼은 있는 편이죠. 그리고 부탁인데, 그냥 진 공자라고 불러 주시면 안 될까요.”

“어머, 좋으면서 싫은 척하기는.”

“족 같네…….”

“응? 방금 뭐라고 했어요?”

“아, 가족 같아서 좋다고요.”

“가족이라, 듣기 좋네. 벌써부터 진 소가주님과의 만남이 기다려지는데요?”

맞다. 이 자리에 입 아프게 떠들어 봤자 결국 결정하는 건 진위경과 홍진이다.

둘 다 이 방면에서는 프로나 다름없으니 아마추어는 빠져 줘야 하는 게 도리겠지.

“그나저나 성운표국에는 무슨 악감정이 있어서 이러는 거예요?”

“악감정이랄 것까진 없고…… 미운 놈 뺨 한 대 더 때려 주는 거죠. 떡고물도 챙길 수 있으니 좋고.”

“아하, 원래 오기로 했던 성운표국의 소국주와 관련된 일?”

이 인간, 눈치가 보통이 아니다.

대강 눈치챈 마당에 괜히 미주알고주알 설명할 필요도 없을 것 같아서 어깨를 으쓱해 보였다.

“뭐, 비슷합니다. 어떻게 아셨어요?”

“진 공자. 난 이십 년을 넘게 황궁(皇宮)에서 살았어요.”

“네?”

“눈치 하나로 살아남았다는 뜻이에요. 어린애들 표정 읽는 것 정도야 쉽지.”

홍진이 산서오문의 후기지수들을 턱짓으로 가리켰다.

멀찍이 떨어진 탁자 끄트머리, 바짝 얼어붙은 표정으로 이쪽을 힐끔거리던 녀석들이 화들짝 놀라며 움츠러든다.

“처음 들어올 때부터 저러더라고. 진 공자 눈치만 살살 살피면서.”

“그랬어요?”

“응. 보는 내가 다 애처로울 정도였다니까. 도대체 무슨 짓을 한 거예요?”

“아까 나가신 분들이랑 비슷한 일이 있었죠.”

“종남삼수? 쯧쯧. 사람을 못 알아봤구나?”

역시 척 하면 착이다. 홍진은 안타깝다는 듯이 혀를 찼고, 이풍은 고개를 홱 돌려 후기지수들을 응시했다.

마치 ‘청풍 사숙’을 건드린 놈들이 누군지 똑똑히 기억해 두겠다는 듯한 눈빛이었다.

“헉.”

“도, 도지휘첨사. 아니, 이 대협. 그게 아니옵고…….”

산서성 군부의 실력자인 데다 화산파 속가제자인 이풍이다.

제아무리 관과 무림이 불가침의 관계라지만 잘못 얽히면 산서오문의 미래가 아주 재미없어질 게 뻔하다.

황급히 변명을 늘어놓는 녀석들을 뒤로하고 이풍이 내게 물었다.

“그 얘기, 자세히 들려줄 수 있겠소?”

“다 끝난 얘기예요. 당사자가 직접 빠따도 쳤는데요, 뭘.”

“빠따?”

“아, 두들겨 팼다는 뜻입니다. 물론 그 전에 사과도 했고요.”

“사숙이 직접 말이오? 흠.”

정확히는 한 명만 조졌지만 때리긴 때린 거다.

이풍이 한결 누그러진 눈빛으로 후기지수들을 바라봤다.

“네놈들의 잘못을 알고 있느냐?”

“예, 옛!”

“뼈저리게 느끼고 있습니다!”

곧장 터져 나오는 우렁찬 외침. 이풍도 이풍이지만 청풍의 신분을 알았으니 똥줄이 탈 만하다.

절정 고수인 건 둘째치고, 무려 검성의 제자에 화산파의 적전제자 아닌가.

‘아주 제대로 엿 된 거지.’

산서오문이라고 해 봤자 결국 중소 문파. 구파일방인 화산파가 열받으면 일가친척까지 빠따를 맞을 수도 있다.

아니, 고작 그걸로 끝나면 다행이지.

“오늘 이곳에서 나눴던 대화와 일들은…….”

이풍의 묵직한 음성이 이어지기도 전에 대답이 튀어나왔다.

“함구하겠습니다!”

“무덤까지 갖고 가겠습니다!”

“전 이미 잊었어요!”

“여기가 어디죠? 제가 누구죠?”

……아주 지랄들을 하는구나.

기억상실증 환자가 속출하는 광경을 바라보고 있던 나는 한마디를 보탰다.

“그걸로 되겠어?”

“예, 예?”

“그게 무슨 말씀이신지…….”

“무슨 말씀이긴. 한 식구 되고 싶으면 너희도 숟가락 얹으라는 얘기지. 거기 너, 식구 뜻이 뭐야?”

지목당한 후기지수가 더듬더듬 대답했다.

“같이 밥 먹는…… 아니라면 죄송합니다.”

“맞았어. 자, 그럼 식구가 되려면 어떻게 해야 할까?”

“아!”

후기지수가 탄성과 함께 이마를 탁 쳤다.

그나마 눈치는 좀 있는 놈이군.

“그럼 다음에 제가 좋은 자리를 마련하겠습니다. 홍화루 어떠십니까?”

“…….”

돌대가리가 따로 없네.

후계자라는 것들이 이 모양이니 산서오문 꼬라지는 안 봐도 뻔하다. 나는 한숨을 푹 내쉬고 간단명료하게 설명해 주었다.

“홍화루는 집어치우고 우리 쪽에서 시키는 거 잘하란 말이야. 가령 성운표국에 관련된 문제라든가, 응?”

“아아.”

태원진가는 분명 산서 제일의 세력을 갖추게 됐지만 중소 문파가 똘똘 뭉쳐 반발한다면 피곤한 일이 생길 게 뻔했다.

명색이 정파 무림 소속인데, 마적 떼처럼 닥치는 대로 뺏고 책임을 물었다가는 손가락질을 받을 테니까.

무림에서 무공만큼이나 중요한 것이 바로 명분 아닌가?

‘하지만 손가락질할 놈들만 없다면 문제 될 것도 없지.’

나는 네 명의 남녀를 천천히 눈에 담았다. 산서오문 중 성운표국을 제외한 네 문파의 후계자들.

이들이 앞장서서 태원진가의 손을 들어 준다면 일이 한층 쉬워질 거다.

“밥 먹을 때 어디에 앉아야 할지 잘 봐. 그래야 한 입씩이라도 얻어먹지.”

비록 변방이라지만 명색이 한 성에서 첫손가락에 꼽는다는 성운표국. 이만하면 조금씩 나눠 먹어도 충분한 진수성찬이다.

내 말에 눈치 빠른 놈은 조용히 눈을 반짝였고, 눈치 없는 놈은 조심스럽게 입을 열었다.

“그래도 그건 좀…….”

나는 어벙해 보이는 놈의 말을 칼같이 잘라 냈다.

“너, 어디 문파 소속이냐?”

“저, 저 말씀이십니까?”

“그래, 너.”

한참을 머뭇거린 끝에 고평문이라는 이름이 튀어나왔다.

얼핏 들어 본 이름 같긴 한데, 기억이 가물가물한 듣보잡 문파. 고평문의 위치는 딱 그 정도다.

아니, 신(新) 산서오문의 위치가 전부 마찬가지였다.

“고평문. 고평문…… 어감이 별로네. 내가 새로 하나 추천해 줘?”

“예?”

아직도 감을 못 잡는 놈의 눈동자를 들여다보며 말을 이었다.

“다음 달부터는 새 이름으로 다시 시작하자. 태원진가 고평지부로. 어때?”

“……!”

“……!”

“마음에 안 드나 보네. 그냥 한번 해 본 소리야, 인마.”

물론 그냥 해 본 소리는 아니지.

나는 새파랗게 질린 고평문 소문주의 어깨를 탁탁 두드리며 좌중을 쓸어 봤다.

“여기 우진태랑 의형제, 의남매 맺은 사람 있냐?”

“어, 없습니다.”

“아니면 어릴 때부터 십 년 넘게 봐 온 끈끈한 사이라든지. 태중 혼약이라든지. 뭐 많잖아?”

“절대! 절대 아닙니다. 몇 번 어울린 게 전부예요.”

“저, 저도 비단 몇 필 선물 받고 보석 조금…….”

“그럼 됐네.”

짝!

날카로운 박수 소리에 네 남녀의 몸이 흠칫 떨렸다.

“선택해. 태원진가와 화산파, 그리고 관까지 적으로 돌릴 건지, 아니면…….”

나는 씩 웃으며 또박또박, 마지막 말을 읊었다.

“별로 안 친한 놈 버리고 우리랑 같이 나눠 먹을 건지.”

짝짝짝짝.

이번에는 내가 아니다. 홍진이 깔깔 웃으며 박수를 치고 있었다.

“우리 진 공자, 보면 볼수록 마음에 든다니까?”

“…….”

그런 위험 발언은 자제해 주십시오, 형님.



* * *



“벌써 가는 것이냐?”

여전히 오만한 말투였지만 목소리와 눈빛에는 아쉬움이 한가득이다.

‘자식, 볼수록 귀엽네.’

나는 꼬마 팬, 아니 상산왕 주표의 머리를 쓰다듬어…… 주려다가 이풍의 눈빛에 손을 내렸다.

아, 맞다. 얘 왕이었지. 그것도 황족.

“커흠. 저도 급한 볼일이 있는지라.”

“나중으로 미루면 안 되겠느냐?”

“죄송합니다. 한시를 다투는 일이라서.”

“그런가…….”

시무룩한 꼬맹이의 얼굴을 보니 살짝 죄책감이 들기는 개뿔, 얼른 본가로 돌아가서 푹 쉬고 싶다.

때맞춰 홍진이 간드러진 목소리로 끼어들었다.

“전하, 제가 있으니 여기 진 공자는 그만 보내 주세요. 네?”

그러나 주표는 고집스러운 얼굴로 날 바라볼 뿐이었다.

“하면 언제쯤 그대를 다시 볼 수 있지?”

“어, 글쎄요. 천 밤쯤 지나면?”

“천 밤!”

주표가 충격받은 얼굴로 외쳤다.

약 3년. 이제 고작 열 살인 어린아이에겐 어마어마한 시간일 것이다.

“그, 그렇게 바쁘단 말이냐?”

“어른의 사정이란 것이 있습니다. 전하.”

“허어어, 돌아가신 아바마마께서도 그 정도는 아니셨는데…….”

상심이 매우 큰 모양이다. 고개를 푹 떨군 주표를 일으켜 세운 건 다음 순간 들려온 이풍의 한마디였다.

“전하, 이렇게 하시는 것은 어떻겠습니까?”

“뭘 말인가?”

“보름 후 태원진가에서 성대한 연회가 열린다고 하니 전하께서 직접 태원진가를 방문하시는 겁니다.”

“태원진가를?”

“예. 산서에서 난다 긴다 하는 고수들이 모두 모일 테니 분명 흡족하실 겁니다.”

주표의 눈동자가 반짝반짝 빛났다.

“옳거니, 그런 방법이 있었구나!”

“예, 전하.”

“…….”

아니, 이것들이 지금 무슨 얘기를 하고 있는 거야.

초대도 안 했는데 아주 상상의 나래를 펼치고 있다. 그렇다고 오지 말라고 하면 일이 터질 기세라 그냥 고개를 끄덕이는 수밖에 없었다.

“이 대협 말이 맞습니다. 그때 한번 놀러 오세요.”

“그래도 될까?”

참 일찍도 물어본다.

나는 영업용 미소를 띠고 대답했다.

“당연하죠. 제 형님들도 반가워할 겁니다.”

“그, 그게 정말인가?”

“네, 제 형님들이 누군지 아시죠? 둘째 형은 구면이실 거고.”

“진천검?”

해맑던 주표의 얼굴에 순간 먹구름이 꼈다.

“그대의 둘째 형은 과인을 싫어한다. 삼 년 전에도 아무 말 없이 밥만 먹고 갔지. 무례하기까지 했어.”

“……아무 말도 안 했다고요?”

“그날에 대한 얘기는 더 이상하기 싫다.”

홍진이 조그마한 목소리로 속삭였다.

“전하께서 서명을 부탁하셨는데 단칼에 거절하더군요.”

진무경이 초청을 받았던 게 3년 전이라고 했으니까…… 주표가 일곱 살 때다.

세상에. 어떻게 일곱 살 어린애, 그것도 왕이 사인을 부탁하는데 딱 잘라 거절할 수 있지?

‘그 인간도 어지간하네.’

어떤 의미에서는 참 진무경답다.

팬심이 무참히 짓밟힌 과거의 기억을 떠올린 주표는 말없이 손가락을 꼬물거렸다.

가만히 보고 있자니 어쩐지 마음 한구석이 짠하다.

“이번에 오시면 제가 부탁해서 서명 받아 드릴게요.”

“헛. 정말?”

“약속. 도장 꽝.”

어리둥절해하는 녀석과 새끼손가락도 걸고 도장까지 찍었다.

“이게 무엇이지?”

“천지신명께 맹세한다. 뭐 그런 뜻입니다.”

“오오!”

주위에서는 황족이니, 왕이니 난리지만 역시 애는 애다.

좋아서 어쩔 줄을 모르는 주표의 모습에 사람들도 흐뭇하게 웃었다.

“전하께서 저렇게 기뻐하시는 모습은 오랜만에 봅니다.”

“그러게요. 매일 재미없는 이 첨사만 상대하다가 오랜만에 활짝 웃으시네요.”

“전 최선을 다한 것밖에 없습니다.”

“최선이 꼭 최고의 결과를 만드는 건 아니죠. 그럴 수 있어요.”

“도지휘동지!”

“왜요, 도지휘첨사?”

이풍과 홍진.

사이가 좋은 건지, 나쁜 건지 도무지 종잡을 수 없는 두 사람이 티격태격할 때 청풍이 잔뜩 기대하는 얼굴로 주표에게 다가갔다.

“저도, 저도 서명해 드릴까요?”

“……당신 서명 처음 해 보지?”

“헛. 어떻게 아셨어요? 오는 길에 쟁자수로 수결(手決)은 해 봤어도 서명은 처음인데.”

“모르는 게 이상한 거 아냐?”

저 기대하는 표정 봐라. 누군가에게 난생처음 서명을 해 주고 싶어서 안달이 난 표정이다.

“저, 전 서명하면 안 되나요?”

“아니. 맘대로 해. 서명해 드리면 전하께서 좋아하실걸.”

하지만 주표의 반응은 예상 밖이었다.

“서명? 그대가?”

“네! 꼭 서명해 드리고 싶습니다!”

“안 된다.”

“왜, 왜요? 저희 할아버지 되게 유명한 분이시래요. 검성 못 들어 보셨어요?”

“알지. 당연히 알지. 하지만…….”

주표가 짐짓 단호한 얼굴로 고개를 저었다.

“그대는 아직 별호가 없지 않나.”

“네?”

“나중에 멋있는 별호가 생기면 다시 오도록. 그땐 내 반드시 서명을 받도록 하지.”

“…….”

“…….”

저거 네임드만 할 수 있는 거였구나.
```

## Final English reading copy

```markdown
# Chapter 145

Hong Jin let out a quiet laugh and tilted his cup.

“Our Young Master Jin, you’re greedier than I thought.”

“I’m about as greedy as anyone else. And I have a favor to ask. Could you just call me Young Master Jin?”

“Oh my, pretending you don’t like it when you do.”

“Fucking hell…”

“Hm? What did you say just now?”

“Ah, I said it’s nice. It feels like family.”

“Family, huh? That’s nice to hear. I’m already looking forward to meeting the Lesser Family Head Jin.”

Right. No matter how much I talked in this room, the final decision would be made by Jin Wikyung and Hong Jin.

Both of them were practically professionals in this area, so it was only proper for an amateur to step aside.

“By the way, what grudge do you have against the Seongun Escort Bureau?”

“It’s not quite a grudge… I’m just giving an extra slap to someone I dislike. And it doesn’t hurt that I can pick up a few crumbs along the way.”

“Ah. Is this related to the Young Bureau Head of the Seongun Escort Bureau who was originally supposed to come?”

This man’s instincts were anything but ordinary.

Since he had already figured it out, there seemed to be no need to explain every little detail. I simply shrugged.

“Something like that. How did you know?”

“Young Master Jin, I’ve lived in the imperial palace for more than twenty years.”

“Excuse me?”

“I survived on my ability to read the room. Reading the expressions of children is easy enough.”

Hong Jin gestured with his chin toward the young prodigies of the Five Gates of Shanxi.

At the far end of a distant table, the young men and women had been sneaking glances our way with frozen expressions. They flinched and shrank back when they realized they had been noticed.

“They’ve been like that since they first came in. Carefully watching Young Master Jin’s every move.”

“Really?”

“Yes. I almost felt sorry for them just watching. What on earth did you do?”

“They had something similar happen with the people who left earlier.”

“The Three Hands of Zhongnan? Tsk, tsk. They failed to recognize who they were dealing with, didn’t they?”

As expected, Hong Jin understood everything with the slightest hint. He clicked his tongue sympathetically, while Li Feng abruptly turned his head and stared at the young prodigies.

His eyes seemed to say he would remember exactly who had provoked Martial Uncle Cheongpung.

“Gasp.”

“Assistant Military Commissioner! No, Great Hero Li! It’s not like that…”

Li Feng was not only a powerful figure in the Shanxi Province military but also a lay disciple of Huashan.

Even though the government and Murim were supposed to remain separate, getting entangled with him in the wrong way would make the future of the Five Gates of Shanxi very unpleasant.

Ignoring the young men as they hurriedly offered excuses, Li Feng asked me,

“Could you tell me more about what happened?”

“It’s all over now. The person involved even beat them himself. What more is there to say?”

“Beat them himself?”

“Ah, I mean he beat them up. Of course, they apologized before that.”

“Martial Uncle did it himself? Hmm.”

Strictly speaking, Cheongpung had only dealt with one of them, but he had beaten him all the same.

Li Feng looked at the young prodigies with a much gentler gaze.

“Do you understand what you did wrong?”

“Yes, sir!”

“We feel it in our bones!”

Their booming replies erupted immediately. It wasn’t only Li Feng’s position that had them sweating bullets. They now knew Cheongpung’s identity as well.

Putting aside the fact that he was a Peak master, he was the Disciple of the Sword Saint and Huashan’s direct Disciple.

*They’re completely screwed.*

The Five Gates of Shanxi were ultimately nothing more than a collection of minor sects. If Huashan, one of the Nine Sects and One Gang, got angry, even their extended families might get beaten with a bat.

No, they would be lucky if it ended there.

“The conversations and events that took place here today…”

Li Feng’s heavy voice had barely begun when the answers came flying out.

“We’ll keep silent!”

“We’ll take it to our graves!”

“I’ve already forgotten everything!”

“Where are we? Who am I?”

*They’re really putting on a fucking show.*

As I watched an epidemic of amnesia break out before my eyes, I added one more thing.

“Is that enough?”

“Ex-Excuse me?”

“What do you mean?”

“What do I mean? If you want to become part of the family, you need to put your spoon in too. You there. What does ‘family’ mean?”

The young prodigy I had pointed at stammered out an answer.

“People who eat together… Unless that’s not it, in which case, I’m sorry.”

“That’s right. Now, how do you become family?”

“Ah!”

The young prodigy slapped his forehead with a cry of realization.

At least that one had some sense.

“Then I’ll arrange a fine place for our next meeting. How about Honghwaru?”

“……”

What a complete idiot.

With heirs like these, the state of the Five Gates of Shanxi was obvious without even looking. I let out a deep sigh and explained it simply.

“Forget Honghwaru. I’m telling you to do whatever our side tells you to do. For example, anything involving the Seongun Escort Bureau. Understand?”

“Ohhh.”

The Jin Family of Taiyuan had certainly become the greatest power in Shanxi, but if the minor sects united and resisted, it would inevitably become a nuisance.

We belonged to the orthodox faction, after all. If we seized whatever we wanted and held people accountable like a band of mounted bandits, everyone would point fingers at us.

Wasn’t legitimacy just as important as martial arts in Murim?

*But if there’s no one left to point fingers, it won’t be a problem.*

I slowly took in the four men and women before me—the heirs of the four sects among the Five Gates of Shanxi, excluding the Seongun Escort Bureau.

If they stepped forward and sided with the Jin Family of Taiyuan, things would become much easier.

“When you’re eating, pay close attention to where you sit. That way, you can at least get a bite or two.”

The Seongun Escort Bureau was supposedly one of the most prominent powers in the province, despite being located in a frontier region. It was more than enough of a feast to share around.

At my words, the quick-witted one’s eyes quietly gleamed, while the clueless one cautiously opened his mouth.

“Even so, that might be a little…”

I cut off the dense-looking young man before he could finish.

“What sect are you from?”

“M-Me?”

“Yes, you.”

After a long hesitation, the name Gopyeong Sect finally came out.

It was a name I vaguely recognized—a minor sect so obscure that I could barely remember hearing it. That was about the extent of Gopyeong Sect’s standing.

No, that was true of all the sects in the new Five Gates of Shanxi.

“Gopyeong Sect. Gopyeong Sect… It doesn’t have a very pleasant ring to it. Should I recommend a new name?”

“Excuse me?”

I stared into his eyes as he continued to fail to understand.

“Starting next month, let’s begin again under a new name. The Gopyeong Branch of the Jin Family of Taiyuan. How does that sound?”

“……!”

“……!”

“You don’t seem to like it. I was only saying it for fun, you idiot.”

Of course, I hadn’t been saying it for fun.

I patted the deathly pale Young Sect Leader of Gopyeong Sect on the shoulder and swept my gaze across the room.

“Is anyone here sworn brothers or sisters with Woo Jintae?”

“N-No, sir.”

“Or perhaps you’ve been close friends since childhood, watching each other for more than ten years? Maybe you were betrothed before birth? There are plenty of possibilities.”

“Absolutely not! Absolutely not. We’ve only spent time together a few times.”

“I-I only received a few bolts of silk and a little jewelry…”

“Then that settles it.”

Clap!

The sharp sound of my hands coming together made the four men and women flinch.

“Choose. Are you going to make enemies of the Jin Family of Taiyuan, Huashan, and the government, or…”

I grinned and enunciated the final words clearly.

“Are you going to abandon someone you aren’t even close to and share the feast with us?”

Clap, clap, clap, clap.

This time, it wasn’t me. Hong Jin was laughing loudly and applauding.

“Our Young Master Jin, I like you more and more every time I see you.”

“……”

*Brother, please refrain from making dangerous remarks.*

* * *

“Are you leaving already?”

His tone was still arrogant, but his voice and eyes were filled with regret.

*The more I see him, the cuter he gets.*

I was about to pat the head of my little fanboy—no, Prince Shangshan Zhu Bao—when I lowered my hand under Li Feng’s gaze.

*Oh, right. He was a king. And a member of the imperial family, at that.*

“Ahem. I have some urgent business to attend to.”

“Can you not put it off until later?”

“I’m sorry, but it’s a matter where every moment counts.”

“I see…”

Looking at the dejected kid’s face made me feel a little guilty—like hell it did. I wanted to hurry back home to my family and get some proper rest.

Right then, Hong Jin cut in with his delicate voice.

“His Highness, I’m here, so please let Young Master Jin go now. All right?”

But Zhu Bao only stared at me stubbornly.

“Then when shall I be able to see you again?”

“Hmm, I don’t know. After a thousand nights?”

“A thousand nights!”

Zhu Bao cried out with a shocked expression.

That was approximately three years. For a child who was only ten years old, it must have seemed like an enormous amount of time.

“Are you truly that busy?”

“There are such things as adult matters, Your Highness.”

“Good heavens. Even my late father was never that busy…”

He seemed deeply disheartened. Zhu Bao’s head drooped, but Li Feng’s next words made him straighten up again.

“Your Highness, what do you think of this?”

“What do you mean?”

“I hear the Jin Family of Taiyuan will be holding a grand banquet in fifteen days. Why don’t you pay the Jin Family of Taiyuan a personal visit?”

“The Jin Family of Taiyuan?”

“Yes. All the masters who are famous throughout Shanxi will be gathered there, so I’m sure you’ll be pleased.”

Zhu Bao’s eyes began to sparkle.

“Of course! Why didn’t I think of that?”

“Yes, Your Highness.”

“……”

What the hell were these two talking about?

They hadn’t even been invited, yet they were spreading their wings and soaring through the realm of imagination. But if I told him not to come, it felt as though something would explode, so all I could do was nod.

“Great Hero Li is right. Come visit us then.”

“Would that really be all right?”

He was asking rather late.

I answered with a professional smile.

“Of course. My brothers will be happy to see you too.”

“Is that really true?”

“You know who my brothers are, don’t you? You should already be acquainted with my second brother.”

“Heaven Shaking Sword?”

A dark cloud suddenly fell over Zhu Bao’s bright, innocent face.

“Your second brother dislikes me. Three years ago, he only ate and left without saying a word. He was even rude.”

“He didn’t say a single word?”

“I do not wish to speak of that day anymore.”

Hong Jin whispered in a tiny voice,

“His Highness asked him for an autograph, but he flatly refused.”

Jin Mukyung had said he was invited three years ago, so…

Zhu Bao must have been seven at the time.

Good grief. How could anyone flatly refuse when a seven-year-old child—an actual king, no less—asked for his autograph?

*That man really is something.*

In a way, it was very much like Jin Mukyung.

Recalling how his fanboy enthusiasm had been so brutally crushed, Zhu Bao silently fidgeted with his fingers.

Watching him, I felt a pang of sympathy.

“If you come this time, I’ll ask him to give you his autograph.”

“Really?”

“Pinky promise. Seal it.”

I even hooked pinkies with the bewildered boy and sealed our promise.

“What is this?”

“It means I swear before the gods of heaven and earth.”

“Oh!”

Everyone around us was making a fuss because he was royalty, because he was a king, and so on. But a child was still a child.

Seeing Zhu Bao so happy that he didn’t know what to do, everyone smiled fondly.

“It’s been a long time since I’ve seen His Highness this happy.”

“I know. After dealing with that boring Assistant Military Commissioner every day, he’s smiling brightly for the first time in ages.”

“I’ve only been doing my best.”

“Doing your best doesn’t always produce the best result. It happens.”

“Deputy Military Commissioner!”

“What is it, Assistant Military Commissioner?”

Hong Jin and Li Feng.

I could never tell whether the two of them got along or hated each other as they bickered back and forth.

Meanwhile, Cheongpung approached Zhu Bao with an expectant expression.

“Can I sign something for you too?”

“……”

“You’ve never signed your name before, have you?”

“Gasp. How did you know? I’ve left my hand mark as a luggage porter before, but this is my first autograph.”

“Wouldn’t it be strange if I didn’t know?”

Just look at that eager expression. He looked desperate to give someone his very first autograph.

“C-Can I not sign one?”

“No. Do whatever you want. His Highness will be happy if you give him your autograph.”

But Zhu Bao’s reaction was unexpected.

“An autograph? Yours?”

“Yes! I really want to give you my autograph!”

“No.”

“W-Why not? They say my grandfather is a very famous man. Haven’t you heard of the Sword Saint?”

“I know. Of course I know. But…”

Zhu Bao put on a deliberately stern expression and shook his head.

“You don’t have a martial title yet, do you?”

“Excuse me?”

“Come back after you’ve acquired a cool martial title. Then I shall certainly get your autograph.”

“……”

“……”

*So this was something only named characters could do.*
```
