<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0153.txt",
      "sha256": "353d877d8407b864ff65a29eeb8201640c02774f63df370b45e96e4655e2002f",
      "bytes": 17746
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "7d0ef2afcbbbee6f01a137d207aa9fb6a7fb78c788b9f486a82add4a197666d4",
      "bytes": 6173
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "c35aeee0fd8678eead8a8c42a325c3490690bfddf5ddb78b0e300df207561bb0",
      "bytes": 35104
    },
    {
      "path": "characters/Cheongpung.md",
      "sha256": "b8d5a7a5b7704ed07842b03c2ee23011a63f8898f60fab07c5cbdaf038c620e9",
      "bytes": 1515
    },
    {
      "path": "characters/Childeuk.md",
      "sha256": "7c0c24d38a7e084ae5e2652a5c14f902c8b6d65965476d4e677369c11529d1d0",
      "bytes": 716
    },
    {
      "path": "characters/Hyuk Mujin.md",
      "sha256": "5ce1c79dcd4907379543ec7cd0d5c094eee8807fd8a55d67ab3dcbe4116bde8e",
      "bytes": 5498
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "d9748115c5305671ceba018506a87eba2ea680700fa2b8f911fdc2d9de7b69b9",
      "bytes": 29248
    }
  ],
  "estimated_tokens": 28672
}
-->

# Durable State Update — Chapter 153

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 153. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 20 concise items, `open_questions` to at most 8
items, and `temporary_decisions` to at most 8 items. Keep the serialized context
under 16384 UTF-8 bytes. Use only chapter
numbers through 153. `profile_updates` may replace one exact, uniquely occurring
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
  "chapter": 153,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 153,
    "continuity_sources": [153],
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
    "The training hall is guarded as a symbol because Founder Jin Muryang allegedly trained beneath its cliff and opened the cliff base with One Strike; Taekyung survived a fall there by slowing himself with a dagger, aided by his physique and toughness stats, and mentioned Taecho Village after waking."
  ],
  "continuity_sources": [
    152,
    151
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
  "safe_through": 152,
  "temporary_decisions": [
    "Render 전하 as “His Highness” as the formal royal address and 왕 as “king” when used literally.",
    "Render 초일류 as “advanced First Rate” and 군문 as “military” when describing an affiliation; render 풍운검군 as “Wind-and-Cloud Sword Lord” and 오촌 당숙 as “father's cousin.”",
    "Render 태을미리장 as “Taeeul Miri Palm.”",
    "Render 후배님 and 선배님 as “Junior” and “Senior” in the Gong Ilhyuk exchange.",
    "Render 태사부 as “Grandmaster,” 사숙 as “Martial Uncle,” 자하신공 as “Zaha Divine Technique,” 근위대 as “royal guard,” and 근위대 갑옷 세트 as “Royal Guard Armor Set.”",
    "Render 비무행 as “dueling tour,” 청강검 as “blue-steel sword,” and 광염 as “light-flames.”",
    "Render 검신 as “Sword God,” 검성 as “Sword Saint,” 임독양맥 as “Conception and Governor Vessels,” 기해 as “qi sea,” 근맥 as “Sinews and Meridians,” 사해오호 as “Four Seas and Five Lakes,” and 환골탈태 as “Bone Transformation.”",
    "Render 연무장 as “training ground,” 수련동 as “training hall,” 청석 as “bluestone,” 십팔반병기 as “eighteen traditional weapons,” 찍고 땡 as “touch-and-go method,” 진무량 조사 as “Founder Jin Muryang,” 천응 as “Heavenly Eagle,” 강시 as “jiangshi,” 혈교 as “Blood Cult,” and 태초 마을 as “Taecho Village.”"
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

## Exact glossary matches

| 무림     | **Murim**          |
| 혁무진    | **Hyuk Mujin**     |
| 청풍     | **Cheongpung**     |
| 검성     | **Sword Saint**               | Mae Jonghak    |
| 화산파    | **Huashan**                      |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 검기     | **Sword Energy**                                 | When functioning as projected weapon qi               |
| 가주     | **Family Head**                              |
| 소가주    | **Lesser Family Head**                       |
| 은인     | **Benefactor**                               |
| 상태               | **Status**                     |
| 퀘스트              | **Quest**                      |
| 체력               | **Stamina**                    |
| 민첩               | **Agility**                    |
| 화산     | **Huashan**            |
| 귀가      | **your family**                                                 |
| 대협      | **Great Hero** or **Sir** depending tone                        |
| 소협      | **Young Hero**                                                  |
| 공자      | **Young Master**                                                |
| 칠득이 | **Childeuk** | Jin Family servant. |
| 삼공자 | **Third Young Master** | Title used for Jin Taekyung. |
| 장칠득 | **Jang Childeuk** | Personal-name form of Childeuk; he is newly appointed as a martial artist directly under Jin Wikyung. |
| 벽곡단 | **fasting pills** | Food-substitute pills found in the hidden cave where Cheol trained. |
| 북망산 | **Mount Beimang** | Mountain associated with burial grounds; used as a threat to send someone to their death. |
| 조장 | **Captain** | Hyuk Mujin's address for Taekyung as squad leader. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 시진 | **shichen** | Traditional time unit of approximately two hours. |
| 고원 | **Gaoyuan** | Plateau region in northern Shanxi. |
| 자하신공 | **Zaha Divine Technique** | Huashan internal-energy technique used by Cheongpung. |
| 강시 | **jiangshi** | Reanimated corpse from folklore; Childeuk and Hong mistakenly identify Taekyung as one. |

## Listed compact profiles

### Cheongpung.md

# Cheongpung (청풍)

- **Safe through:** Chapter 151
- **Aliases:** None
- **Role:** Mysterious young man encountered at Honghwa Inn; an exceptionally young Peak master whose Level Jin Taekyung cannot determine through Qi Sense; the grandson and disciple of Sword Saint Mae Jonghak, who secretly descended from Huashan to seek out and defeat the Ten Dragons and Phoenixes, beginning with Jin Mukyung; he has no martial title yet, naturally opened his Governor Vessel through enlightenment two years ago, has begun teaching Jin Taekyung and Hyuk Mujin using Mae Jonghak's training method, and Prince Shangshan will only accept his autograph after he gains one
- **Personality:** Affable, dreamy, hazy, and childlike in manner, with innocent curiosity, delight in novel public attention, and a martial artist's competitive pride
- **Voice:** Dreamy and hazy, with innocent, polite phrasing
- **Relationships:** Mae Jonghak, the Sword Saint, is his grandfather and martial instructor; Cheongpung came to Huashan at about age three or four rather than being born there, lived with Mae Jonghak at a hidden residence, and secretly left Huashan without his grandfather's knowledge to challenge the Ten Dragons and Phoenixes; Baek Museong met him ten years ago and is now traveling with the Three Plum Blossom Elites to meet him; Li Feng is his Martial Nephew within Huashan's hierarchy; calls Jin Taekyung and Hyuk Mujin Benefactors after they feed him

### Childeuk.md

# Childeuk (칠득이)

- **Safe through:** Chapter 152
- **Aliases:** None
- **Role:** Illiterate Level 15 martial artist and servant of the Jin Family of Taiyuan, directly under Jin Wikyung; newly appointed to guard the training hall and intensely loyal to the family
- **Personality:** Physically strong, diligent, gullible, and intensely excitable; readily interprets praise as recognition of exceptional talent
- **Voice:** Deferential, overeager, and breathless when speaking to Jin Wikyung
- **Relationships:** Servant under Jin Wikyung; assigned to serve Jin Mukyung and Jin Taekyung until removed from meal delivery after a misunderstanding

### Hyuk Mujin.md

# Hyuk Mujin (혁무진)

- **Safe through:** Chapter 151
- **Aliases:** None revealed
- **Role:** First Rate martial artist from a wealthy Taiyuan textile-merchant family; Captain of the Gatekeepers at the Jin Family of Taiyuan; deputy squad leader of White Tiger Hall’s reconnaissance squad; candidate to become the next Master of the Gatekeeper Pavilion; has accepted Jin Taekyung’s invitation to train alongside Taekyung and Cheongpung in Taekyung’s private training ground
- **Personality:** Young, disciplined, suspicious of Jin Taekyung, and openly contemptuous of the family’s disgraced third son; believes loyalty and respectable conduct matter, but is also proud, hungry for glory, and an avid wuxia-novel reader who sometimes mistakes fictional Murim conventions for reality
- **Voice:** Formal and clipped when performing his duties; blunt and moralizing when addressing Taekyung
- **Relationships:** Gatekeeper under the Jin Family; deputy subordinate to Jin Taekyung in the reconnaissance squad; son of the Hyuk Family Textile Shop’s owners, with a younger sibling who removed the need for him to inherit the family business

## Korean source

```text
＃153화



“그러니까…….”

장칠득이 힘겹게 말을 이었다.

“수련 중이셨다고요?”

“네.”

“혹시 벽호공(壁虎功)을 익히고 계셨던 겁니까?”

“저도 잘은 모르겠는데 일단 그런 것 같아요.”

벽호공. 무협 소설에서 많이 봤다.

도마뱀이 벽을 타는 모습에서 창안된 무공이라던가?

현실에 존재하는 스포츠인 클라이밍(Climbing)과 비슷하지만 다른 점이 딱 두 가지가 있다.

첫째, 클라이밍과는 달리 공력을 사용한다.

둘째, 안전장치가 없다.

‘역시 무림이야, 빠꾸가 없지.’

떨어지면 골로 가는, 그야말로 상남자의 무공이다.

내가 고개를 끄덕이자 두 사람이 귀신 바라보듯 나를 쳐다봤다.

“이 높이에서요?”

“그게 됩니까?”

“되던데요.”

처음 청풍의 말을 들었을 때는 나도 무슨 미친 소린가 했다. 그런데 하니까 되더라.

지금까지 시도해 보지 않아서 비현실적으로 느껴졌을 뿐, 내 육신은 이미 초인의 영역에 들었다고 해도 과언이 아니다.

“아이고, 삼공자님. 이러다가 큰일이라도 나면 어쩌려고 그러십니까!”

중년 아재가 호들갑을 떨며 내 몸에 묻은 먼지를 툭툭 털어 주었다.

한 3분 전까지만 하더라도 태초 마을에서 온 강시 취급 하더니, 지금은 삼대독자 아들 대하듯 조심스럽다.

“자자, 수련은 이쯤 하시고 처소로 돌아가시는 게 좋을 것 같습니다.”

“왜요?”

“왜라니요! 이번에는 운이 좋았기에 망정이지, 한 번 더 떨어지셨다가는 정말 돌아가실지도 모릅니다.”

나는 손을 내저었다.

“괜찮아요. 한두 번도 아니고.”

“예?”

“지금이 벌써 다섯 번짼데요. 뭘 새삼스럽게.”

“다섯…… 번이요?”

“네. 다섯 번.”

떨리는 눈빛이 나와 가파른 절벽을 번갈아 바라본다.

“도, 도대체 어떻게 아직 살아 계신 겁니까?”

“괜찮아요. 열 번도 넘게 떨어진 놈도 있으니까.”

“……?”

“……?”

“슬슬 한 번 더 떨어질 때가 됐는데…… 아, 저기 온다.”

나는 높이 솟은 절벽 한군데를 가리켰다. 점점 커져 가는 검은 점 하나와 찢어지는 비명이 뒤를 이었다.

“끼아아아아악! 조오오자아앙!”

두 사람이 입을 딱 벌렸다.

“세상에. 정말 한 명 더 있었네.”

“저건 누굽니까?”

“제 오른팔, 아니 새끼발가락이요.”

“예? 그게 무슨.”

“아니, 그 전에 당장 구해 줘야 하는 것 아닙니까?”

“구해요? 저걸?”

나는 고개를 가로저었다.

혁무진도 신체 건장한 성인 남성이다. 저 높이에서 추락하는 녀석을 받아 들었다가는 어디 한군데 부러지는 정도로 안 끝난다.

“그냥 내버려 두세요. 괜히 끼어들었다가 다치지 마시고.”

두 사람이 비명을 내질렀다.

“떨어진다! 떨어진다!”

“이대로 두면 죽을 겁니다!”

“쟤 안 죽어요.”

그랬으면 이미 열 번도 더 죽었지.

하지만 혁무진에게는 동아줄이 있다. 언제나 한 끗 차이로 그를 구해 주는 튼튼한 동아줄이.

“끼아아아악!”

추락하는 혁무진의 비명이 시시각각 가까워져 마침내 경악한 표정조차 생생하게 보인 그 순간, 저 위에서 빛줄기가 번쩍였다.

유성(流星)처럼 빠르게 급강하하는 그것은 은은한 자줏빛으로 빛나고 있었다.

“저, 저게…….”

“뭡니까?”

내가 짤막하게 대답했다.

“자하신공.”

정확히는 자하신공을 끌어 올린 누군가지.

두 사람에게는 보이지 않겠지만, 내 눈에는 자하신공 특유의 자색 기운에 휩싸인 청풍이 똑똑히 보였다.

녀석은 입이 찢어져라 웃고 있다.

“우와아아아아!”

“…….”

저놈 저거 신난 거 봐라.

그러나 살짝 맛이 간 성격과는 별개로 능력 하나만큼은 넘사벽이다. 나는 이어지는 광경에 혀를 내둘렀다.

‘어떻게 저게 가능하지?’

화살처럼 쏘아진 청풍은 눈 깜짝할 시간 만에 혁무진의 허리를 낚아챘다.

그리고 급속도로 가까워진 지면을 향해 손바닥을 내밀었다.

팡! 퍼버벙!

한 번, 두 번, 세 번…….

압축된 공기가 터져 나가는 소리와 함께 바닥이 푹푹 파인다.

보이지 않는 거인이 주먹으로 내리친다면 이렇게 될까?

청풍이 일장(一掌)을 내지를 때마다 얼어붙은 땅이 뒤집히고 그 반발력으로 추락하던 신형이 허공에 멈춘다. 이내 청풍의 발이 사뿐히 땅을 밟았다.

“휴, 이번에도 재밌었다. 그렇죠?”

이미 혼절한 혁무진이 신음을 내뱉었다.

“흐어, 흐어어어.”

“역시, 좋아하실 줄 알았어요.”

“…….”

도대체 어딜 봐서?

즐겁게 웃으며 혁무진을 내려놓은 청풍이 내게 알은체를 해 왔다.

“엇, 은인! 아직 여기 계셨네요?”

“떨어졌거든요. 누구 덕분에.”

나는 청풍을 지그시 노려봤다.

사실 지금까지 정상에 오를 기회가 몇 번이나 있었다. 문제는 청풍이라는 놈이 보통 정신 상태의 소유자가 아니라는 것이지.

“헤헤, 제 덕분이라고 해 주시니 기분이 좋아지네요.”

“닥쳐! 당신이 위에서 훼방만 안 놨어도 진작 올라왔어!”

“헉! 진정하세요, 은인!”

“진정? 그런 말은 돌 굴리기 전에 했어야지!”

생각해 봐라.

맨손으로 백여 장이 훌쩍 넘는 절벽을 기어오르는 것도 만만치 않은데, 어느 정도 왔다 싶으면 위에서 어린애만 한 돌덩이가 와르르 쏟아진다.

청풍의 천진난만한 외침은 덤이다.



‘은인, 돌 굴러가요!’



이건 당해 본 사람만 안다. 석가모니가 내 입장이었어도 염주로 저놈 목 졸라 죽였다.

‘다시 생각하니까 열받네.’

그냥 확 들이받아 버릴까.

주먹을 움켜쥔 그때, 바닥에 누워 손가락만 움찔거리던 혁무진이 비명과 함께 벌떡 일어났다.

“끼아아아아아!”

“야, 야. 숨 쉬어, 숨. 여기 땅이야.”

“허억, 허어어억. 저 살아 있는 거 맞습니까?”

“그래, 인마. 아직 살아 있어.”

“무, 물 좀.”

청풍이 허리춤에 찬 죽통을 내밀었다.

“여기요.”

“고맙…….”

무심코 죽통을 받아 들던 혁무진의 신형이 우뚝 굳었다.

그리고 곧이어 터져 나오는 사자후.

“야, 이 개새끼야!”

눈이 뒤집혀 날뛰는 혁무진의 모습에 청풍이 기겁했다.

“저, 저한테 갑자기 왜 이러세요!”

“지금 몰라서 묻냐? 조장, 저 새끼 잡아요!”

“저는 할아버지께 배운 그대로 해 드리고 있는 건데.”

“당장 이리 안 와!”

“은인, 이따 위에서 뵐게요!”

혁무진을 피해 후다닥 물러난 청풍이 땅을 박찼다.

쾅! 단번에 십여 미터를 날아오른 녀석은 절벽에 철썩 달라붙더니 벽호공을 펼쳐 절벽을 올라가기 시작했다.

파파파파팍!

역시 고인물.

태어날 때부터 사족보행이었던 것처럼 빠르게 사라지는 청풍의 모습에 혁무진이 주저앉았다.

“저, 저 자식이 저한테 돌을, 돌을…….”

내가 숙연하게 대답했다.

“알아. 아까 너 떨어지는 거 봤어. 눈에 맞았더라.”

“저거 완전히 미친놈이에요. 어린애 머리통만 한 걸 던져요.”

“내 것보다는 작네. 나한텐 흙도 뿌리던데.”

“조장. 저 결심했습니다.”

“뭘?”

“저놈 잡아서 족치기 전까지는 포기 안 합니다. 사나이 혁무진의 이름을 걸고 맹세하는 거예요.”

혁무진의 눈동자가 이글이글 타올랐다.

지금처럼 열의에 불타는 모습은 처음 본다. 속마음은 어떨지 몰라도 표면적으로는 늘 유쾌하고 설렁설렁한 녀석이었으니까.

‘설마 이걸 노리고?’

이 모든 게 혁무진의 분노를 끌어 올려 최선을 다하게 만들려는 청풍의…….

아니다. 저 화산파 출신 자연인에게는 그런 머리가 없다.

‘뭐, 좋은 게 좋은 거지.’

씩씩거리는 혁무진에게 보퉁이 하나를 던졌다.

“품에 잘 챙겨 놔.”

“이게 뭡니까?”

“벽곡단. 수련 시작 전에 챙겨 놨었지.”

허기와 기력을 보충하는 것에는 저만한 게 없다. 크기가 작고 무게가 가벼우니 휴대도 간편하고.

“올라가다가 힘 딸린다 싶으면 먹어라.”

“사방이 낭떠러지인데 벽곡단을 어디서 먹습니까. 전 당장 올라가서 저놈을 단칼에…….”

“단칼에 죽을걸.”

새로 배운 벽호공으로 북망산을 타고 싶은 모양이다. 나는 혁무진의 뒤통수를 갈겼다.

“악!”

“그리고 절벽이 일직선이냐? 중간중간 깎여 있는 곳도 있으니까 알아서 자리 잡고 먹어. 조급해하다가 떨어지지 말고 천천히, 한 번에 성공하겠다는 생각으로 해.”

“후우.”

“그럼 가자.”

“옛!”

나와 혁무진이 결연한 표정으로 절벽 앞에 섰을 때였다.

“저기…….”

“사, 삼공자님.”

맞다. 이 사람들도 있었지.

장칠득과 중년 아재가 머뭇거리며 입을 열었다.

“소가주님께 보고를 해도 괜찮겠습니까?”

“아무래도 사안이 사안인지라. 공자님께서 부상이라도 입으시면 저희가…….”

손을 들어 그들의 말을 막았다.

뒷말은 듣지 않아도 충분히 짐작할 수 있었다. 직장인들 입장은 내가 더 잘 안다.

“보고하세요, 단.”

“단?”

“근무 끝나고 난 후에. 지금 얼마나 남았죠?”

“이제 세 시진 정도 남았습니다.”

“그 정도면 충분해요.”

벌써 절벽을 오르기 시작한 지 반나절.

남은 세 시진 안에 이 지긋지긋한 절벽을 정복할 생각이었다.



* * *



높고 가파른 이 이름 모를 절벽은 세월을 고스란히 맞아 어느 부분은 울퉁불퉁하고, 또 어떤 부분은 매끄럽다.

두꺼운 뿌리나 암석이 튀어나와 있어 잡기 쉬운 구간이 있는가 하면 조그마한 틈에 손가락 하나를 끼워 넣어 버텨야 할 때도 있었다.

‘하다못해 공력이나 병장기를 쓰면 편해질 텐데.’

공력을 사용하면 단단한 암석도 두부처럼 으스러진다.

인벤토리에 있는 병장기를 꺼낸다면 단검을 계단처럼 박아가며 올라갈 수 있다.

굳이 손쉬운 방법을 놔두고 이 고생을 하는 이유는 수련이기 때문……인 것도 있지만 그렇게 하려고 할 때마다 청풍이 귀신같이 알아차리고 돌을 떨구기 때문이다.

투두두둑.

갑자기 위에서 돌가루가 쏟아진다는 건 불길한 징조다.

나와 혁무진은 황급히 팔로 머리를 가리고 외쳤다.

“안 했어요! 진짜 아무것도 안 했어! 돌 굴리지 마!”

“으어어어!”

저 위에서 희멀건 얼굴이 빼꼼 튀어나왔다.

“진짜요?”

우리는 미친 듯이 고개를 끄덕였다.

아직 절반도 못 왔다. 여기서 스톤 샤워를 맞고 떨어지면 올라오기 전 호언장담했던 것이 흑역사가 될 거다.

“믿어 주세요!”

“청풍 소협! 아니, 청풍 대협!”

“할아버지께서 그러셨어요. 수련에는 결코 꼼수가 있어서는 안 된다. 무공은 피와 땀으로 얻어지는 것이다.”

일장 연설을 늘어놓은 청풍이 선심 쓴다는 듯이 한마디를 덧붙였다.

“이번 한 번만 봐드릴게요.”

“…….”

“…….”

아주 상전이 따로 없다. 나와 혁무진은 분통을 참으며 다시 절벽을 오르기 시작했다.

아주 사소한 실수 하나만 해도 다시 저 아래로 곤두박질치는 상황.

이렇다 보니 감각이 날카로워지고 손가락, 발가락 하나하나에 엄청난 신경을 기울이게 된다.

‘겨울만 아니었어도 진작 올라갔을 텐데…….’

올라가면 갈수록 경사는 험난했고, 표면은 밋밋해졌다.

가뜩이나 미끄러운 절벽이다. 그런데 심지어 하루가 멀다고 산발적으로 흩날리는 눈발과 북쪽 고원에서 불어온 바람이 절벽을 거대한 얼음으로 만들어 버렸다.

‘막혔다. 도무지 길이 안 보여.’

입술을 잘근잘근 깨무는 내 시선에 문득 뭔가가 눈에 들어왔다. 아직 얼지 않은 눈덩이로 막혀 있는 바위 틈새.

손가락 하나 들어갈까 말까 한 작은 공간이다. 힘들겠지만 지금으로써는 별수 없다.

“흡!”

나는 기합과 함께 몸을 날렸다. 동시에 가장 작은 새끼손가락을 정확히 틈새에 꽂아 넣었다.

푹, 내 예상은 절반만 맞았다. 아직 얼지 않은 눈덩이는 뚫어 낼 수 있었지만, 틈새의 깊이가 생각보다 너무 짧다.

고작 손가락 한 마디. 그것도 새끼손가락으로 0.1t에 달하는 몸무게를 지탱해야 한다.

“끄응.”

아무리 나라고 해도 이건 좀 빡센데?

설상가상으로 틈새에 고인 물기 때문에 손가락이 서서히 미끄러지는 중이다.

‘시간을 지체하면 추락한다.’

이제 얼마 남지 않았다. 나는 호흡을 가다듬고 몸의 긴장을 가라앉혔다. 새끼손가락을 지지대 삼아 전신을 들어 올렸다.

그야말로 초인(超人)이라 불릴 만한 신체 능력.

띠링.



- [근력]이 1 상승했습니다.

- [민첩]이 1 상승했습니다.

- [체력]이 1 상승했습니다.



때마침 스탯 상승까지. 회심의 미소를 지으며 다음 틈새를 향해 손을 뻗으려던 그때였다.

‘흡!’

“조장!”

이런, 중요한 순간에 호흡이 흐트러졌다. 다시 호흡을 가다듬는데 혁무진의 외침이 이어졌다.

“이! 이!”

“뭐라는 거야! 잘 안 들려!”

세차게 불어오는 눈바람은 시야와 소리를 흩어 놓았다.

내가 다시 입을 떼려는데, 또렷한 고함이 귓가를 후려쳤다.

“위! 위요!”

“위?”

혁무진의 목소리가 들렸다는 것은 맹렬한 바람이 주춤했다는 뜻. 그제야 막혔던 시야가 트이고 귀가 뚫렸다.

나는 혁무진의 손짓을 따라 고개를 들어 마침내 목격했다.

얼굴을 향해 떨어지는 거대한 바위를.

후우우웅!

“아, 시바.”

쾅!



* * *



“와, 그 큰 바위를 맨주먹으로 깨트리실 줄이야.”

청풍의 감탄을 한 귀로 흘리고 털썩 드러누웠다.

아까만 해도 저 자식을 두들겨 패고 싶은 마음뿐이었는데, 지금은 진이 다 빠졌다.

‘올라왔다. 끝났다!’

손 하나 까딱하지 못하고 속으로만 환호를 지르고 있을 때, 푸르딩딩하게 얼어붙은 손이 정상을 짚었다.

“허억. 흐어억.”

“겨우 하루 만에 성공하시다니! 두 분 다 너무 대단해요!”

너만 아니었어도 한 시진 안에 성공했어, 인마.

한바탕 쏘아 주고 싶은데 힘들어서 말이 안 나온다. 성취감과 피로로 헉헉거리는 우리를 보며 청풍이 허리를 꾸벅 숙였다.

“정말 고생하셨습니다! 한 번 성공한 경험이 있으니 남은 아홉 번은 더 빨리 오르실 수 있을 거예요.”

“……?”

“……?”

얼마나 충격적인 말이었던지, 나와 혁무진은 숨을 몰아쉬는 것도 잊고 청풍을 바라봤다.

‘저게 무슨 말이야.’

설마 지금 내가 생각한 그건가? 아니겠지?

나는 현대 사회의 지식인답게 침착한 태도로 입을 열었다.

“아홉 번이라니. 그게 무슨 개소리십니까?”

“저희 할아버지께서…….”

이 자식은 자연인이야, 소년 탐정이야.

이 순간만큼은 검성이고 나발이고 눈이 뒤집힐 수밖에 없었다.

“그러니까 이걸 아홉 번을 더 하라고요?”

“네!”

“당신은 똑같이 여기서 바위 던지고?”

“네!”

“안 해.”

“네?”

나와 혁무진이 동시에 자리에 드러누웠다.

“안 한다고. 내려갈 힘도 없어. 배 째.”

“내 배도 째라. 이 악랄한 놈아!”

“푸헤헤.”

“……웃어?”

청풍이 싱글벙글 웃으며 말했다.

“죄송해요. 제가 처음 수련 시작했을 때 모습을 보는 것 같아서 그만.”

“거봐! 당신도 하기 싫었잖아!”

“아뇨. 전 재밌어서 계속하고 싶었는데 몸이 안 따라 주더라고요.”

혁무진이 내게만 들릴 정도로 작은 목소리로 중얼거렸다.

“……미친놈인가.”

“그래서 할아버지께 말씀드렸죠. 다리가 말을 안 들으니 내일 이어서 하면 안 되겠냐고.”

행복한 과거를 회상하던 청풍이 돌연 검을 뽑아 들었다. 동시에 자줏빛 검기가 발출됐다.

서걱.

얼음, 흙, 바위. 가릴 것 없이 모두 베어 버린 청풍이 말을 이었다.

“그랬더니 할아버지께서 대답하셨어요. 올라오는 게 어렵지. 내려가는 건 쉽다고. 잠깐만 참으면 금방 내려간다고요.”

쿠구구궁.

딱 나와 혁무진이 누워 있는 3평 남짓한 절벽의 끄트머리가 진동했다.

‘실화냐.’

멍해 있는 우리에게 청풍이 손을 흔들었다.

“아홉 번 남았어요.”

띠링.



- 퀘스트, [검성 수련 간접체험기]가 생성되었습니다.
```

## Final English reading copy

```markdown
# Chapter 153

“So…”

Jang Childeuk continued haltingly.

“You were training?”

“Yes.”

“Were you perhaps practicing the Wall Lizard Technique?”

“I’m not entirely sure myself, but I think so.”

The Wall Lizard Technique. I’d seen it plenty of times in wuxia novels.

Apparently, it had been created by observing lizards climbing walls.

It was similar to the real-world sport of climbing, but there were two key differences.

First, unlike climbing, it used internal energy.

Second, there were no safety devices.

*This really is the Murim. No holding back.*

If you fell, you were as good as dead. It was the ultimate macho martial art.

When I nodded, the two men stared at me as though I were a ghost.

“From this height?”

“Is that even possible?”

“It worked.”

When I first heard Cheongpung suggest it, I had wondered what kind of insane nonsense he was talking about, too. But once I tried it, it worked.

It had only seemed unrealistic because I had never attempted it before. My body had already entered the realm of the superhuman—it would not be an exaggeration to say so.

“Oh, my. Third Young Master, what will you do if something serious happens to you?”

The middle-aged guy fussed as he brushed the dust off my clothes.

Only three minutes ago, he had treated me like a jiangshi from Taecho Village. Now he was handling me as carefully as though I were his family’s precious only son, three generations in the making.

“Well, why don’t you stop training for now and return to your quarters?”

“Why?”

“What do you mean, why? You were lucky this time, but if you fall one more time, you could really die.”

I waved a hand dismissively.

“It’s fine. It’s not like this was my first or second time.”

“What?”

“This is already the fifth time. Why are you acting surprised now?”

“The fifth… time?”

“Yes. Five times.”

His trembling eyes moved back and forth between me and the steep cliff.

“H-how are you still alive?”

“It’s fine. There’s someone who’s fallen more than ten times.”

“…”

“…”

“Looks like it’s about time for him to fall again… Oh, there he comes.”

I pointed toward a spot high up on the cliff. A black dot that grew larger by the second was followed by a piercing scream.

“Aaaaaaah! Caaaaaptain!”

The two men’s mouths fell open.

“My goodness. There really was someone else.”

“Who is that?”

“My right arm—no, my little toe.”

“What? What does that mean?”

“No, wait. Shouldn’t we save him right now?”

“Save him? Him?”

I shook my head.

Hyuk Mujin was a healthy adult man. If I tried to catch him as he fell from that height, it would end with more than just a broken bone somewhere.

“Just leave him alone. Don’t get involved and hurt yourselves.”

The two men screamed.

“He’s falling! He’s falling!”

“He’ll die if you leave him like this!”

“He won’t die.”

If he could die from this, he would have died ten times over by now.

But Hyuk Mujin had a lifeline—a sturdy rope that always saved him at the very last moment.

“Aaaaaaah!”

Hyuk Mujin’s scream drew closer by the second. At last, even his horrified expression became clearly visible.

That was when a streak of light flashed above us.

The thing plunging downward at meteor-like speed was glowing with a soft purple light.

“W-what is that…?”

“What is it?”

I answered briefly.

“The Zaha Divine Technique.”

More precisely, it was someone channeling the Zaha Divine Technique.

The two men could not see him, but I could clearly make out Cheongpung, wrapped in the distinctive purple qi of the Zaha Divine Technique.

He was grinning from ear to ear.

“Whoooooa!”

“…”

Look at that bastard having the time of his life.

His personality might have been a little unhinged, but when it came to ability, he was in a league of his own. I could only marvel at what happened next.

*How is that even possible?*

Shot forward like an arrow, Cheongpung snatched Hyuk Mujin by the waist in the blink of an eye.

Then he extended his palm toward the ground rushing up beneath them.

*Bang! Boom-boom!*

Once. Twice. Three times…

With each explosion of compressed air, the ground caved in.

Would this be what happened if an invisible giant pounded the earth with its fists?

Every time Cheongpung struck out with a palm, the frozen ground flipped over. The resulting recoil stopped the falling figure in midair.

A moment later, Cheongpung’s feet landed lightly on the ground.

“Whew, that was fun again. Right?”

Hyuk Mujin, already unconscious, groaned.

“Uhh… uhhh.”

“I knew you’d like it.”

“…”

How exactly did it look like he was enjoying himself?

Cheongpung cheerfully set Hyuk Mujin down, then acknowledged my presence.

“Oh, Benefactor! You’re still here?”

“I fell, remember? Thanks to someone.”

I glared steadily at Cheongpung.

In fact, I had already had several chances to reach the summit. The problem was that Cheongpung was not exactly a man in possession of an ordinary state of mind.

“Hehe. It makes me happy that you say it was thanks to me.”

“Shut up! I would’ve reached the top ages ago if you hadn’t done anything but interfere from up there!”

“Gasp! Please calm down, Benefactor!”

“Calm down? You should have said that before rolling rocks down at me!”

Think about it.

Climbing a cliff more than a hundred jang high with your bare hands was no easy feat to begin with. But every time I thought I had made decent progress, rocks the size of children came tumbling down from above.

Cheongpung’s innocent cries were an added bonus.

*Benefactor, rocks are rolling!*

Only someone who had experienced it could understand. Even if Shakyamuni himself had been in my position, he would have strangled that bastard to death with his prayer beads.

*Now that I think about it, I’m getting pissed off again.*

Should I just go at him?

Just as I clenched my fist, Hyuk Mujin, who had been lying on the ground and twitching only his fingers, suddenly sprang upright with a scream.

“Aaaaaaaah!”

“Hey, hey. Breathe. Take a breath. You’re on the ground.”

“Huff, huff. Am I really alive?”

“Yeah, you idiot. You’re still alive.”

“W-water, please.”

Cheongpung held out the bamboo tube hanging from his waist.

“Here.”

“Thank you…”

Hyuk Mujin absentmindedly accepted the bamboo tube, then froze stiff.

A moment later, a roar burst from him.

“You fucking bastard!”

Cheongpung recoiled in alarm at the sight of Hyuk Mujin running wild with his eyes rolling back.

“W-why are you suddenly acting like this toward me?”

“You’re asking because you don’t know? Captain, catch that bastard!”

“I’m only doing exactly what my grandfather taught me.”

“Get over here right now!”

“See you up there later, Benefactor!”

Cheongpung hurriedly backed away from Hyuk Mujin, then kicked off the ground.

*Boom!*

He shot more than ten meters into the air in a single bound, slapped onto the cliff, and began climbing with the Wall Lizard Technique.

*Papapapapak!*

Now that was a true veteran.

Cheongpung vanished so quickly that he looked as though he had been born walking on all fours. Hyuk Mujin sank to the ground.

“That bastard threw rocks at me. Rocks…”

I answered solemnly.

“I know. I saw you fall earlier. One hit you right in the eye.”

“He’s completely insane. He throws rocks as big as a child’s head.”

“That’s smaller than what he threw at me. He even threw dirt at me.”

“Captain. I’ve made up my mind.”

“About what?”

“I won’t give up until I catch that bastard and beat the shit out of him. I swear it on the name of Hyuk Mujin, a true man.”

Hyuk Mujin’s eyes burned fiercely.

I had never seen him so fired up. No matter what he was like inside, on the surface he had always been cheerful and carefree.

*Could this have been what he was aiming for?*

Was all of this Cheongpung’s way of drawing out Hyuk Mujin’s anger so that he would give it his all?

No. That nature-loving Huashan guy did not have the brains for that.

*Well, as long as it works out.*

I threw a bundle at the huffing Hyuk Mujin.

“Keep it secure inside your clothes.”

“What is this?”

“Fasting pills. I packed them before we started training.”

There was nothing better for replenishing hunger and energy. They were small and light, making them easy to carry, too.

“Eat them if you start running out of strength on the way up.”

“We’re surrounded by cliffs. Where am I supposed to eat fasting pills? I’m going up there right now and cutting that bastard down in one stroke…”

“You’ll be the one who dies in one stroke.”

Apparently, he wanted his newly learned Wall Lizard Technique to take him straight to Mount Beimang. I smacked Hyuk Mujin on the back of the head.

“Ow!”

“And it’s not like the cliff is sheer all the way up. There are ledges here and there, so find a place to stop and eat. Don’t fall because you’re in a hurry. Take it slowly, thinking only about succeeding in one attempt.”

“Hoo.”

“Then let’s go.”

“Yes, Captain!”

Hyuk Mujin and I were standing before the cliff with determined expressions when—

“Um…”

“T-Third Young Master.”

Right. These two were here, too.

Jang Childeuk and the middle-aged guy hesitantly opened their mouths.

“Would it be all right if we reported this to the Lesser Family Head?”

“Considering the circumstances… If you suffer even an injury, Young Master, then we…”

I raised a hand to stop them.

I could easily guess what they were going to say next. I knew the perspective of ordinary employees better than anyone.

“Report it, but…”

“But?”

“After your shift ends. How much time is left?”

“About three shichen.”

“That’s enough.”

It had already been half a day since I started climbing the cliff.

I intended to conquer this maddening cliff within the remaining three shichen.

* * *

This tall, steep, nameless cliff had endured the passage of time. Some sections were uneven, while others were smooth.

In some places, thick roots or rocks jutted out, making them easy to grab. In others, I had to wedge a single finger into a tiny crack and hang on.

*It would be much easier if I could use internal energy or a weapon, at least.*

With internal energy, even solid rock would crumble like tofu.

If I took a weapon from my inventory, I could drive daggers into the cliff like steps and climb that way.

The reason I was going through all this trouble instead of taking the easy route was because this was training…

Well, that was part of it. But every time I tried to use an easier method, Cheongpung would somehow sense it and drop rocks on me.

*Thud-thud-thud.*

A sudden shower of rock dust from above was an ominous sign.

Hyuk Mujin and I hurriedly covered our heads with our arms and shouted.

“We didn’t do anything! Seriously, we didn’t do anything! Don’t roll any rocks!”

“Uuughhh!”

A pale face cautiously poked out from above.

“Really?”

We nodded frantically.

We had not even made it halfway. If we were hit by a stone shower and fell now, all the bold claims we had made before climbing would become a humiliating memory.

“Please believe us!”

“Young Hero Cheongpung! No, Great Hero Cheongpung!”

“My grandfather always said that there must never be any tricks in training. Martial arts are gained through blood and sweat.”

After delivering a full speech, Cheongpung added one more sentence as though he were showing us mercy.

“I’ll let it go just this once.”

“…”

“…”

He was acting like an absolute tyrant.

Suppressing our outrage, Hyuk Mujin and I started climbing the cliff again.

We were in a situation where even the slightest mistake would send us hurtling back down below.

As a result, our senses grew sharper, and we had to pay tremendous attention to every single finger and toe.

*If it weren’t winter, I would have reached the top long ago…*

The higher we climbed, the more treacherous the slope became and the smoother the surface grew.

The cliff was already slippery enough. On top of that, the scattered snow flurries that came almost every day and the wind blowing in from the northern Gaoyuan had turned it into one enormous sheet of ice.

*I’m blocked. I can’t see a path at all.*

As I bit down on my lip, something suddenly caught my eye.

A crack in the rock blocked by a snowball that had not yet frozen.

It was a tiny space, barely wide enough for one finger. It would be difficult, but I had no other choice.

*Hup!*

I launched myself forward with a shout, simultaneously jamming my smallest finger—the little finger—precisely into the crack.

*Thud.*

My prediction had been only half right. I could break through the unfrozen snowball, but the crack was much shallower than I had expected.

It was barely one finger joint deep. And I had to support a body weighing 0.1 tons with my little finger.

“Ungh.”

Even for me, this was a bit much.

To make matters worse, my finger was slowly slipping because of the moisture pooled inside the crack.

*If I waste any more time, I’ll fall.*

There was not much farther to go. I steadied my breathing and calmed the tension in my body. Using my little finger as a support, I lifted my entire body.

Physical ability worthy of being called superhuman.

> **System**
>
> - **Strength** increased by 1.
>
> - **Agility** increased by 1.
>
> - **Stamina** increased by 1.

The stat increase came at exactly the right moment.

Just as I smiled triumphantly and reached toward the next crack—

*Hup!*

“Captain!”

Damn it. My breathing had faltered at the worst possible moment. I steadied my breathing again, but Hyuk Mujin continued shouting.

“Th-this! This!”

“What are you saying? I can’t hear you!”

The fierce snowstorm scattered both sound and visibility.

I was about to open my mouth again when a clear shout struck my ears.

“Above! Above!”

“Above?”

The fact that I could hear Hyuk Mujin’s voice meant the savage wind had paused. Only then did my obstructed vision clear and my ears open.

Following Hyuk Mujin’s gesture, I raised my head and finally saw it.

A massive boulder falling straight toward my face.

*Whoooosh!*

“Ah, shit.”

*Boom!*

* * *

“Wow. I can’t believe you broke such a huge boulder with your bare fist.”

I let Cheongpung’s admiration go in one ear and collapsed onto my back.

Only a moment ago, I had wanted nothing more than to beat that bastard senseless. Now I was completely drained.

*I made it up. It’s over!*

Just as I lay there, unable to move even a hand and cheering inwardly, a bluish, frozen hand reached the summit.

“Huff. Haaah.”

“You succeeded in only one day! You’re both incredible!”

If it weren’t for you, I would have done it in one shichen, you idiot.

I wanted to lay into him, but I was too exhausted to speak. As Hyuk Mujin and I panted from a mixture of accomplishment and fatigue, Cheongpung bowed deeply at the waist.

“You’ve both worked so hard! Now that you’ve succeeded once, you should be able to climb the remaining nine times much faster.”

“…”

“…”

The statement was so shocking that Hyuk Mujin and I stared at Cheongpung without even remembering to breathe.

*What is he talking about?*

Could he possibly mean what I thought he meant?

No, surely not.

As an intellectual of modern society, I opened my mouth with a calm demeanor.

“The remaining nine times? What kind of bullshit is that?”

“My grandfather…”

This guy was either a mountain hermit or a boy detective.

At that moment, Sword Saint be damned—I couldn’t help but see red.

“So you’re telling us to do this nine more times?”

“Yes!”

“You’re going to keep throwing rocks at us from up here?”

“Yes!”

“No.”

“What?”

Hyuk Mujin and I simultaneously collapsed onto the ground.

“I’m not doing it. I don’t even have the strength to go back down. Go ahead and gut me.”

“Gut me too, you vicious bastard!”

“Puhahaha.”

“Are you laughing?”

Cheongpung smiled brightly.

“Sorry. You looked just like me when I first started training, so I couldn’t help it.”

“See? You didn’t want to do it either!”

“No. I thought it was fun and wanted to keep going, but my body wouldn’t keep up.”

Hyuk Mujin muttered in a voice so quiet that only I could hear.

“…Is he insane?”

“So I told my grandfather. I asked whether I could continue the next day because my legs wouldn’t listen to me.”

As he reminisced about his happy past, Cheongpung suddenly drew his sword.

At the same time, purple Sword Energy shot forth.

*Shhk.*

Ice, dirt, rock—Cheongpung cut through all of it without distinction, then continued speaking.

“My grandfather answered that climbing up was difficult, but going down was easy. He said that if I endured it for just a little while, I would be back down in no time.”

*Rumble, rumble, rumble.*

The edge of the cliff ledge where Hyuk Mujin and I were lying—barely ten square meters in size—began to shake.

*Is this for real?*

As we lay there in a daze, Cheongpung waved at us.

“Nine more to go.”

> **System**
>
> - The Quest **Sword Saint Training: A Secondhand Experience** has been generated.
```
