<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0154.txt",
      "sha256": "f46589a88b00b171840c4c5866b5a816d35f85759d8a44d4dfa7f8e859848239",
      "bytes": 16921
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "d931813ca5f6585e7100672ce8f1f645389b40b9171c1ac542f9526ac008bf7e",
      "bytes": 6600
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "378806c0305619563a023f02f110f470494e3b50ebba68c772fd0080ee69d0ce",
      "bytes": 35201
    },
    {
      "path": "characters/Cheongpung.md",
      "sha256": "1ff7db76dd1b223a21335347e1b0b9e7ee1f41bb3ae197ed303ba7bc40999623",
      "bytes": 1515
    },
    {
      "path": "characters/Childeuk.md",
      "sha256": "6b46e0a3a40541cf6c56c984f8c009aa7c42c73d6dec2e8e042688043754be24",
      "bytes": 716
    },
    {
      "path": "characters/Hyuk Mujin.md",
      "sha256": "2da6c608b2d464c24b8ffe4388a0c6f16ab678b9af533fabec4066eefc3f1d99",
      "bytes": 5498
    },
    {
      "path": "characters/Jin Mukyung.md",
      "sha256": "6b6b230448d4e0dcab3413e1716b6afa32a2a1a5ceeb1b02649c018a5fff95de",
      "bytes": 1826
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "56e163799f2ffb291c118093825df3fc7592260573a859c283ac0dbf1674fa0a",
      "bytes": 24583
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "d355c2e4928666fc4a721a3340b6e0a07c2d6016ab4be797dcf2ebe97723ace9",
      "bytes": 622
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "b15e6baf1d1ef5763e7f3e0c3b055c264294e0f85803e00e087b53b9ef838a5b",
      "bytes": 29457
    }
  ],
  "estimated_tokens": 29429
}
-->

# Durable State Update — Chapter 154

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 154. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 20 concise items, `open_questions` to at most 8
items, and `temporary_decisions` to at most 8 items. Keep the serialized context
under 16384 UTF-8 bytes. Use only chapter
numbers through 154. `profile_updates` may replace one exact, uniquely occurring
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
  "chapter": 154,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 154,
    "continuity_sources": [154],
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
    "The City Lord's luncheon requirement has concluded; Prince Shangshan's Token was obtained as the Quest Reward, and Zhu Bao is expected at the Jin Family's grand banquet in roughly fifteen days.",
    "Zhu Bao is ten years old, has trained in martial arts daily for three years, is an exceptionally skilled young swordsman personally named Zhu Bao, and admires Jin Taekyung.",
    "Taekyung remains below the Peak realm and cannot use Sword Energy despite defeating Jopil, Jin Baekyang, and Pung Yang.",
    "Hong Jin and Li Feng are pursuing the Shaanxi–Shanxi trade project through Huashan, with Li Feng acting as intermediary and the Seongun Escort Bureau proposed as the base.",
    "Cheongpung is a twenty-year-old Peak master raised by Mae Jonghak, knows several Huashan martial arts, can use the Zaha Divine Technique, obtained the Royal Guard Armor Set, has no martial title yet, and has begun teaching Taekyung and Hyuk Mujin using Mae's training method.",
    "Mae Jonghak remained in deep seclusion at a hidden Huashan residence and had been there at least ten years before the luncheon; Cheongpung came to Huashan at about age three or four rather than being born there.",
    "Huashan was sealed after Mae Jonghak entered the sleeping Sect Leader's quarters, left a dagger and handwritten letter, and disappeared; the search for his residence remains ongoing.",
    "Baek Museong is a first-generation Huashan disciple known as Huashan's Lone Crane and the first of the Three Plum Blossom Elites; he met Cheongpung ten years ago and is traveling with the other Elites to meet him again.",
    "Chulwoo and Eunhyang are Baek Museong's junior disciples and fellow members of the Three Plum Blossom Elites; both are notorious troublemakers who caused trouble with the Black Serpent Sect while traveling.",
    "Li Feng left Huashan after becoming discouraged by Cheongpung's extraordinary talent, not because of his defeat by Gong Ilhyuk.",
    "The identities of the other two members of the Three Hands of Zhongnan remain unknown.",
    "Hong Jin is a eunuch who formerly served the late Emperor, was ordered to assist Prince Shangshan, has served the prince since infancy, and is the power behind the Shanxi Provincial Office.",
    "Gong Ilhyuk leaves the luncheon humiliated and vows revenge against those who rejected and insulted him.",
    "Jin Mukyung lost to Cheongpung four days before the luncheon, then secluded himself to train; the defeat clarified his ambition and strengthened his Sword Energy.",
    "Jin Wikyung returned to the Jin Family after nearly ten days away, faces a large administrative workload, and prefers practical people with flexible thinking over rigid scholars; Hong Jin gave him one thousand silver nyang, prompting an extravagant pro-imperial welcome and a joking rapport between them.",
    "Taekyung failed to force open the Conception and Governor Vessels, suffering slight acupoint damage and a one-point reduction in Sinews and Meridians.",
    "Taekyung now has a private training ground in a newly rebuilt pavilion at the Jin Family; Hyuk Mujin accepted his invitation to train with him and Cheongpung.",
    "Jang Childeuk, formerly a Jin Family servant and now a martial artist directly under Jin Wikyung, has been assigned to guard the largely unused training hall and remains intensely loyal to the family.",
    "The training hall is guarded as a symbol because Founder Jin Muryang allegedly trained beneath its cliff and opened the cliff base with One Strike; Taekyung survived a fall there by slowing himself with a dagger, aided by his physique and toughness stats, and mentioned Taecho Village after waking.",
    "Cheongpung's training based on Mae Jonghak's method has Taekyung and Hyuk Mujin repeatedly climb a steep unnamed winter cliff using the Wall Lizard Technique; Cheongpung rescues Mujin from a fall with the Zaha Divine Technique, and nine more climbs remain after their first successful ascent. Taekyung's Strength, Agility, and Stamina each increase by one during the climb, and the Sword Saint Training: A Secondhand Experience Quest is generated."
  ],
  "continuity_sources": [
    153,
    152
  ],
  "open_questions": [
    "What did Mae Jonghak mean by saying a crane delivered Cheongpung to him?",
    "Why did Mae Jonghak remain hidden at Huashan despite the sect eventually finding his residence?",
    "What are the names and individual identities of the other two members of the Three Hands of Zhongnan?",
    "What is the full title of the wuxia novel beginning with 군림…… that Taekyung read through volume thirty-four?",
    "Was the Emperor's reported suspicion of his younger brother the reason Prince Shangshan was sent to Shanxi, and what danger does the imperial succession pose?",
    "What martial title will Cheongpung eventually acquire?",
    "What circumstances led Hong Jin to become a eunuch and come to the frontier in something like exile?",
    "What is Taecho Village, and why does Taekyung say “again” after landing?"
  ],
  "safe_through": 153,
  "temporary_decisions": [
    "Render 전하 as “His Highness” as the formal royal address and 왕 as “king” when used literally.",
    "Render 초일류 as “advanced First Rate” and 군문 as “military” when describing an affiliation; render 풍운검군 as “Wind-and-Cloud Sword Lord” and 오촌 당숙 as “father's cousin.”",
    "Render 태을미리장 as “Taeeul Miri Palm.”",
    "Render 후배님 and 선배님 as “Junior” and “Senior” in the Gong Ilhyuk exchange.",
    "Render 태사부 as “Grandmaster,” 사숙 as “Martial Uncle,” 자하신공 as “Zaha Divine Technique,” 근위대 as “royal guard,” and 근위대 갑옷 세트 as “Royal Guard Armor Set.”",
    "Render 비무행 as “dueling tour,” 청강검 as “blue-steel sword,” and 광염 as “light-flames.”",
    "Render 검신 as “Sword God,” 검성 as “Sword Saint,” 임독양맥 as “Conception and Governor Vessels,” 기해 as “qi sea,” 근맥 as “Sinews and Meridians,” 사해오호 as “Four Seas and Five Lakes,” and 환골탈태 as “Bone Transformation.”",
    "Render 연무장 as “training ground,” 수련동 as “training hall,” 청석 as “bluestone,” 십팔반병기 as “eighteen traditional weapons,” 찍고 땡 as “touch-and-go method,” 진무량 조사 as “Founder Jin Muryang,” 천응 as “Heavenly Eagle,” 강시 as “jiangshi,” and 태초 마을 as “Taecho Village.”"
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

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 진무경    | **Jin Mukyung**    |
| 혁무진    | **Hyuk Mujin**     |
| 청풍     | **Cheongpung**     |
| 검성     | **Sword Saint**               | Mae Jonghak    |
| 태원진가   | **Jin Family of Taiyuan**        |
| 이류     | **Second Rate**   |
| 일류     | **First Rate**    |
| 절정     | **Peak**          |
| 무인     | **martial artist**                               | Default term                                          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 마교     | **Demonic Cult**                                 |                                                       |
| 은인     | **Benefactor**                               |
| 시스템              | **System**                     |
| 스킬               | **Skill**                      |
| 레벨               | **Level**                      |
| 퀘스트              | **Quest**                      |
| 보상               | **Reward**                     |
| 칭호               | **Title**                      |
| 등급               | **Grade**                      | System/UI field for quest, item, and martial-art classifications; do not use “Rank” here |
| 습득               | **Acquired**                   |
| 헌터      | **Hunter**            |
| 태원     | **Taiyuan**            |
| 화산     | **Huashan**            |
| 칠득이 | **Childeuk** | Jin Family servant. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 금나수 | **grappling technique** | Close-combat wrist-lock technique; rendered descriptively |
| 장칠득 | **Jang Childeuk** | Personal-name form of Childeuk; he is newly appointed as a martial artist directly under Jin Wikyung. |
| 조장 | **Captain** | Hyuk Mujin's address for Taekyung as squad leader. |
| 원단 | **New Year's Day** | The day the Mount Heng Sword Sect will visit Taiyuan. |
| 수련동 | **training hall** | Building located roughly two hundred jang from the training ground. |
| 혈교 | **Blood Cult** | Demonic organization named as a possible source of the intruder. |
| 벽호공 | **Wall Lizard Technique** | Climbing martial art used to scale walls and cliffs. |

## Listed compact profiles

### Cheongpung.md

# Cheongpung (청풍)

- **Safe through:** Chapter 153
- **Aliases:** None
- **Role:** Mysterious young man encountered at Honghwa Inn; an exceptionally young Peak master whose Level Jin Taekyung cannot determine through Qi Sense; the grandson and disciple of Sword Saint Mae Jonghak, who secretly descended from Huashan to seek out and defeat the Ten Dragons and Phoenixes, beginning with Jin Mukyung; he has no martial title yet, naturally opened his Governor Vessel through enlightenment two years ago, has begun teaching Jin Taekyung and Hyuk Mujin using Mae Jonghak's training method, and Prince Shangshan will only accept his autograph after he gains one
- **Personality:** Affable, dreamy, hazy, and childlike in manner, with innocent curiosity, delight in novel public attention, and a martial artist's competitive pride
- **Voice:** Dreamy and hazy, with innocent, polite phrasing
- **Relationships:** Mae Jonghak, the Sword Saint, is his grandfather and martial instructor; Cheongpung came to Huashan at about age three or four rather than being born there, lived with Mae Jonghak at a hidden residence, and secretly left Huashan without his grandfather's knowledge to challenge the Ten Dragons and Phoenixes; Baek Museong met him ten years ago and is now traveling with the Three Plum Blossom Elites to meet him; Li Feng is his Martial Nephew within Huashan's hierarchy; calls Jin Taekyung and Hyuk Mujin Benefactors after they feed him

### Childeuk.md

# Childeuk (칠득이)

- **Safe through:** Chapter 153
- **Aliases:** None
- **Role:** Illiterate Level 15 martial artist and servant of the Jin Family of Taiyuan, directly under Jin Wikyung; newly appointed to guard the training hall and intensely loyal to the family
- **Personality:** Physically strong, diligent, gullible, and intensely excitable; readily interprets praise as recognition of exceptional talent
- **Voice:** Deferential, overeager, and breathless when speaking to Jin Wikyung
- **Relationships:** Servant under Jin Wikyung; assigned to serve Jin Mukyung and Jin Taekyung until removed from meal delivery after a misunderstanding

### Hyuk Mujin.md

# Hyuk Mujin (혁무진)

- **Safe through:** Chapter 153
- **Aliases:** None revealed
- **Role:** First Rate martial artist from a wealthy Taiyuan textile-merchant family; Captain of the Gatekeepers at the Jin Family of Taiyuan; deputy squad leader of White Tiger Hall’s reconnaissance squad; candidate to become the next Master of the Gatekeeper Pavilion; has accepted Jin Taekyung’s invitation to train alongside Taekyung and Cheongpung in Taekyung’s private training ground
- **Personality:** Young, disciplined, suspicious of Jin Taekyung, and openly contemptuous of the family’s disgraced third son; believes loyalty and respectable conduct matter, but is also proud, hungry for glory, and an avid wuxia-novel reader who sometimes mistakes fictional Murim conventions for reality
- **Voice:** Formal and clipped when performing his duties; blunt and moralizing when addressing Taekyung
- **Relationships:** Gatekeeper under the Jin Family; deputy subordinate to Jin Taekyung in the reconnaissance squad; son of the Hyuk Family Textile Shop’s owners, with a younger sibling who removed the need for him to inherit the family business

### Jin Mukyung.md

# Jin Mukyung (진무경)

- **Safe through:** Chapter 151
- **Aliases:** Heaven Shaking Sword; Jin Family Second Young Master
- **Role:** Second son of the Jin Family of Taiyuan; twenty-three-year-old cadet at Heaven’s Gate Temple; a young Peak-level genius swordsman who won the visible exchange with Pung Yang, was then incapacitated by five concealed throwing knives, and survived the battle to recover after Taekyung's intervention; recovered enough from his Internal Injuries to return to the Jin Family of Taiyuan, though he is not yet fully recovered; four days before this chapter, he lost his duel with Cheongpung after roughly three hundred exchanges, secluded himself to train, and sharpened his Sword Energy while resolving to surpass Cheongpung and the other geniuses
- **Personality:** Reserved, terse, and easily irritated by exaggerated praise; glares coldly when Taekyung identifies him
- **Voice:** Quiet and resonant; clipped and blunt in direct speech
- **Relationships:** Taekyung’s older brother and current martial arts instructor; returned to the Jin Family after several years away; three years earlier, he flatly refused seven-year-old Zhu Bao’s request for an autograph

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 144
- **Aliases:** Sleeping Dragon of Shanxi
- **Role:** Modern-world protagonist; recently fired after seven years at his job; C-rank Hunter who defeated eight B-rank Minotaurs and killed a Level 70 B-rank Minotaur Warrior in one blow; First Rate martial artist standing before the Peak realm who now possesses forty-five years of internal energy with the Scorching Yang Qi attribute after fully absorbing the Blazing Flame Divine Pill; youngest son of the Jin Family of Taiyuan; new owner of a two-story detached house in Goyang intended for his family; Qi Sense reaches a seventy-meter radius; possesses one Temporary Strength Pill in his Inventory and has reserved it for a worst-case, life-threatening contingency; Level 61 with 2,100 Fame and 60 unspent stat points, and the Sleeping Dragon of Shanxi Title now grants all stats +15 and Fame +200
- **Personality:** Hungry, self-aware, dryly observant, and willing to take a questionable opportunity when desperate; treats the impossible as a game until the danger becomes undeniable
- **Voice:** First-person, conversational, dryly self-mocking; uses vivid trap-and-prey imagery, game jargon, and occasional profanity
- **Relationships:** Jin Mukyung’s younger brother and current student; son of a deceased father; supports his mother and younger sibling; loves Song Song; has a strained relationship with Lee Seowol, the current Sect Leader of the Mount Heng Sword Sect, whose marriage proposal he has decided to reject

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 145
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

## Korean source

```text
＃154화



중년 무인과 장칠득은 오늘도 하늘을, 아니 절벽을 바라보고 있었다.

“이보게, 장 아우. 혹시 벽호공 익혀 본 적 있나?”

“벽호공이요? 어휴, 저처럼 담이 작은 놈은 엄두도 못 냅니다. 형님은요?”

“오 년 전쯤에 한 번.”

“왜 그만두셨습니까?”

“벽호공 수련을 시작한 지 석 달쯤 됐나? 발을 헛디뎌서 떨어지는 바람에 발목이 부러졌었지.”

“아이고, 높은 곳에서 떨어지셨나 봅니다.”

“겨우 오 장 남짓이었어. 하루도 빠지지 않고 석 달을 수련했는데 발목이 부러진 거야.”

“저런. 아쉽습니다.”

“아쉽다니?”

“혹시 압니까, 계속 익히셨으면 벽호공의 고수가 되셨을지도…….”

“벽호공의 고수? 평생 익힌 검공으로도 이류를 못 벗어나는 내가?”

중년 무인이 피식 웃으며 절벽을 가리켰다.

“무슨 무공이든 무재(武才)가 있어야 고수 소리 듣는 거야. 저 두 사람을 보면서 느끼는 게 없나?”

“확실히 그건 그렇습니다.”

두 사람은 절벽 위를 빠르게 올라가는 두 신형을 응시했다.

볼 것도 없이 오늘도 벽호공 수련에 매진하는 진태경과 혁무진이다.

파파파파팍!

까마득한 위에서 굴러떨어지는 돌멩이과 눈덩이.

지금 이 순간, 두 사람은 같은 생각을 떠올리는 중이었다.

‘저게 사람이야, 도마뱀이야.’

거의 수직으로 이어진 절벽을 오르는 손발에 거침이 없다.

비록 속도의 차이는 꽤 크지만 수련 기간을 생각해 본다면 실로 괄목할 만한 성과였다.

“지금이 며칠째지?”

“어디 보자, 이번이 세 번째 교대니까…… 딱 사흘째입니다.”

“고작 사흘이라. 내가 석 달이 아니라 일 년을 수련했다면 저 정도로 벽호공을 익힐 수 있었을까?”

“…….”

그 질문에 대한 답은 중년 무인도 알고 장칠득도 안다.

잠깐 말이 없던 장칠득이 입을 열었다.

“형님.”

“응?”

“무재가 없는 우린 뭘 할 수 있죠?”

“우린 쓸모가 없어. 육포나 꺼내.”

“옙.”

장칠득은 냉큼 품에서 육포와 술병을 꺼냈다. 태원진가 최고의 꿀 보직이라는 수련동 근무에 빠르게 적응해 나가는 그였다.



* * *



후우웅!

무서운 속도로 떨어지는 바위를, 절벽에 바짝 달라붙어 피했다. 한참 위에서 아쉬운 얼굴로 입맛을 다시는 청풍이 보인다.

‘이럴 줄 알았다, 인마.’

이 짓 한두 번 당하나?

어릴 때부터 공부 머리는 나빠도 몸으로 익히는 거 하나만큼은 타의 추종을 불허하던 나다.

“흐어어억!”

그에 비해 혁무진 저놈은 좀 느린 편이다. 아무래도 지금의 나와는 확실히 수준 차이가 있으니 당연할지도 모르겠다.

나는 한참 밑에서 기어 올라오는 혁무진을 향해 외쳤다.

“무진아, 괜찮냐?”

“아니요!”

“……어, 그래?”

칼답 봐라. 당연히 안 괜찮겠지만 보통은 빈말이라도 괜찮다고 하는데, 혁무진 이놈은 그런 게 없다.

“엄살 부리지 말고 빨리 올라와!”

“온몸에 쥐가 나서 죽겠다고요! 방금도 간신히 피했어요!”

말은 저렇게 해도 제법 잘 따라온다. 이번 수련을 통해 다시 한번 확인했다. 혁무진은 제법 끈기와 무재가 있는 놈이라는 사실을.

“이제 거의 다 왔다. 이 악물고 올라와!”

나는 절벽의 오목한 곳에 몸을 집어넣고 잠시 숨 고르기에 들어갔다.

‘퀘스트 창 오픈.’

띠링.



퀘스트



[검성 수련 간접 체험기]

고수는 수많은 담금질과 망치질 끝에 만들어지는 법.

검성으로부터 혹독한 수련을 받은 청풍은 어린 시절의 기억을 되살려 당신들을 교육시킬 겁니다!



등급 : 절정

제한 : 청풍의 허락을 받은 자

임무 : 절벽 10회 등반 (9/10)

보상 : [벽호공] 습득

 [청풍]이 매우 기뻐합니다

 ???

실패 : 부상 또는 사망

 [청풍]이 매우 슬퍼합니다





이 빌어먹을 절벽을 타기 시작한 지 오늘로 딱 사흘째.

퀘스트 완료까지는 딱 한 번이 남았지만 아직 방심해서는 안 된다.

왜냐하면…….

“은인! 어디 계세요! 고개 좀 내밀어 보세요!”

“싫어! 꺼져!”

“아, 거기 계셨구나! 근처에 던질 만한 게 다 떨어져서 구해 오느라 좀 늦었어요!”

당장이라도 내 얼굴에 바위를 떨구고 싶어 하는 저 사이코패스 때문이지.

첫 번째 절벽 등반도 충분히 힘들었는데, 청풍의 훼방은 회차를 거듭할수록 점점 강도를 더해 가는 중이다.

나는 몸을 바짝 웅크리고 외쳤다.

“그걸 왜 구해 와! 돌 떨어졌으면 그냥 던지질 마!”

“그치만…… 이렇게 하지 않으면, 은인께서 벽호공을 제대로 익히실 수 없는걸요!”

“…….”

미친놈인가. 세상천지에 바위 처맞아 가면서 벽호공 익히는 사람이 몇 명이나 된다고.

기가 차서 말도 안 나오던 와중에 상처투성이 손 하나가 내가 있는 공간으로 쑥 솟구쳤다.

오래전 이곳에서 벽호공을 익히다가 죽은 귀신……은 당연히 아니고 혁무진이다.

“흐어억. 죽겠다.”

진짜 힘들면 말도 안 나온다. 숨이 턱 끝까지 차서 머리는 띵하고 호흡하는 것만으로도 가슴이 뻐근해진다.

그래도 아직 충분히 살 만해 보이는 녀석이 옆자리로 엉금엉금 기어 오더니 다리를 쩍 벌렸다.

“야, 좁잖아.”

“조장님만 좁습니까? 저도 좁습니다.”

“다리를 오므리든가, 옆으로 좀 더 가라. 여긴 기본적으로 일 인석이야.”

“아, 힘들어요. 조장님이 옆으로 가세요. 힘겹게 여기까지 올라온 오른팔한테 너무 야박한 거 아닙니까?”

“오른팔한테는 잘해 주지. 근데 넌 새끼발가락이라 좀 야박하게 굴어도 돼.”

“와, 진짜 이러시깁니까? 그나마 바위 피할 곳이라고는 여기밖에 없는데. 제가 그냥 확 뛰쳐나가서 면상에 바위라도 맞아야 속이 시원하시겠어요?”

나는 정색하고 대답했다.

“말을 왜 그렇게 하냐? 당연히 아니지.”

“오, 조장님이 웬일로…….”

“한동안 속이 갑갑하고 죄책감에 시달릴 거야. 하지만 일 년쯤 지나면 괜찮아지겠지. 십 년쯤 지나면 얼굴도 까먹을 거고.”

“……거, 되게 현실적이시네.”

“원래 인생이 그런 거야, 인마. 그러니까 당장 다리 오므려. 아니면 내가 죄책감 느낄 일이 생길 것 같으니까.”

“넵.”

쩍벌충은 바위에 뚝배기가 깨져도 상관없다. 쩍벌충이니까.

다리를 바짝 오므린 채 숨을 고른 혁무진이 한숨을 내쉬었다.

“아무리 생각해도 미친 것 같습니다.”

“뭐가?”

“이딴 걸 시키는 청풍 저놈도 미친 것 같고, 시킨다고 하는 저도 미친놈 같아요.”

“그런 것치곤 잘하고 있는데?”

“그냥 죽자 살자 하는 거죠.”

“그게 답이지.”

“예?”

“죽자 살자 하는 거. 그게 답이라고. 나중에 정말 죽음이 코앞에 닥치면 지금 이 순간을 후회하게 될걸?”

나는 흐트러진 머리를 질끈 묶으며 말을 이었다.

“아, 그때 좀 더 열심히 했어야 했는데. 뭐 그런 후회 있잖아.”

헌터로 살면서 피똥 쌀 정도로 노력했다고 자부한다. 하지만 그렇게 했어도 남는 게 후회더라. 후회는 늘 늦는다. 그리고 소중한 뭔가를 잃은 후에야 뼈아프게 다가온다.

“네 목숨, 재물, 아니면 사람. 소중한 걸 잃기 싫다면 지금 목숨 걸고 해. 살아 있을 때 죽도록 노력하는 게 죽는 것보다는 낫잖아?”

“어…….”

혁무진이 눈을 동그랗게 뜨고 나를 바라봤다.

“뭔가 경험자처럼 말씀하시네요.”

“왜, 이상하냐?”

“누구 입에서 나온 말이냐에 따라 느낌이 다르잖아요. 제가 보는 조장님은, 으음…….”

“남부럽지 않게 자란 도련님이 할 말은 아니다?”

“굳이 따지면 뭐 그렇죠. 분명히 살면서 소중한 뭔가를 잃어 본 적 없을 것 같은 사람인데, 산전수전 다 겪은 백전노장 같다고 해야 하나?”

이 녀석, 제법 촉이 좋다.

아니, 어쩌면 다른 사람들의 시선에도 그렇게 보이려나?

별다른 말 없이 피식 웃는 나를 혁무진이 미심쩍은 눈빛으로 바라봤다.

“뭡니까, 그 웃음은?”

“그냥 제법이다 싶어서.”

“혹시 조장님, 가짜 아니죠?”

“뭐?”

“이제 와서 꺼내기에는 좀 새삼스러운 이야기긴 한데……. 달라져도 너무 달라졌잖아요. 성격도 그렇고, 무공도 그렇고. 완전 딴사람이 된 것 같다니까요.”

“소문 못 들었어? 태원진가에서 비밀리에 길러 낸 비밀 병기.”

“소문은 소문이죠. 확인 안 된 소문. 조장님이 흥청망청 노는 거 본 사람이 어디 한두 명입니까?”

“너도 그중 하나고?”

“네. 처음에는 인피면구(人皮面具)라도 쓰고 있나 했는데 그건 아닌 것 같고.”

“인피면구? 사람 얼굴 가죽 벗겨서 쓰는 그거?”

“보세요. 이런 것도 처음 듣는 양 되물으시고. 가끔 뜻 모를 말도 자주 하시잖아요.”

“흠.”

그러고 보니 어느 순간부터 의심을 피하는 것에 많이 신경 쓰지 않았다. 주위의 모두가 나를 태원진가의 진태경으로 생각하고 있었으니까. 나도 무림에서의 모습을 내 일부로 받아들인 지 오래였다.

“혹시 조장님이 소설에서나 보던 암중 세력이 내세운 대역, 뭐 그런 거면 지금 말씀해 주세요. 조용히 넘어가 드릴 테니까.”

“이거 어이없는 놈일세. 그럼 당장 보고해야지.”

“저야 뭐 예전 모습보다는 지금이 훨씬 나으니까요. 조장님한테는 목숨 빚도 있고. 헤헤.”

입은 웃고 있지만 농담은 아니다. 은연중에 넘어가는 목울대, 살짝 흔들리는 눈빛이 그 증거다.

나는 잠시 고민하다가 입을 열었다.

“솔직하게 말해 줘?”

“소, 솔직하게?”

“안 그래도 말하고 싶어서 입 근질거렸는데 잘됐지. 장소도 딱 적당하고.”

혁무진이 불안한 표정으로 주위를 살폈다. 딱 두 사람이 엉덩이 붙일 만큼 움푹 들어간 절벽. 때마침 밖으로 얼굴만 내밀면 바위를 떨궈 줄 미친놈도 기다리고 있다.

그야말로 둘이 앉아 있다가 하나가 죽어도 모를 명당이다.

“너 머리 되게 나쁘구나?”

혁무진이 마른침을 꿀꺽 삼켰다.

“조, 조, 조장님. 전 조장님이 어떤 사람이어도 상관없습니다.”

“이미 늦었어.”

“헉! 말 안 할게요! 아까 했던 말 진심이었어요!”

“내가 마교 소속이라고 해도?”

“마교!”

“딱 한 번 말한다. 잘 들어라.”

“못 들은 걸로 하겠습니다. 아니, 안 들을게요!”

새파랗게 질린 혁무진이 귀를 막으려 했지만 내 말이 한발 빨랐다.

“나, 사실 다른 세상에서 왔다.”

“……?”

“만 리를 떨어져 있어도 서로 대화할 수 있고, 뿔이나 날개가 달린 괴물들이 우글거려. 무림으로 치자면 악귀라고 하나?”

“……예?”

“아무튼 그런 세상에서 어쩌다가 여기까지 오게 됐는데, 눈앞에 막 이상한 게 보이더니 레벨 업을 팍! 포인트가 펑! 머릿속에서 띠링띠링띠링!”

“……”

“아무튼 그렇게 무공에 입문한 지는 두세 달쯤 됐지. 일류 고수 수십 명을 발랐고 절정 고수 셋을 잡았고. 자, 그럼 여기서 질문?”

혁무진이 귀를 반쯤 막고 있던 양손을 스르륵 내렸다.

빡침과 안도가 뒤섞인 복잡한 표정이다.

“후우, 그냥 제가 잘못한 걸로 합시다. 됐어요?”

“왜, 사실인데. 안 믿겨?”

“지나가던 개도 안 믿습니다. 내가 진짜 무공만 더 강했어도…….”

따악!

투덜거리는 녀석의 뒤통수를 후려갈겨 준 다음, 자리에서 일어났다. 진실이지만 진실 같지 않은 이야기다.

물론 나 스스로도 혁무진의 이런 반응을 예상하고 있었기에 말한 것이다.

다른 세상에서 왔다니, 누가 들어도 황당한 이야기 아닌가?

“뇌반업? 포인두? 내참, 말을 말아야지. 제가 조장님한테 뭘 기대했는지 모르겠습니다.”

“뭘 기대했는데? 마교? 혈교?”

“아, 쫌! 그만 좀 하세요!”

자리에서 일어나는 혁무진의 어깨를 잡아챘다. 다음 순간 살벌한 파공음과 함께 성인 남성 키만 한 바위가 스쳐 지나갔다.

“조심해라. 아직 갈 길 멀다.”

나는 녀석을 등을 툭툭 두드려 주고 다시 절벽을 오르기 시작했다. 남은 정상까지는 이제 고작 절반이었다.



* * *



나와 혁무진이 마침내 정상에 오른 순간, 축포처럼 시스템 알림이 터져 나왔다.

띠링. 띠링. 띠링!



- 절벽 10회 등반(10/10)

- 퀘스트를 성공적으로 완료했습니다!

- 새로운 무공, [벽호공]이 활성화됩니다!

- 예상을 뛰어넘는 훌륭한 성과를 거두었으므로 추가 보상이 주어집니다!

- 레벨 업!

- 스탯, 스킬 포인트를 각각 10포인트씩 획득합니다!

- 칭호, [초보 수련자]가 [중급 수련자]로 강화됩니다!

- 변경된 사항은 해당 시스템 창을 열어 확인, 적용시켜 주시기 바랍니다.



청풍이 우리를 향해 활짝 웃었다.

“와아, 이걸 진짜 해냈네요!”

“……그게 무슨 뜻입니까?”

“혹시.”

이 새끼 설마? 우리 둘의 날카로운 눈빛에 청풍이 고개를 저었다.

“별건 아니에요. 전 보름이나 걸렸거든요. 이렇게 빨리 끝내실 줄은 몰라서.”

“보름 말입니까?”

되물은 혁무진이 얼떨떨한 기색으로 나를 바라봤다.

청풍이 누구인가, 검성의 후인이자 진무경을 꺾은 절정 고수다. 그보다 빠른 성취를 이뤘다는 사실이 믿기지 않겠지.

하지만…….

“뭘 좋아해, 인마. 나이대가 다른데. 그렇죠?”

“별로 어리지도 않았어요. 열 살이나 먹었을 때니까!”

“……보통은 열 살밖에 아닌가?”

청풍은 해맑게 웃으며 그때 그 시절을 회상했다.

“그때는 낙안봉(落雁峰)에서 올라갔다가 떨어지는 게 일상이었죠. 참 재밌었는데.”

“낙안봉이요?”

“화산에 있는 봉우리예요. 높이는 오백 장을 가뿐히 넘기는 정도? 아, 물론 저도 끝까지 올라갈 수 있었던 건 열여덟부터였어요.”

“…….”

“…….”

15세 관람 등급 영화도 못 보는 나이 아니냐?

초등학교 3학년이면 급식충이라고 하기에도 뭣하다.

‘난 저 나이 때 학교 운동장에 있는 정글짐 타고 놀았는데…….’

청풍 저놈은 화산 산봉우리를 타고 놀았구나.

역시 대륙, 스케일이 다르다.

“어쨌든 두 분 다 너무너무 고생하셨습니다. 대단한 성과를 거두셨어요!”

혼자 신나게 박수를 친 청풍이 말을 이었다.

“그래서 말인데요…….”

뭔가 불길함을 느낀 혁무진이 황급히 나섰다.

“아냐, 잠깐만. 잠깐만 기다려 봐요.”

“제가 더 재밌는 수련을 많이 알고 있거든요.”

“야! 잠깐만 기다려 보라고!”

혁무진이 고함과 함께 달려들었지만 이미 늦었다. 금나수로 가볍게 녀석을 제압한 청풍이 씩씩하게 외쳤다.

“우리 다 같이 힘내 봐요!”

띠링.



- [청풍]은 당신의 뛰어난 성과에 기분이 한껏 고양되었습니다!

- 특별 보상으로 연계 퀘스트, [검성 수련 간접 체험기-2]가 생성되었습니다!



“야, 이 새끼야! 당장 팔 안 놔!”

혁무진의 고함을 들으면서 문득 드는 의문이 있었다.

‘이거, 연계 퀘스트가 몇 개나 있는 거지?’

하나는 확실하다.

저 청풍이 고작 2에서 멈출 리는 없다는 것.

‘오지게 굴리겠군.’

나는 꽥꽥 소리를 질러 대는 혁무진의 목소리를 뒤로하고 하늘을 바라봤다. 드넓은 하늘이 푸르기 그지없다. 공기는 서늘하고, 거대한 날개를 활짝 펼친 매 몇 마리가 하늘을 부유한다.

원단이 열흘 앞으로 다가온 시점이었다.
```

## Final English reading copy

```markdown
# Chapter 154

The middle-aged martial artist and Jang Childeuk were staring at the sky again today—or rather, at the cliff.

“Say, Brother Jang. Have you ever learned the Wall Lizard Technique?”

“The Wall Lizard Technique? Good heavens, someone as timid as me would never even dare try it. What about you, hyung?”

“Once, about five years ago.”

“Why did you quit?”

“Had it been about three months since I started training in it? I misstepped and fell, and broke my ankle.”

“Oof. You must have fallen from somewhere pretty high.”

“Barely five jang or so. I trained for three months without missing a single day, and still broke my ankle.”

“That’s a shame.”

“A shame?”

“Who knows? If you’d kept learning, you might have become a master of the Wall Lizard Technique…”

“A master of the Wall Lizard Technique? Me? I can’t even break out of Second Rate with the sword techniques I’ve practiced all my life.”

The middle-aged martial artist let out a quiet laugh and pointed at the cliff.

“Whatever the martial art, you need talent to be called a master. Don’t you feel anything when you look at those two?”

“That’s certainly true.”

The two men watched the two figures swiftly climbing the cliff.

There was no mistaking them. Jin Taekyung and Hyuk Mujin were dedicating themselves to Wall Lizard Technique training again today.

*Thud-thud-thud-thud!*

Stones and snowballs came tumbling down from far above.

At that very moment, both men were thinking the same thing.

*Are those people or lizards?*

Their hands and feet moved without hesitation as they climbed the nearly vertical cliff.

The difference in speed between them was considerable, but considering how long they had been training, their progress was truly remarkable.

“How many days has it been now?”

“Let’s see. This is our third shift, so… exactly our third day.”

“Only three days. If I had trained for a year instead of three months, could I have learned the Wall Lizard Technique to that extent?”

“…”

The answer to that question was known to both the middle-aged martial artist and Jang Childeuk.

After a brief silence, Childeuk spoke.

“Hyung.”

“Hmm?”

“What can people without martial talent do?”

“We’re useless. Get out the jerky.”

“Yes, sir.”

Jang Childeuk quickly pulled out some jerky and a bottle of liquor from inside his robes. He was adapting rapidly to his post guarding the training hall—the Jin Family of Taiyuan’s cushiest assignment.

* * *

*Whoooosh!*

I pressed myself tightly against the cliff and dodged the boulder plummeting downward at terrifying speed. Far above, I could see Cheongpung looking disappointed as he smacked his lips.

*I knew this would happen, you bastard.*

As if this were the first or second time I’d been subjected to this.

I might have been bad at book learning when I was young, but when it came to learning through my body, I had been unrivaled.

“Haaaargh!”

Hyuk Mujin, on the other hand, was a little slower. Compared to me as I was now, there was a clear difference in level, so perhaps it was only natural.

I shouted toward Hyuk Mujin, who was crawling up from far below.

“Mujin, you okay?”

“No!”

“...Oh. Right.”

What a brutally quick answer.

Of course he wasn’t okay, but most people would say they were fine even as empty courtesy. Hyuk Mujin had no such habit.

“Quit whining and get up here!”

“My entire body is cramping! I barely dodged that one just now!”

For all his complaining, he was keeping up fairly well. This training had confirmed it once again: Hyuk Mujin had a decent amount of persistence and martial talent.

“We’re almost there. Grit your teeth and climb!”

I wedged myself into a hollow in the cliff and took a moment to catch my breath.

*Open the Quest window.*

*Ding.*

> **System**
>
> **Quest**
>
> **Sword Saint Training: A Secondhand Experience**
>
> A master is forged through countless rounds of tempering and hammering.
>
> Cheongpung, who received harsh training from the Sword Saint, will revive his childhood memories and put you through training!
>
> **Grade:** Peak
>
> **Restriction:** Those who have Cheongpung’s permission
>
> **Mission:** Climb the cliff 10 times (9/10)
>
> **Reward:** Acquire **Wall Lizard Technique**
>
> **Cheongpung** is extremely pleased.
>
> **???**
>
> **Failure:** Injury or death
>
> **Cheongpung** is extremely saddened.

Today marked exactly three days since we started climbing this damned cliff.

Only one climb remained before the Quest was complete, but I still couldn’t let my guard down.

Because of this psychopath who looked like he wanted to drop a boulder straight onto my face at any moment.

The first climb had been hard enough, but Cheongpung’s interference had grown more intense with every round.

I curled up as tightly as I could and shouted.

“Benefactor! Where are you? Show me your head!”

“No! Get lost!”

“Oh, there you are! I ran out of things nearby that were good for throwing, so I was delayed while I went to find more!”

“What do you mean, find more? If you ran out of rocks, just don’t throw anything!”

“But… if I don’t do this, you won’t be able to properly learn the Wall Lizard Technique, Benefactor!”

“…”

Was this guy insane?

How many people in the world learned the Wall Lizard Technique while getting pelted with rocks?

Just as I was rendered speechless by the sheer absurdity of it, a battered hand shot up into the hollow where I was hiding.

It wasn’t the hand of some ghost that had died here long ago while learning the Wall Lizard Technique.

Naturally, it was Hyuk Mujin.

“Haaaargh. I’m dying.”

When you were truly exhausted, you couldn’t even speak. You got so out of breath that your head rang, and even breathing made your chest ache.

Even so, Mujin still looked like he had plenty of life left in him. He crawled over beside me, then spread his legs wide.

“Hey, it’s cramped.”

“Am I the only one cramped, Captain? I’m cramped too.”

“Pull your legs in or move over. This is basically a one-person seat.”

“Ah, I’m too tired. You move over, Captain. Aren’t you being a little too harsh on your right-hand man after he worked so hard to get up here?”

“I’m nice to my right arm. But you’re my little toe, so I can afford to be a little harsh.”

“Wow, you’re really going to be like this? This is the only place where we can avoid the rocks. Would it make you feel better if I just jumped out and got one straight to the face?”

I answered with a perfectly serious expression.

“Why would you say that? Of course not.”

“Oh, wow. What’s gotten into you all of a sudden, Captain…”

“I’d feel stifled and guilty for a while. But after a year, I’d be fine. After ten years, I’d have forgotten your face.”

“...You’re awfully realistic.”

“That’s life, punk. Now pull your legs in. Otherwise, you might give me something to feel guilty about.”

“Yes, sir.”

Manspreaders could get their skulls cracked by a rock for all I cared. That was what they got for manspreading.

Hyuk Mujin pulled his legs tightly together, caught his breath, and sighed.

“No matter how I think about it, this is insane.”

“What is?”

“Cheongpung is insane for making us do this, and I’m insane for agreeing to do it.”

“You’re doing pretty well for someone who thinks it’s insane.”

“I’m just fighting like my life depends on it.”

“That’s the answer.”

“What?”

“Going at it like it’s do or die. That’s the answer. Later, when death really is staring you in the face, you’ll regret this moment.”

I tied back my disheveled hair and continued.

“Ah, I should’ve worked harder back then. You know, that kind of regret.”

I prided myself on having worked so hard as a Hunter that I had practically shit blood. But even after doing all that, regret was what remained.

Regret always came too late. It only struck with bone-deep pain after you had lost something precious.

“Your life, your wealth, or someone you care about. If you don’t want to lose something precious, put your life on the line now. Working yourself to death while you’re alive is still better than actually dying, isn’t it?”

“Uh…”

Hyuk Mujin stared at me with round eyes.

“You’re talking like someone who’s been through it.”

“Why? Is that strange?”

“Words feel different depending on whose mouth they come from. The Captain I know is, um…”

“Not exactly someone who should be saying that, having grown up as a young master with nothing to envy?”

“If I had to put it that way, then yes. You look like someone who’s never lost anything precious in his life, but you talk like a battle-hardened veteran who’s been through every possible hardship.”

This guy had pretty good instincts.

Or maybe that was how I looked to everyone else, too.

I simply let out a quiet laugh without answering. Hyuk Mujin studied me suspiciously.

“What’s with that laugh?”

“I was just thinking you’re pretty perceptive.”

“Captain, you’re not a fake, are you?”

“What?”

“It’s a little late to bring this up, but… you’ve changed too much. Your personality, your martial arts—everything. You’re like a completely different person.”

“Haven’t you heard the rumors? I’m a secret weapon secretly raised by the Jin Family of Taiyuan.”

“Rumors are just rumors—unverified ones. Plenty of people saw you carousing and wasting your time, Captain.”

“You were one of them?”

“Yes. At first, I thought you might be wearing a human-skin mask, but that doesn’t seem to be it.”

“A human-skin mask? The kind where you peel the skin off someone’s face and wear it?”

“See? You ask again as if you’re hearing about it for the first time. You also say things that make no sense all the time.”

“Hmm.”

Come to think of it, at some point I had stopped worrying so much about avoiding suspicion. Everyone around me thought I was Jin Taekyung of the Jin Family of Taiyuan. I had also long since accepted my Murim self as part of who I was.

“If I’m right, and you’re some kind of double put forward by a shadowy organization like the ones in wuxia novels, tell me now. I’ll let it slide quietly.”

“What an absurd thing to say. Then you should report me immediately.”

“Well, I like you much better now than I did before. And I owe you my life. Hehe.”

His lips were smiling, but it wasn’t a joke. The subtle movement of his throat as he swallowed and the slight tremor in his eyes were proof.

I thought for a moment, then opened my mouth.

“Want me to tell you honestly?”

“H-honestly?”

“I’ve been itching to tell someone anyway, so this works out. And the location is perfect.”

Hyuk Mujin glanced around anxiously.

The hollow in the cliff was just large enough for two people to plant their backsides. As luck would have it, the lunatic who would drop a rock on us the moment we stuck our faces outside was waiting nearby, too.

It was the perfect place for two people to sit until one of them died without anyone ever knowing.

“You really are stupid, aren’t you?”

Hyuk Mujin swallowed hard.

“C-C-Captain. I don’t care who you are.”

“Too late.”

“Gasp! I won’t say anything! I meant what I said earlier!”

“What if I told you I belonged to the Demonic Cult?”

“The Demonic Cult!”

“I’m only going to say this once. Listen carefully.”

“I’ll pretend I didn’t hear it. No, I won’t listen!”

Hyuk Mujin’s face turned deathly pale as he tried to cover his ears, but my words came a moment faster.

“I’m actually from another world.”

“...?”

“People can talk to each other even when they’re ten thousand li apart, and monsters with horns or wings roam everywhere. If you put it in Murim terms, I suppose you’d call them evil spirits.”

“...What?”

“Anyway, somehow I ended up here from that kind of world. Then strange things started appearing before my eyes, and suddenly—Level Up! Bam! Points! Boom! Ding-ding-ding-ding inside my head!”

“…”

“Anyway, I only entered the world of martial arts two or three months ago. I’ve wiped the floor with dozens of First Rate masters and taken down three Peak masters. So, any questions?”

Hyuk Mujin slowly lowered the hands that had been half-covering his ears.

His expression was complicated, a mixture of irritation and relief.

“Whew. Let’s just say I was wrong. Happy now?”

“Why? It’s the truth. You don’t believe me?”

“Not even a stray dog would believe that. If only my martial arts were stronger…”

*Smack!*

After smacking him on the back of the head, I stood up.

It was a true story, but it didn’t sound true.

Of course, I had expected Hyuk Mujin to react this way. That was precisely why I had told him.

Someone coming from another world? Anyone would think that was ridiculous.

“Nevel-up? Poin-two? Good grief, I should just stop talking. I don’t know what I expected from you, Captain.”

“What did you expect? The Demonic Cult? The Blood Cult?”

“Oh, come on! Just stop!”

I grabbed Hyuk Mujin by the shoulder as he stood up. The next instant, a murderous shriek of displaced air filled the space, and a boulder as tall as a grown man shot past us.

“Watch yourself. We still have a long way to go.”

I patted him on the back and started climbing the cliff again.

We were only halfway to the summit.

* * *

The moment Hyuk Mujin and I finally reached the summit, System notifications burst forth like celebratory cannon fire.

*Ding. Ding. Ding.*

> **System**
>
> - **Cliff climb:** 10 times (10/10)
>
> - Quest successfully completed!
>
> - New martial art, **Wall Lizard Technique**, is now activated!
>
> - Because you achieved outstanding results that exceeded expectations, you will receive an additional reward!
>
> - Level Up!
>
> - You have acquired 10 Stat Points and 10 Skill Points!
>
> - The Title **Beginner Trainee** has been upgraded to **Intermediate Trainee**!
>
> - Open the relevant System window to check and apply the changes.

Cheongpung beamed at us.

“Wow! You really did it!”

“...What’s that supposed to mean?”

“By any chance—”

*This bastard. Don’t tell me…*

At the sharp look the two of us gave him, Cheongpung shook his head.

“It’s nothing. It took me fifteen days, you see. I didn’t expect you to finish so quickly.”

“Fifteen days?”

Hyuk Mujin repeated the number, then stared at me in disbelief.

Who was Cheongpung? The Sword Saint’s successor, a Peak master who had defeated Jin Mukyung. It was only natural that Mujin couldn’t believe we had achieved this faster than he had.

But…

“What are you so happy about, punk? We’re not the same age. Right?”

“I wasn’t even that young! I was already ten years old!”

“...Isn’t ten usually considered young?”

Cheongpung smiled brightly as he reminisced about those days.

“Back then, climbing up Falling Goose Peak and falling back down was part of my daily routine. It was so much fun.”

“Falling Goose Peak?”

“It’s a peak on Huashan. It’s comfortably more than five hundred jang high. Oh, of course, I couldn’t climb all the way to the top until I was eighteen.”

“…”

“…”

Wasn’t he too young even to watch a movie rated fifteen-plus?

At that age, he would’ve only been in third grade—barely old enough to count as a snot-nosed schoolkid.

*When I was that age, I was playing on the jungle gym in the school playground…*

That bastard Cheongpung had been playing on the mountain peaks of Huashan.

As expected of the continent. The scale was completely different.

“Anyway, you both worked incredibly hard. You achieved something amazing!”

Cheongpung clapped excitedly all by himself, then continued.

“So, about that…”

Sensing something ominous, Hyuk Mujin hurriedly cut in.

“No. Hold on. Wait just a second.”

“I know lots of other fun training exercises.”

“Hey! I said wait a second!”

Hyuk Mujin lunged at him with a shout, but it was already too late. Cheongpung effortlessly subdued him with a grappling technique and called out energetically,

“Let’s all give it our best!”

*Ding.*

> **System**
>
> - **Cheongpung** is in extremely high spirits over your outstanding achievement!
>
> - As a special reward, the linked Quest **Sword Saint Training: A Secondhand Experience—2** has been generated!

“You bastard! Let go of my arm right now!”

As I listened to Hyuk Mujin shout, a question suddenly occurred to me.

*How many of these linked Quests are there?*

One thing was certain.

There was no way Cheongpung would stop at a measly two.

*He’s going to work us into the ground.*

I left Hyuk Mujin’s shrill shouting behind and looked up at the sky.

The vast sky was an intense blue. The air was cool, and several hawks floated overhead with their enormous wings spread wide.

New Year’s Day was ten days away.
```
